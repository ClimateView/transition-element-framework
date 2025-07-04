---
id: energy_intensity_walking_biking
title: Energy intensity walking/biking
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_person_km
tags:
  - energy_intensity
  - PRIO_GLOBAL
values:
  - value: 0.0001
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0.0001
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung, ohne e-bikes
  - value: 0.0001
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Är satt till noll
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.0001 | Global | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 0.0001 | DE | CONSTANT | 2019-01-01 | Schätzung, ohne e-bikes |  |
| 0.0001 | SE | CONSTANT | 2019-01-01 | Är satt till noll |  |


