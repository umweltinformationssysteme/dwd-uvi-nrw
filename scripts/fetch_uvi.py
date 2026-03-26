import requests
import json
import math
from datetime import datetime, timedelta
from pathlib import Path
import re

# --- DWD Stations with Coordinates (relevant for NRW and surrounding areas) ---
DWD_STATIONS = [
    {"name": "Düsseldorf",    "lat": 51.221, "lon": 6.776},
    {"name": "Bonn",          "lat": 50.735, "lon": 7.099},
    {"name": "Kahler Asten",  "lat": 51.180, "lon": 8.490},
    {"name": "Osnabrück",     "lat": 52.279, "lon": 8.052},
    {"name": "Kassel",        "lat": 51.296, "lon": 9.447},
    {"name": "Frankfurt/Main","lat": 50.033, "lon": 8.570},
    {"name": "Hannover",      "lat": 52.467, "lon": 9.685},
    {"name": "Hahn",          "lat": 49.948, "lon": 7.264},
]

# --- All 53 NRW Districts and Independent Cities ---
NRW_DISTRICTS = [
    {"name": "Aachen (City)",            "lat": 50.776, "lon": 6.084},
    {"name": "Bielefeld",                "lat": 52.021, "lon": 8.532},
    {"name": "Bochum",                   "lat": 51.482, "lon": 7.216},
    {"name": "Bonn (City)",              "lat": 50.735, "lon": 7.099},
    {"name": "Borken",                   "lat": 51.845, "lon": 6.858},
    {"name": "Bottrop",                  "lat": 51.524, "lon": 6.929},
    {"name": "Coesfeld",                 "lat": 51.945, "lon": 7.170},
    {"name": "Dortmund",                 "lat": 51.514, "lon": 7.466},
    {"name": "Duisburg",                 "lat": 51.435, "lon": 6.762},
    {"name": "Düren",                    "lat": 50.804, "lon": 6.495},
    {"name": "Düsseldorf (City)",        "lat": 51.221, "lon": 6.776},
    {"name": "Ennepe-Ruhr-District",     "lat": 51.343, "lon": 7.321},
    {"name": "Essen",                    "lat": 51.459, "lon": 7.012},
    {"name": "Euskirchen",               "lat": 50.660, "lon": 6.787},
    {"name": "Gelsenkirchen",            "lat": 51.517, "lon": 7.086},
    {"name": "Gütersloh",                "lat": 51.905, "lon": 8.382},
    {"name": "Hagen",                    "lat": 51.360, "lon": 7.474},
    {"name": "Hamm",                     "lat": 51.680, "lon": 7.816},
    {"name": "Heinsberg",                "lat": 51.063, "lon": 6.097},
    {"name": "Herford",                  "lat": 52.113, "lon": 8.673},
    {"name": "Herne",                    "lat": 51.538, "lon": 7.224},
    {"name": "Hochsauerland District",   "lat": 51.312, "lon": 8.453},
    {"name": "Höxter",                   "lat": 51.770, "lon": 9.381},
    {"name": "Kleve",                    "lat": 51.789, "lon": 6.138},
    {"name": "Cologne (City)",           "lat": 50.938, "lon": 6.960},
    {"name": "Krefeld",                  "lat": 51.335, "lon": 6.586},
    {"name": "Leverkusen",               "lat": 51.045, "lon": 7.002},
    {"name": "Lippe",                    "lat": 51.917, "lon": 9.017},
    {"name": "Märkischer District",      "lat": 51.215, "lon": 7.706},
    {"name": "Mettmann",                 "lat": 51.251, "lon": 6.977},
    {"name": "Minden-Lübbecke",          "lat": 52.290, "lon": 8.917},
    {"name": "Mönchengladbach",          "lat": 51.200, "lon": 6.440},
    {"name": "Mülheim an der Ruhr",      "lat": 51.430, "lon": 6.882},
    {"name": "Münster",                  "lat": 51.962, "lon": 7.626},
    {"name": "Oberbergischer District",  "lat": 51.079, "lon": 7.560},
    {"name": "Oberhausen",               "lat": 51.470, "lon": 6.852},
    {"name": "Olpe",                     "lat": 51.028, "lon": 7.852},
    {"name": "Paderborn",                "lat": 51.720, "lon": 8.754},
    {"name": "Recklinghausen",           "lat": 51.614, "lon": 7.198},
    {"name": "Remscheid",                "lat": 51.180, "lon": 7.193},
    {"name": "Rhein-Erft-District",      "lat": 51.022, "lon": 6.750},
    {"name": "Rhine-District Neuss",     "lat": 51.200, "lon": 6.695},
    {"name": "Rheinisch-Bergischer District","lat": 51.013, "lon": 7.196},
    {"name": "Rhine-Sieg-District",      "lat": 50.783, "lon": 7.319},
    {"name": "Siegen-Wittgenstein",      "lat": 50.875, "lon": 8.024},
    {"name": "Soest",                    "lat": 51.570, "lon": 8.108},
    {"name": "Solingen",                 "lat": 51.165, "lon": 7.083},
    {"name": "Steinfurt",                "lat": 52.150, "lon": 7.335},
    {"name": "Unna",                     "lat": 51.534, "lon": 7.685},
    {"name": "Viersen",                  "lat": 51.255, "lon": 6.397},
    {"name": "Warendorf",                "lat": 51.953, "lon": 7.994},
    {"name": "Wesel",                    "lat": 51.659, "lon": 6.615},
    {"name": "Wuppertal",                "lat": 51.257, "lon": 7.149},
]


def haversine(lat1, lon1, lat2, lon2):
    """Calculates the great-circle distance between two points."""
    R = 6371 # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def nearest_station(district, uv_lookup):
    """Finds the nearest DWD station for a given district."""
    best_name, best_dist = None, float("inf")
    for st in DWD_STATIONS:
        if st["name"] not in uv_lookup:
            continue
        d = haversine(district["lat"], district["lon"], st["lat"], st["lon"])
        if d < best_dist:
            best_dist = d
            best_name = st["name"]
    return best_name, round(best_dist)


UV_META = {
    1:  {"label": "low",       "color": "339C23"},
    2:  {"label": "low",       "color": "9CC401"},
    3:  {"label": "moderate",  "color": "FFF200"},
    4:  {"label": "moderate",  "color": "FED300"},
    5:  {"label": "moderate",  "color": "F7AF00"},
    6:  {"label": "high",      "color": "EF8300"},
    7:  {"label": "high",      "color": "EA6003"},
    8:  {"label": "very high", "color": "D90017"},
    9:  {"label": "very high", "color": "FF009A"},
    10: {"label": "very high", "color": "B64BFF"},
    11: {"label": "extreme",   "color": "9A8DFF"},
}

def uv_meta(val, key):
    fallback = {"label": "–", "color": "cccccc"}
    if val is None:
        return fallback[key]
    return UV_META.get(min(val, 11), UV_META[11])[key]

def uv_label(val):
    return uv_meta(val, "label")

def uv_color(val):
    return uv_meta(val, "color")


def fetch_dwd():
    """Fetches UV-Index data from DWD Open Data Portal."""
    url = "https://opendata.dwd.de/climate_environment/health/alerts/uvi.json"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.json()


def build_results(dwd_data):
    """Maps DWD forecast data to NRW districts."""
    uv_lookup = {item["city"]: item["forecast"] for item in dwd_data["content"]}
    forecast_day = dwd_data.get("forecast_day", "")
    last_update = dwd_data.get("last_update", "")

    results = []
    for district in NRW_DISTRICTS:
        station, dist_km = nearest_station(district, uv_lookup)
        forecast = uv_lookup.get(station, {}) if station else {}
        results.append({
            "district": district["name"],
            "station": station or "–",
            "station_km": dist_km,
            "today":    forecast.get("today"),
            "tomorrow": forecast.get("tomorrow"),
            "dayafter": forecast.get("dayafter_to"),
        })

    return results, forecast_day, last_update


def write_json(results, forecast_day, last_update):
    """Saves the results to a JSON file."""
    out = {
        "source": "German Weather Service (DWD) – Open Data",
        "forecast_day": forecast_day,
        "last_update": last_update,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "data": results,
    }
    Path("data").mkdir(exist_ok=True)
    with open("data/uvi_nrw.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✓ data/uvi_nrw.json written")


def date_label(forecast_day, offset):
    """Helper for date formatting."""
    try:
        d = datetime.strptime(forecast_day, "%Y-%m-%d") + timedelta(days=offset)
        return d.strftime("%a %b %d")
    except:
        return f"Day {offset}"


def write_readme(results, forecast_day, last_update):
    """Updates the UV-Index table in README.md."""
    day0 = date_label(forecast_day, 0)
    day1 = date_label(forecast_day, 1)
    day2 = date_label(forecast_day, 2)

    def badge(val):
        if val is None:
            return "–"
        color = uv_color(val)
        label = uv_label(val)
        return f"![{label}](https://placehold.co/18x18/{color}/{color}.png) {val}"

    rows = "\n".join(
        f"| {r['district']} | {r['station']} | {badge(r['today'])} | {badge(r['tomorrow'])} | {badge(r['dayafter'])} |"
        for r in sorted(results, key=lambda x: x["district"])
    )

    # Note: Using English headers for the table
    table_block = (
        f"\n"
        f"**Last Update:** {last_update.replace('T', ' ')[:16]} &nbsp;|&nbsp; "
        f"**Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC\n\n"
        f"| District / City | DWD Station | Today ({day0}) | Tomorrow ({day1}) | Day After ({day2}) |\n"
        f"|---|---|:---:|:---:|:---:|\n"
        f"{rows}\n"
        f""
    )

    readme_path = Path("README.md")
    if not readme_path.exists():
        print("! README.md not found, skipping table update.")
        return

    content = readme_path.read_text(encoding="utf-8")
    content = re.sub(
        r".*?",
        table_block,
        content,
        flags=re.DOTALL,
    )
    readme_path.write_text(content, encoding="utf-8")
    print("✓ README.md table updated")


if __name__ == "__main__":
    print("Fetching DWD data...")
    try:
        dwd_raw = fetch_dwd()
        results, f_day, l_update = build_results(dwd_raw)
        write_json(results, f_day, l_update)
        write_readme(results, f_day, l_update)
        print("Done.")
    except Exception as e:
        print(f"Error: {e}")
