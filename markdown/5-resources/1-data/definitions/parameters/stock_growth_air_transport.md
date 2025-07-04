---
id: stock_growth_air_transport
title: Growth air transport per new capita
type: parameter
parameter_type: GROWTH_FACTOR
unit: person_km_percapita
tags:
  - operations_growth
values:
  - value: 0
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Estimates for global air travel
    reference: https://climateview.slab.com/public/posts/h6wke7kr
  - value: 739.6148
    country: ES
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/transporte-aereo-air-transport-1nhvy53b#hsdsf-passenger-air-travel
  - value: 428.5008
    country: FR
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/air-transport-france-dt93wban
  - value: 0
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        För värden baserade på nationell statistik, se dokumentation.
    reference: https://research.chalmers.se/publication/508693/file/508693_Fulltext.pdf
  - value: 0
    country: US
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        For estimates based on national statistics, see documentation.
    reference: https://climateview.slab.com/posts/air-transportation-y7ajcmm0#hoyo0-table-2-domestic-air-travel
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2019-01-01 | Estimates for global air travel | https://climateview.slab.com/public/posts/h6wke7kr |
| 739.6148 | ES | CONSTANT | 2019-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/transporte-aereo-air-transport-1nhvy53b#hsdsf-passenger-air-travel |
| 428.5008 | FR | CONSTANT | 2019-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/air-transport-france-dt93wban |
| 0 | SE | CONSTANT | 2019-01-01 | För värden baserade på nationell statistik, se dokumentation. | https://research.chalmers.se/publication/508693/file/508693_Fulltext.pdf |
| 0 | US | CONSTANT | 2019-01-01 | For estimates based on national statistics, see documentation. | https://climateview.slab.com/posts/air-transportation-y7ajcmm0#hoyo0-table-2-domestic-air-travel |


