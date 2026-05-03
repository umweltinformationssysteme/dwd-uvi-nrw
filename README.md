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
**Updated:** 2026-05-03 07:30 UTC &nbsp;|&nbsp; **Generated:** 2026-05-03 10:05 UTC

| District / City | DWD Station | Today (Sun 03.05.) | Tomorrow (Mon 04.05.) | Day after (Tue 05.05.) |
|---|---|:---:|:---:|:---:|
| Aachen (Stadt) | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Bielefeld | Osnabrück | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Bochum | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Bonn (Stadt) | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Borken | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Bottrop | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Coesfeld | Osnabrück | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Dortmund | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Duisburg | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Düren | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Düsseldorf (Stadt) | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Ennepe-Ruhr-Kreis | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Essen | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Euskirchen | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Gelsenkirchen | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Gütersloh | Osnabrück | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Hagen | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Hamm | Osnabrück | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Heinsberg | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Herford | Osnabrück | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Herne | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Hochsauerlandkreis | Kahler Asten | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 |
| Höxter | Kassel | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 |
| Kleve | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Krefeld | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Köln (Stadt) | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Leverkusen | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Lippe | Kassel | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 |
| Mettmann | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Minden-Lübbecke | Hannover | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Märkischer Kreis | Kahler Asten | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 |
| Mönchengladbach | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Mülheim an der Ruhr | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Münster | Osnabrück | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Oberbergischer Kreis | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Oberhausen | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Olpe | Kahler Asten | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 |
| Paderborn | Kahler Asten | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 |
| Recklinghausen | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Remscheid | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Rhein-Erft-Kreis | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Rhein-Kreis Neuss | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Rhein-Sieg-Kreis | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Rheinisch-Bergischer Kreis | Bonn | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Siegen-Wittgenstein | Kahler Asten | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 |
| Soest | Kahler Asten | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 |
| Solingen | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Steinfurt | Osnabrück | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Unna | Kahler Asten | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 |
| Viersen | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Warendorf | Osnabrück | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Wesel | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
| Wuppertal | Düsseldorf | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 |
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
