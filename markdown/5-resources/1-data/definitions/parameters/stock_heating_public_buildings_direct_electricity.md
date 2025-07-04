---
id: stock_heating_public_buildings_direct_electricity
title: Stock direct electricity (non-residential, public)
type: parameter
parameter_type: OPERATIONS
unit: m2
tags:
  - operations
  - PRIO_HIGH
values:
  - value: 0.6745
    global: True
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 3.35
    country: CA
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada - Heating - Non-Residential
    reference: https://climateview.slab.com/public/posts/nbl9oykl
  - value: 6.3
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Quebec - Heating - Non-Residential
    reference: https://climateview.slab.com/public/posts/qqekk96z
  - value: 0
    country: CH
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 0.03
    country: DE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 0.9848
    country: ES
    scalingType: PER_CAPITA
    validFrom: 2017-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#h6k4z-institutional-space-heating
  - value: 1.822670088
    country: FR
    scalingType: PER_CAPITA
    validFrom: 2020-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-france-lvoxv5kr#hw5va-tableau-5-chauffage-des-locaux-des-batiments-publics
  - value: 0.6745
    country: GB
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 0.5605
    country: SE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från statistik från energimyndigheten och SCB.
    reference: https://climateview.slab.com/public/posts/dgkomg2d
  - value: 2.13
    country: US
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US national statistics.
    reference: https://climateview.slab.com/public/posts/l99gvehv
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.6745 | Global | PER_CAPITA | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 3.35 | CA | PER_CAPITA | 2019-01-01 | Model description ClimateView - Canada - Heating - Non-Residential | https://climateview.slab.com/public/posts/nbl9oykl |
| 6.3 | CA-QC | PER_CAPITA | 2019-01-01 | Model description ClimateView - Quebec - Heating - Non-Residential | https://climateview.slab.com/public/posts/qqekk96z |
| 0 | CH | PER_CAPITA | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 0.03 | DE | PER_CAPITA | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 0.9848 | ES | PER_CAPITA | 2017-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#h6k4z-institutional-space-heating |
| 1.822670088 | FR | PER_CAPITA | 2020-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/stationary-energy-non-residential-france-lvoxv5kr#hw5va-tableau-5-chauffage-des-locaux-des-batiments-publics |
| 0.6745 | GB | PER_CAPITA | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 0.5605 | SE | PER_CAPITA | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/posts/dgkomg2d |
| 2.13 | US | PER_CAPITA | 2019-01-01 | Value based on US national statistics. | https://climateview.slab.com/public/posts/l99gvehv |


