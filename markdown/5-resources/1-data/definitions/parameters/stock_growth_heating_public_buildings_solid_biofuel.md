---
id: stock_growth_heating_public_buildings_solid_biofuel
title: Growth heating by solid biofuel (public buildings), per capita
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
  - value: 0.04
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 0.0409
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
| 0 | Global | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 0.04 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 0.0409 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/posts/dgkomg2d |


