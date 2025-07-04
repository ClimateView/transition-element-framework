---
id: stock_mobility_bus_bev
title: Stock of electric (BEV) bus operation
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
        Annahme 0 (Ausgangswert)
  - value: 0
    country: DE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Annahme: null im Startjahr.
    reference: https://climateview.slab.com/public/piy3mcng
  - value: 1.155
    country: ES
    scalingType: PER_CAPITA
    validFrom: 2020-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#h9fvg-buses
  - value: 0.4739
    country: FR
    scalingType: PER_CAPITA
    validFrom: 2021-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/road-transport-france-eoxjg43o#hjygq-tableau-4-bus-et-cars
  - value: 0
    country: GB
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0.8741
    country: SE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per invånare, beräknat på TRAFAs statistik för körsträckor 2019
    reference: https://climateview.slab.com/public/81gb14xu
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0 | CA | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0 | CH | PER_CAPITA | 2019-01-01 | Annahme 0 (Ausgangswert) |  |
| 0 | DE | PER_CAPITA | 2019-01-01 | Annahme: null im Startjahr. | https://climateview.slab.com/public/piy3mcng |
| 1.155 | ES | PER_CAPITA | 2020-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#h9fvg-buses |
| 0.4739 | FR | PER_CAPITA | 2021-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/road-transport-france-eoxjg43o#hjygq-tableau-4-bus-et-cars |
| 0 | GB | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0.8741 | SE | PER_CAPITA | 2019-01-01 | Per invånare, beräknat på TRAFAs statistik för körsträckor 2019 | https://climateview.slab.com/public/81gb14xu |


