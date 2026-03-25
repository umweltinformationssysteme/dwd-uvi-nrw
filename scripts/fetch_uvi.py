import requests
import json
import math
from datetime import datetime, timedelta
from pathlib import Path

# --- DWD-Stationen mit Koordinaten (nur relevante für NRW-Umgebung) ---
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

# --- Alle 53 NRW-Kreise und kreisfreie Städte ---
NRW_DISTRICTS = [
    {"name": "Aachen (Stadt)",           "lat": 50.776, "lon": 6.084},
    {"name": "Bielefeld",                "lat": 52.021, "lon": 8.532},
    {"name": "Bochum",                   "lat": 51.482, "lon": 7.216},
    {"name": "Bonn (Stadt)",             "lat": 50.735, "lon": 7.099},
    {"name": "Borken",                   "lat": 51.845, "lon": 6.858},
    {"name": "Bottrop",                  "lat": 51.524, "lon": 6.929},
    {"name": "Coesfeld",                 "lat": 51.945, "lon": 7.170},
    {"name": "Dortmund",                 "lat": 51.514, "lon": 7.466},
    {"name": "Duisburg",                 "lat": 51.435, "lon": 6.762},
    {"name": "Düren",                    "lat": 50.804, "lon": 6.495},
    {"name": "Düsseldorf (Stadt)",       "lat": 51.221, "lon": 6.776},
    {"name": "Ennepe-Ruhr-Kreis",        "lat": 51.343, "lon": 7.321},
    {"name": "Essen",                    "lat": 51.459, "lon": 7.012},
    {"name": "Euskirchen",               "lat": 50.660, "lon": 6.787},
    {"name": "Gelsenkirchen",            "lat": 51.517, "lon": 7.086},
    {"name": "Gütersloh",                "lat": 51.905, "lon": 8.382},
    {"name": "Hagen",                    "lat": 51.360, "lon": 7.474},
    {"name": "Hamm",                     "lat": 51.680, "lon": 7.816},
    {"name": "Heinsberg",                "lat": 51.063, "lon": 6.097},
    {"name": "Herford",                  "lat": 52.113, "lon": 8.673},
    {"name": "Herne",                    "lat": 51.538, "lon": 7.224},
    {"name": "Hochsauerlandkreis",       "lat": 51.312, "lon": 8.453},
    {"name": "Höxter",                   "lat": 51.770, "lon": 9.381},
    {"name": "Kleve",                    "lat": 51.789, "lon": 6.138},
    {"name": "Köln (Stadt)",             "lat": 50.938, "lon": 6.960},
    {"name": "Krefeld",                  "lat": 51.335, "lon": 6.586},
    {"name": "Leverkusen",               "lat": 51.045, "lon": 7.002},
    {"name": "Lippe",                    "lat": 51.917, "lon": 9.017},
    {"name": "Märkischer Kreis",         "lat": 51.215, "lon": 7.706},
    {"name": "Mettmann",                 "lat": 51.251, "lon": 6.977},
    {"name": "Minden-Lübbecke",          "lat": 52.290, "lon": 8.917},
    {"name": "Mönchengladbach",          "lat": 51.200, "lon": 6.440},
    {"name": "Mülheim an der Ruhr",      "lat": 51.430, "lon": 6.882},
    {"name": "Münster",                  "lat": 51.962, "lon": 7.626},
    {"name": "Oberbergischer Kreis",     "lat": 51.079, "lon": 7.560},
    {"name": "Oberhausen",               "lat": 51.470, "lon": 6.852},
    {"name": "Olpe",                     "lat": 51.028, "lon": 7.852},
    {"name": "Paderborn",                "lat": 51.720, "lon": 8.754},
    {"name": "Recklinghausen",           "lat": 51.614, "lon": 7.198},
    {"name": "Remscheid",                "lat": 51.180, "lon": 7.193},
    {"name": "Rhein-Erft-Kreis",         "lat": 51.022, "lon": 6.750},
    {"name": "Rhein-Kreis Neuss",        "lat": 51.200, "lon": 6.695},
    {"name": "Rheinisch-Bergischer Kreis","lat": 51.013, "lon": 7.196},
    {"name": "Rhein-Sieg-Kreis",         "lat": 50.783, "lon": 7.319},
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
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def nearest_station(district, uv_lookup):
    best_name, best_dist = None, float("inf")
    for st in DWD_STATIONS:
        if st["name"] not in uv_lookup:
            continue
        d = haversine(district["lat"], district["lon"], st["lat"], st["lon"])
        if d < best_dist:
            best_dist = d
            best_name = st["name"]
    return best_name, round(best_dist)


def uv_label(val):
    if val is None:
        return "–"
    if val <= 2:
        return "gering"
    if val <= 5:
        return "mäßig"
    if val <= 7:
        return "hoch"
    if val <= 9:
        return "sehr hoch"
    return "extrem"


def uv_color(val):
    if val is None:
        return "#ccc"
    if val <= 2:
        return "#5DCAA5"
    if val <= 5:
        return "#EF9F27"
    if val <= 7:
        return "#F0997B"
    if val <= 9:
        return "#E24B4A"
    return "#A32D2D"


def fetch_dwd():
    url = "https://opendata.dwd.de/climate_environment/health/alerts/uvi.json"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.json()


def build_results(dwd_data):
    uv_lookup = {item["city"]: item["forecast"] for item in dwd_data["content"]}
    forecast_day = dwd_data.get("forecast_day", "")
    last_update = dwd_data.get("last_update", "")

    results = []
    for district in NRW_DISTRICTS:
        station, dist_km = nearest_station(district, uv_lookup)
        forecast = uv_lookup.get(station, {}) if station else {}
        results.append({
            "kreis": district["name"],
            "station": station or "–",
            "station_km": dist_km,
            "today":    forecast.get("today"),
            "tomorrow": forecast.get("tomorrow"),
            "dayafter": forecast.get("dayafter_to"),
        })

    return results, forecast_day, last_update


def write_json(results, forecast_day, last_update):
    out = {
        "source": "Deutscher Wetterdienst – Open Data",
        "forecast_day": forecast_day,
        "last_update": last_update,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "data": results,
    }
    Path("data").mkdir(exist_ok=True)
    with open("data/uvi_nrw.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✓ data/uvi_nrw.json geschrieben")


def date_label(forecast_day, offset):
    d = datetime.strptime(forecast_day, "%Y-%m-%d") + timedelta(days=offset)
    return d.strftime("%a %d.%m.")


def write_readme(results, forecast_day, last_update):
    day0 = date_label(forecast_day, 0)
    day1 = date_label(forecast_day, 1)
    day2 = date_label(forecast_day, 2)

    def badge(val):
        if val is None:
            return "–"
        color = uv_color(val).lstrip("#")
        # GitHub README unterstützt kein inline-HTML in Tabellen zuverlässig,
        # daher wird der Wert als Text mit Emoji-Ampel dargestellt
        dot = "🟢" if val <= 2 else "🟡" if val <= 5 else "🟠" if val <= 7 else "🔴"
        return f"{dot} {val}"

    rows = "\n".join(
        f"| {r['kreis']} | {r['station']} | {badge(r['today'])} | {badge(r['tomorrow'])} | {badge(r['dayafter'])} |"
        for r in sorted(results, key=lambda x: x["kreis"])
    )

    readme = f"""# UV-Gefahrenindex NRW

Automatisch aktualisierte Übersicht des UV-Gefahrenindex für alle 53 Landkreise
und kreisfreien Städte in Nordrhein-Westfalen.

**Quelle:** [DWD Open Data](https://opendata.dwd.de/climate_environment/health/alerts/)  
**Stand:** {last_update.replace("T", " ").replace(":00", "", 1)} Uhr  
**Prognose ab:** {forecast_day}  
**Zuletzt generiert:** {datetime.utcnow().strftime("%d.%m.%Y %H:%M")} UTC

> Die Zuordnung erfolgt über die jeweils nächste DWD-Messstation.
> JSON-Daten: [`data/uvi_nrw.json`](data/uvi_nrw.json)

## Legende

| Symbol | UV-Index | Gefährdung |
|--------|----------|------------|
| 🟢 | 1–2 | gering |
| 🟡 | 3–5 | mäßig |
| 🟠 | 6–7 | hoch |
| 🔴 | 8–10 | sehr hoch / extrem |

## UV-Index nach Landkreis

| Landkreis / Stadt | DWD-Station | Heute ({day0}) | Morgen ({day1}) | Übermorgen ({day2}) |
|---|---|:---:|:---:|:---:|
{rows}

---
*Dieses Repository wird täglich automatisch durch einen [GitHub Actions Workflow](.github/workflows/update.yml) aktualisiert.*
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print("✓ README.md geschrieben")


if __name__ == "__main__":
    print("Lade DWD-Daten...")
    dwd_data = fetch_dwd()
    results, forecast_day, last_update = build_results(dwd_data)
    write_json(results, forecast_day, last_update)
    write_readme(results, forecast_day, last_update)
    print("Fertig.")
