---
id: pm2_5_combustion_bus_lpg
title: pm2_5_combustion_bus_lpg
type: parameter
parameter_type: ECONOMIC_PARAMETER
unit: g_vkm
tags:
  - economic_parameter
values:
  - value: 0
    global: True
    scalingType: CONSTANT
    validFrom: 2023-01-01
    comment: |
        No global estimates for economic data
  - value: 0.03
    country: DE
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Preliminary economic data. Assumed same as gas bus.
    reference: https://docs.climateview.global/germany/transportation/economic-data/bus/
  - value: 0.03
    country: NL
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Based on German data. Assumed same as gas bus.
    reference: https://docs.climateview.global/germany/transportation/economic-data/bus/
  - value: 0.03
    country: ES
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Values based on European data. Assumed same as gas bus.
    reference: https://docs.climateview.global/germany/transportation/economic-data/bus/
  - value: 0.03
    country: GB
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Values based on European data. Assumed same as gas bus.
    reference: https://docs.climateview.global/germany/transportation/economic-data/bus/
  - value: 0
    country: SE
    scalingType: CONSTANT
    validFrom: 2023-01-01
    comment: |
        Preliminary values based on swedish data. Assumed same as gas bus.
    reference: https://docs.climateview.global/sweden/transportation/economic-data/elbuss/
  - value: 0
    country: US
    scalingType: CONSTANT
    validFrom: 2023-01-01
    comment: |
        Preliminary values based on US data. Assumed same as gas bus.
    reference: https://docs.climateview.global/us/transportation/economic-data/fossilbus/
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2023-01-01 | No global estimates for economic data |  |
| 0.03 | DE | CONSTANT | 2016-01-01 | Preliminary economic data. Assumed same as gas bus. | https://docs.climateview.global/germany/transportation/economic-data/bus/ |
| 0.03 | NL | CONSTANT | 2016-01-01 | Based on German data. Assumed same as gas bus. | https://docs.climateview.global/germany/transportation/economic-data/bus/ |
| 0.03 | ES | CONSTANT | 2016-01-01 | Values based on European data. Assumed same as gas bus. | https://docs.climateview.global/germany/transportation/economic-data/bus/ |
| 0.03 | GB | CONSTANT | 2016-01-01 | Values based on European data. Assumed same as gas bus. | https://docs.climateview.global/germany/transportation/economic-data/bus/ |
| 0 | SE | CONSTANT | 2023-01-01 | Preliminary values based on swedish data. Assumed same as gas bus. | https://docs.climateview.global/sweden/transportation/economic-data/elbuss/ |
| 0 | US | CONSTANT | 2023-01-01 | Preliminary values based on US data. Assumed same as gas bus. | https://docs.climateview.global/us/transportation/economic-data/fossilbus/ |


