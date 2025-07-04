---
id: nox_emissions_propane_boiler_multi_family_buildings
title: NOx emissions (combustion, large scale propane boilers)
type: parameter
parameter_type: ECONOMIC_PARAMETER
unit: g_kwh
tags:
  - economic_parameter
values:
  - value: 0
    global: True
    scalingType: CONSTANT
    validFrom: 2022-01-01
    comment: |
        No global estimates for economic data.
  - value: 0.18
    country: US
    scalingType: CONSTANT
    validFrom: 2010-01-01
    comment: |
        Preliminary economic data based on US data
    reference: https://www.engineeringtoolbox.com/nox-emission-combustion-fuels-d_1086.html
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2022-01-01 | No global estimates for economic data. |  |
| 0.18 | US | CONSTANT | 2010-01-01 | Preliminary economic data based on US data | https://www.engineeringtoolbox.com/nox-emission-combustion-fuels-d_1086.html |


