---
id: stock_growth_mobility_walking_biking
title: Growth of active travel (walking and cycling) operations
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
        Initialized to zero.
  - value: 0
    country: CA
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 913.53
    country: DE
    scalingType: CONSTANT
    validFrom: 2017-01-01
    comment: |
        nur Radverkehr
    reference: https://climateview.slab.com/public/piy3mcng
  - value: 0
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 3.88
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Nationellt cykelbokslut 2019, sid 8
    reference: https://trafikverket.diva-portal.org/smash/get/diva2:1452283/FULLTEXT01.pdf
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 0 | CA | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 913.53 | DE | CONSTANT | 2017-01-01 | nur Radverkehr | https://climateview.slab.com/public/piy3mcng |
| 0 | GB | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 3.88 | SE | CONSTANT | 2019-01-01 | Nationellt cykelbokslut 2019, sid 8 | https://trafikverket.diva-portal.org/smash/get/diva2:1452283/FULLTEXT01.pdf |


