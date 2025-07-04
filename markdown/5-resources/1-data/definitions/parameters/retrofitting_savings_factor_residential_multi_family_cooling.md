---
id: retrofitting_savings_factor_residential_multi_family_cooling
title: Retrofitting savings factor for cooling in residential buildings
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: percent
tags:
  - target_stretch
  - socioeconomic_parameter
values:
  - value: 25
    global: True
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Estimate based on US data.
    reference: https://docs.climateview.global/us/stationary-energy/physical-data/ac/
  - value: 25
    country: US
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Value based on US national and international numbers.
    reference: https://docs.climateview.global/us/stationary-energy/physical-data/ac/
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 25 | Global | CONSTANT | 2020-01-01 | Estimate based on US data. | https://docs.climateview.global/us/stationary-energy/physical-data/ac/ |
| 25 | US | CONSTANT | 2020-01-01 | Value based on US national and international numbers. | https://docs.climateview.global/us/stationary-energy/physical-data/ac/ |


