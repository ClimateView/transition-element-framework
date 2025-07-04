---
id: pm2_5_wear_tear_bus_electric
title: PM 2.5 Particles emitted from wear and tear (electric buses)
type: parameter
parameter_type: ECONOMIC_PARAMETER
unit: g_vkm
tags:
  - economic_parameter
values:
  - value: 0
    global: True
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        No global estimates for economic data.
  - value: 0
    country: DE
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Preliminary economic data
    reference: https://docs.climateview.global/germany/transportation/economic-data/bus/
  - value: 0
    country: ES
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Values based on European data
    reference: https://docs.climateview.global/germany/transportation/economic-data/bus/
  - value: 0
    country: GB
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Values based on European data
    reference: https://docs.climateview.global/germany/transportation/economic-data/bus/
  - value: 0.0189
    country: SE
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        Assumption: half of the total particle emissions for buses from wear and tear.
    reference: https://docs.climateview.global/sweden/transportation/economic-data/elbuss/
  - value: 0.23
    country: US
    scalingType: CONSTANT
    validFrom: 2023-01-01
    comment: |
        Preliminary values based on US data
    reference: https://docs.climateview.global/us/transportation/economic-data/fossilbus/
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2021-01-01 | No global estimates for economic data. |  |
| 0 | DE | CONSTANT | 2016-01-01 | Preliminary economic data | https://docs.climateview.global/germany/transportation/economic-data/bus/ |
| 0 | ES | CONSTANT | 2016-01-01 | Values based on European data | https://docs.climateview.global/germany/transportation/economic-data/bus/ |
| 0 | GB | CONSTANT | 2016-01-01 | Values based on European data | https://docs.climateview.global/germany/transportation/economic-data/bus/ |
| 0.0189 | SE | CONSTANT | 2021-01-01 | Assumption: half of the total particle emissions for buses from wear and tear. | https://docs.climateview.global/sweden/transportation/economic-data/elbuss/ |
| 0.23 | US | CONSTANT | 2023-01-01 | Preliminary values based on US data | https://docs.climateview.global/us/transportation/economic-data/fossilbus/ |


