---
id: stock_growth_heating_residential_multi_family_gas
title: Growth heating by gas (multi-family), per capita
type: parameter
parameter_type: GROWTH_FACTOR
unit: m2_percapita
tags:
  - operations_growth
values:
  - value: 4
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 9.53
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 12.33
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 15.2397
    country: ES
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating
  - value: 6.2039
    country: FR
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hvdfv-tableau-3-chauffage-des-appartements-5
  - value: 0.2065
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
| 4 | Global | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/zy17l63p |
| 9.53 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 12.33 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 15.2397 | ES | CONSTANT | 2020-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating |
| 6.2039 | FR | CONSTANT | 2016-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hvdfv-tableau-3-chauffage-des-appartements-5 |
| 0.2065 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/uui9yijv |


