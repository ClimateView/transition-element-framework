---
id: stock_growth_heating_public_buildings_oil
title: Growth heating by oil (public), per capita
type: parameter
parameter_type: GROWTH_FACTOR
unit: m2_percapita
tags:
  - operations_growth
values:
  - value: 0.2068
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 0.01
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 0.27
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 2.3926
    country: ES
    scalingType: CONSTANT
    validFrom: 2017-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#h6k4z-institutional-space-heating
  - value: 0.9427603905
    country: FR
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-france-lvoxv5kr#hw5va-tableau-5-chauffage-des-locaux-des-batiments-publics
  - value: 0.0146
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
| 0.2068 | Global | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 0.01 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 0.27 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 2.3926 | ES | CONSTANT | 2017-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#h6k4z-institutional-space-heating |
| 0.9427603905 | FR | CONSTANT | 2020-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/stationary-energy-non-residential-france-lvoxv5kr#hw5va-tableau-5-chauffage-des-locaux-des-batiments-publics |
| 0.0146 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/posts/dgkomg2d |


