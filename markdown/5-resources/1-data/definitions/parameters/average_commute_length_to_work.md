---
id: average_commute_length_to_work
title: Average commute length to work (round-trip)
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: km_commute
tags:
  - atoc
  - PRIO_MEDIUM
  - socioeconomic_parameter
values:
  - value: 30
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView -Transportation
    reference: https://climateview.slab.com/public/ranizl8z
  - value: 17.4
    country: CA
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada -  Personal Transportation
    reference: https://climateview.slab.com/public/ird2eslu
  - value: 30000
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Durchschnitt Schweiz
    reference: https://www.bfs.admin.ch/bfs/de/home/statistiken/mobilitaet-verkehr/personenverkehr/pendlermobilitaet.html
  - value: 23.5
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Durchschnitt Mannheim (25.1) und Kiel (22.2)
    reference: https://climateview.slab.com/public/z1katuv7
  - value: 20
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        RVU Sverige 2015-2016
    reference: https://www.trafa.se/kommunikationsvanor/RVU-Sverige/
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 30 | Global | CONSTANT | 2019-01-01 | Model description ClimateView -Transportation | https://climateview.slab.com/public/ranizl8z |
| 17.4 | CA | CONSTANT | 2019-01-01 | Model description ClimateView - Canada -  Personal Transportation | https://climateview.slab.com/public/ird2eslu |
| 30000 | CH | CONSTANT | 2019-01-01 | Durchschnitt Schweiz | https://www.bfs.admin.ch/bfs/de/home/statistiken/mobilitaet-verkehr/personenverkehr/pendlermobilitaet.html |
| 23.5 | DE | CONSTANT | 2019-01-01 | Durchschnitt Mannheim (25.1) und Kiel (22.2) | https://climateview.slab.com/public/z1katuv7 |
| 20 | SE | CONSTANT | 2019-01-01 | RVU Sverige 2015-2016 | https://www.trafa.se/kommunikationsvanor/RVU-Sverige/ |


