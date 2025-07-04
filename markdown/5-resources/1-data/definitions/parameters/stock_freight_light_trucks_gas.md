---
id: stock_freight_light_trucks_gas
title: Stock of light truck operation (CNG)
type: parameter
parameter_type: OPERATIONS
unit: vehicle_km
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
    validFrom: 2020-01-01
    comment: |
        For values based on national Spanish data, please see documentation.
    reference: https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#hfvae-light-goods-vehicles-lg-vs
  - value: 3.4531
    country: FR
    scalingType: PER_CAPITA
    validFrom: 2021-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/road-transport-france-eoxjg43o#hmetp-tableau-5-vehicules-utilitaires-legers-vu-ls
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0 | ES | PER_CAPITA | 2020-01-01 | For values based on national Spanish data, please see documentation. | https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#hfvae-light-goods-vehicles-lg-vs |
| 3.4531 | FR | PER_CAPITA | 2021-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/road-transport-france-eoxjg43o#hmetp-tableau-5-vehicules-utilitaires-legers-vu-ls |


