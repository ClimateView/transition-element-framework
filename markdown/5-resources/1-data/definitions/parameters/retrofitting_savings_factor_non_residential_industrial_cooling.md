---
id: retrofitting_savings_factor_non_residential_industrial_cooling
title: Retrofitting savings factor for cooling in industrial buildings
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: percent
tags:
  - target_stretch
  - socioeconomic_parameter
values:
  - value: 70
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Assumed same potential as for heating.
    reference: https://climateview.slab.com/public/jpyhzloj
  - value: 30
    country: US
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Assumption.
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 70 | Global | CONSTANT | 2019-01-01 | Assumed same potential as for heating. | https://climateview.slab.com/public/jpyhzloj |
| 30 | US | CONSTANT | 2019-01-01 | Assumption. |  |


