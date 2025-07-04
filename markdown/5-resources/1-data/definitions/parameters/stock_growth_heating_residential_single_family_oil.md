---
id: stock_growth_heating_residential_single_family_oil
title: Growth heating by oil (single-family), per capita
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
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 1.37
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 5.59
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 5.6775
    country: ES
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating
  - value: 5.1745
    country: FR
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hzc28-tableau-4-chauffage-des-maisons-individuelles-5
  - value: 0.2349
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
| 0 | Global | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/zy17l63p |
| 1.37 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 5.59 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 5.6775 | ES | CONSTANT | 2020-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating |
| 5.1745 | FR | CONSTANT | 2016-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hzc28-tableau-4-chauffage-des-maisons-individuelles-5 |
| 0.2349 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/uui9yijv |


