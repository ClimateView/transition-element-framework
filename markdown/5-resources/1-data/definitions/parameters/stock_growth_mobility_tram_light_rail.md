---
id: stock_growth_mobility_tram_light_rail
title: Growth of tram and light rail operations
type: parameter
parameter_type: GROWTH_FACTOR
unit: vehicle_km_percapita
tags:
  - operations_growth
values:
  - value: 0
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 7.4515
    country: ES
    scalingType: CONSTANT
    validFrom: 2007-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/transporte-ferroviario-rail-transport-v6m8lcgr#hx8so-tram-light-rail-and-metro
  - value: 2.3623
    country: FR
    scalingType: CONSTANT
    validFrom: 2018-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/rail-transport-france-npr7q7rn#hqffq-tramway-train-leger-et-metro
  - value: 1.846558847
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Framräknat baserat på värden från TRAFA.
    reference: https://climateview.slab.com/public/posts/rz36acpx
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 7.4515 | ES | CONSTANT | 2007-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/transporte-ferroviario-rail-transport-v6m8lcgr#hx8so-tram-light-rail-and-metro |
| 2.3623 | FR | CONSTANT | 2018-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/rail-transport-france-npr7q7rn#hqffq-tramway-train-leger-et-metro |
| 1.846558847 | SE | CONSTANT | 2019-01-01 | Framräknat baserat på värden från TRAFA. | https://climateview.slab.com/public/posts/rz36acpx |


