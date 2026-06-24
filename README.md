# UV Index NRW

Daily UV index forecast for all 53 districts and independent cities
in North Rhine-Westphalia (NRW), Germany. Updated automatically every morning.

Data is sourced from the **German Weather Service (DWD)** via their open data API.
Since the DWD provides values for ~38 measurement stations nationwide rather than
per district, each district is assigned its geographically nearest station using
the Haversine formula. The primary stations covering NRW are Düsseldorf, Bonn,
Kahler Asten, and Osnabrück.

## Repository structure

```
dwd-uvi-nrw/
├── .github/workflows/update.yml   # GitHub Actions: runs daily at 09:00 UTC
├── scripts/fetch_uvi.py           # Fetches data, writes JSON and updates README
├── data/uvi_nrw.json              # Machine-readable output (refreshed daily)
├── README.md                      # This file (table section updated daily)
└── requirements.txt
```

## Data source

| Field | Value |
|---|---|
| Provider | Deutscher Wetterdienst (DWD) |
| Dataset | UV-Gefahrenindex Open Data |
| URL | https://opendata.dwd.de/climate_environment/health/alerts/uvi.json |
| Licence | [Data licence Germany – attribution – version 2.0](https://www.govdata.de/dl-de/by-2-0) |
| Update frequency | Daily in the morning (~07:30–08:30 UTC) |

## Methodology

Each district is matched to the nearest DWD station by straight-line distance
(Haversine). No spatial interpolation is performed. The UV index value of the
matched station is used as-is for that district.

## Legend

| UV Index | Risk level | Colour |
|:---:|---|---|
| 1 | low | ![](https://placehold.co/18x18/339C23/339C23.png) |
| 2 | low | ![](https://placehold.co/18x18/9CC401/9CC401.png) |
| 3 | moderate | ![](https://placehold.co/18x18/FFF200/FFF200.png) |
| 4 | moderate | ![](https://placehold.co/18x18/FED300/FED300.png) |
| 5 | moderate | ![](https://placehold.co/18x18/F7AF00/F7AF00.png) |
| 6 | high | ![](https://placehold.co/18x18/EF8300/EF8300.png) |
| 7 | high | ![](https://placehold.co/18x18/EA6003/EA6003.png) |
| 8 | very high | ![](https://placehold.co/18x18/D90017/D90017.png) |
| 9 | very high | ![](https://placehold.co/18x18/FF009A/FF009A.png) |
| 10 | very high | ![](https://placehold.co/18x18/B64BFF/B64BFF.png) |
| 11+ | extreme | ![](https://placehold.co/18x18/9A8DFF/9A8DFF.png) |

Each row in the table below shows a colour swatch alongside the numeric UV value.

## UV index by district

<!-- UV-TABLE-START -->
**Updated:** 2026-06-24 07:30 UTC &nbsp;|&nbsp; **Generated:** 2026-06-24 11:45 UTC

| District / City | DWD Station | Today (Wed 24.06.) | Tomorrow (Thu 25.06.) | Day after (Fri 26.06.) |
|---|---|:---:|:---:|:---:|
| Aachen (Stadt) | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Bielefeld | Osnabrück | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Bochum | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Bonn (Stadt) | Bonn | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Borken | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Bottrop | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Coesfeld | Osnabrück | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Dortmund | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Duisburg | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Düren | Bonn | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Düsseldorf (Stadt) | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Ennepe-Ruhr-Kreis | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Essen | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Euskirchen | Bonn | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Gelsenkirchen | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Gütersloh | Osnabrück | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Hagen | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Hamm | Osnabrück | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Heinsberg | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Herford | Osnabrück | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Herne | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Hochsauerlandkreis | Kahler Asten | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 |
| Höxter | Kassel | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Kleve | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Krefeld | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Köln (Stadt) | Bonn | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Leverkusen | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Lippe | Kassel | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Mettmann | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Minden-Lübbecke | Hannover | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Märkischer Kreis | Kahler Asten | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 |
| Mönchengladbach | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Mülheim an der Ruhr | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Münster | Osnabrück | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Oberbergischer Kreis | Bonn | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Oberhausen | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Olpe | Kahler Asten | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 |
| Paderborn | Kahler Asten | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 |
| Recklinghausen | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Remscheid | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Rhein-Erft-Kreis | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Rhein-Kreis Neuss | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Rhein-Sieg-Kreis | Bonn | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Rheinisch-Bergischer Kreis | Bonn | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Siegen-Wittgenstein | Kahler Asten | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 |
| Soest | Kahler Asten | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 |
| Solingen | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Steinfurt | Osnabrück | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Unna | Kahler Asten | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 |
| Viersen | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Warendorf | Osnabrück | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Wesel | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
| Wuppertal | Düsseldorf | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![very high](https://placehold.co/18x18/D90017/D90017.png) 8 | ![high](https://placehold.co/18x18/EA6003/EA6003.png) 7 |
<!-- UV-TABLE-END -->

## Licence & attribution

The UV index data is provided by the **Deutscher Wetterdienst (DWD)** under the
[Data licence Germany – attribution – version 2.0](https://www.govdata.de/dl-de/by-2-0)
(Datenlizenz Deutschland – Namensnennung – Version 2.0).

When reusing the data from this repository, please include the following attribution:

> Datenbasis: Deutscher Wetterdienst, own calculations

---

*This repository is updated automatically every day by a
[GitHub Actions workflow](.github/workflows/update.yml).*
*Raw JSON data: [`data/uvi_nrw.json`](data/uvi_nrw.json)*
