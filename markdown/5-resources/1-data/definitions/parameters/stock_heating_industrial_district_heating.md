---
id: stock_heating_industrial_district_heating
title: Stock district heating (non-residential, industrial)
type: parameter
parameter_type: OPERATIONS
unit: m2
tags:
  - operations
  - PRIO_MEDIUM
values:
  - value: 0.0601
    global: True
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 0
    country: CA
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 1.41
    country: CH
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 0.74
    country: DE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 0
    country: ES
    scalingType: PER_CAPITA
    validFrom: 2017-01-01
    comment: |
        Initialized to zero.
  - value: 0.0601
    country: GB
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 6.0046
    country: SE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från statistik från energimyndigheten och SCB.
    reference: https://climateview.slab.com/public/posts/dgkomg2d
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.0601 | Global | PER_CAPITA | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 0 | CA | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 1.41 | CH | PER_CAPITA | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 0.74 | DE | PER_CAPITA | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 0 | ES | PER_CAPITA | 2017-01-01 | Initialized to zero. |  |
| 0.0601 | GB | PER_CAPITA | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 6.0046 | SE | PER_CAPITA | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/posts/dgkomg2d |


