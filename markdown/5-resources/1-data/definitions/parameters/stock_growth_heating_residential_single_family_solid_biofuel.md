---
id: stock_growth_heating_residential_single_family_solid_biofuel
title: Growth heating by solid biofuel (single-family), per capita
type: parameter
parameter_type: GROWTH_FACTOR
unit: m2_percapita
tags:
  - operations_growth
values:
  - value: 0
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0.11
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von Schweizer Städten
  - value: 0.88
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 10.4044
    country: ES
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating
  - value: 2.0661
    country: FR
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hzc28-tableau-4-chauffage-des-maisons-individuelles-5
  - value: 3.5447
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från statistik från energimyndigheten och SCB.
    reference: https://climateview.slab.com/public/uui9yijv
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 0.11 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von Schweizer Städten |  |
| 0.88 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 10.4044 | ES | CONSTANT | 2020-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating |
| 2.0661 | FR | CONSTANT | 2016-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hzc28-tableau-4-chauffage-des-maisons-individuelles-5 |
| 3.5447 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/uui9yijv |


