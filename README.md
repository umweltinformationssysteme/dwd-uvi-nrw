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
**Updated:** 2026-06-12 07:30 UTC &nbsp;|&nbsp; **Generated:** 2026-06-12 12:20 UTC

| District / City | DWD Station | Today (Fri 12.06.) | Tomorrow (Sat 13.06.) | Day after (Sun 14.06.) |
|---|---|:---:|:---:|:---:|
| Aachen (Stadt) | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Bielefeld | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Bochum | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Bonn (Stadt) | Bonn | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Borken | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Bottrop | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Coesfeld | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Dortmund | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Duisburg | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Düren | Bonn | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Düsseldorf (Stadt) | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Ennepe-Ruhr-Kreis | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Essen | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Euskirchen | Bonn | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Gelsenkirchen | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Gütersloh | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Hagen | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Hamm | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Heinsberg | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Herford | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Herne | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Hochsauerlandkreis | Kahler Asten | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![high](https://placehold.co/18x18/EF8300/EF8300.png) 6 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Höxter | Kassel | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Kleve | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Krefeld | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Köln (Stadt) | Bonn | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Leverkusen | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Lippe | Kassel | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Mettmann | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Minden-Lübbecke | Hannover | ![low](https://placehold.co/18x18/9CC401/9CC401.png) 2 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Märkischer Kreis | Kahler Asten | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![high](https://placehold.co/18x18/EF8300/EF8300.png) 6 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Mönchengladbach | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Mülheim an der Ruhr | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Münster | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Oberbergischer Kreis | Bonn | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Oberhausen | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Olpe | Kahler Asten | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![high](https://placehold.co/18x18/EF8300/EF8300.png) 6 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Paderborn | Kahler Asten | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![high](https://placehold.co/18x18/EF8300/EF8300.png) 6 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Recklinghausen | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Remscheid | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Rhein-Erft-Kreis | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Rhein-Kreis Neuss | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Rhein-Sieg-Kreis | Bonn | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Rheinisch-Bergischer Kreis | Bonn | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Siegen-Wittgenstein | Kahler Asten | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![high](https://placehold.co/18x18/EF8300/EF8300.png) 6 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Soest | Kahler Asten | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![high](https://placehold.co/18x18/EF8300/EF8300.png) 6 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Solingen | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Steinfurt | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Unna | Kahler Asten | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![high](https://placehold.co/18x18/EF8300/EF8300.png) 6 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 |
| Viersen | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Warendorf | Osnabrück | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 | ![moderate](https://placehold.co/18x18/FED300/FED300.png) 4 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Wesel | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
| Wuppertal | Düsseldorf | ![low](https://placehold.co/18x18/339C23/339C23.png) 1 | ![moderate](https://placehold.co/18x18/F7AF00/F7AF00.png) 5 | ![moderate](https://placehold.co/18x18/FFF200/FFF200.png) 3 |
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
