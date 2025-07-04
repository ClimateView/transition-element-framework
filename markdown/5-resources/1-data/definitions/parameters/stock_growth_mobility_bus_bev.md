---
id: stock_growth_mobility_bus_bev
title: Growth of electric bus operations
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
  - value: 0
    country: CA
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Annahme 0 (Ausgangswert)
  - value: 0
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Annahme: null im Startjahr.
    reference: https://climateview.slab.com/public/piy3mcng
  - value: 1.155
    country: ES
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#h9fvg-buses
  - value: 0.4739
    country: FR
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/road-transport-france-eoxjg43o#hjygq-tableau-4-bus-et-cars
  - value: 0
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0.8741
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per invånare, beräknat på TRAFAs statistik för körsträckor 2019
    reference: https://climateview.slab.com/public/81gb14xu
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 0 | CA | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 0 | CH | CONSTANT | 2019-01-01 | Annahme 0 (Ausgangswert) |  |
| 0 | DE | CONSTANT | 2019-01-01 | Annahme: null im Startjahr. | https://climateview.slab.com/public/piy3mcng |
| 1.155 | ES | CONSTANT | 2020-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#h9fvg-buses |
| 0.4739 | FR | CONSTANT | 2021-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/road-transport-france-eoxjg43o#hjygq-tableau-4-bus-et-cars |
| 0 | GB | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 0.8741 | SE | CONSTANT | 2019-01-01 | Per invånare, beräknat på TRAFAs statistik för körsträckor 2019 | https://climateview.slab.com/public/81gb14xu |


