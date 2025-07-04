---
id: stock_freight_heavy_trucks_gas
title: Stock of heavy truck operation (CNG)
type: parameter
parameter_type: OPERATIONS
unit: tonne_km
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
    country: ES
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        For values based on national Spanish data, please see documentation.
    reference: https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#hjt6q-heavy-goods-vehicles-hg-vs
  - value: 54.7204
    country: FR
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/road-transport-france-eoxjg43o#hp6pa-tableau-6-transport-poids-lourds
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0 | ES | PER_CAPITA | 2019-01-01 | For values based on national Spanish data, please see documentation. | https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#hjt6q-heavy-goods-vehicles-hg-vs |
| 54.7204 | FR | PER_CAPITA | 2019-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/road-transport-france-eoxjg43o#hp6pa-tableau-6-transport-poids-lourds |


