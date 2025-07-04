---
id: stock_growth_heating_public_buildings_direct_electricity
title: Growth heating by direct electricity (public), per capita
type: parameter
parameter_type: GROWTH_FACTOR
unit: m2_percapita
tags:
  - operations_growth
values:
  - value: 0.6745
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 0
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 0.03
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 0.9848
    country: ES
    scalingType: CONSTANT
    validFrom: 2017-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#h6k4z-institutional-space-heating
  - value: 1.822670088
    country: FR
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-france-lvoxv5kr#hw5va-tableau-5-chauffage-des-locaux-des-batiments-publics
  - value: 0.5605
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från statistik från energimyndigheten och SCB.
    reference: https://climateview.slab.com/public/posts/dgkomg2d
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.6745 | Global | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 0 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 0.03 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 0.9848 | ES | CONSTANT | 2017-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#h6k4z-institutional-space-heating |
| 1.822670088 | FR | CONSTANT | 2020-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/stationary-energy-non-residential-france-lvoxv5kr#hw5va-tableau-5-chauffage-des-locaux-des-batiments-publics |
| 0.5605 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/posts/dgkomg2d |


