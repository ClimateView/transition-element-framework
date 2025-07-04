---
id: stock_heating_industrial_heat_pumps
title: Stock heatpumps (non-residential, industrial)
type: parameter
parameter_type: OPERATIONS
unit: m2
tags:
  - operations
  - PRIO_MEDIUM
values:
  - value: 0
    global: True
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0
    country: CA
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0
    country: CH
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 0.14
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
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#hvhq4-industrial-floor-area-and-space-heating
  - value: 0
    country: GB
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0.2087
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
| 0 | Global | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0 | CA | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0 | CH | PER_CAPITA | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 0.14 | DE | PER_CAPITA | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 0 | ES | PER_CAPITA | 2017-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#hvhq4-industrial-floor-area-and-space-heating |
| 0 | GB | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0.2087 | SE | PER_CAPITA | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/posts/dgkomg2d |


