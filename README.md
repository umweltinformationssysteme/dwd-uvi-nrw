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
**Updated:** 2026-04-04 07:30 UTC &nbsp;|&nbsp; **Generated:** 2026-04-04 10:55 UTC

| District / City | DWD Station | Today (Sat 04.04.) | Tomorrow (Sun 05.04.) | Day after (Mon 06.04.) |
|---|---|:---:|:---:|:---:|
| Aachen (Stadt) | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Bielefeld | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Bochum | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Bonn (Stadt) | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Borken | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Bottrop | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Coesfeld | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Dortmund | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Duisburg | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Düren | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Düsseldorf (Stadt) | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Ennepe-Ruhr-Kreis | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Essen | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Euskirchen | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Gelsenkirchen | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Gütersloh | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Hagen | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Hamm | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Heinsberg | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Herford | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Herne | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Hochsauerlandkreis | Kahler Asten | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Höxter | Kassel | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Kleve | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Krefeld | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Köln (Stadt) | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Leverkusen | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Lippe | Kassel | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Mettmann | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Minden-Lübbecke | Hannover | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Märkischer Kreis | Kahler Asten | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Mönchengladbach | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Mülheim an der Ruhr | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Münster | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Oberbergischer Kreis | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Oberhausen | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Olpe | Kahler Asten | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Paderborn | Kahler Asten | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Recklinghausen | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Remscheid | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Rhein-Erft-Kreis | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Rhein-Kreis Neuss | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Rhein-Sieg-Kreis | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Rheinisch-Bergischer Kreis | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Siegen-Wittgenstein | Kahler Asten | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Soest | Kahler Asten | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Solingen | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Steinfurt | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Unna | Kahler Asten | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Viersen | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Warendorf | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Wesel | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Wuppertal | Düsseldorf | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
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
