---
id: stock_growth_heating_industrial_district_heating
title: Growth heating by district heating (industrial), per capita
type: parameter
parameter_type: GROWTH_FACTOR
unit: m2_percapita
tags:
  - operations_growth
values:
  - value: 0.0601
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 0
    country: CA
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 1.41
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von Schweizer Städten
  - value: 0.74
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 0
    country: ES
    scalingType: CONSTANT
    validFrom: 2017-01-01
    comment: |
        Initialized to zero.
  - value: 0.0601
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 6.0046
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
| 0.0601 | Global | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 0 | CA | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 1.41 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von Schweizer Städten |  |
| 0.74 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 0 | ES | CONSTANT | 2017-01-01 | Initialized to zero. |  |
| 0.0601 | GB | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 6.0046 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/posts/dgkomg2d |


