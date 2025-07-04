---
id: energy_from_waste_conversion
title: Energy from waste conversion factor (calorific content)
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: kwh_tonne
tags:
  - atoc
  - PRIO_MEDIUM
  - socioeconomic_parameter
values:
  - value: 600
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Wikipedia: approx. average from waste-to-energy-plant
    reference: https://en.wikipedia.org/wiki/Waste-to-energy_plant
  - value: 3000
    country: SE
    scalingType: CONSTANT
    validFrom: 2022-01-01
    comment: |
        Värde från Avfall Sverige.
    reference: https://www.avfallsverige.se/fakta-statistik/avfallsbehandling/energiatervinning
  - value: 3231
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
| 600 | Global | CONSTANT | 2019-01-01 | Wikipedia: approx. average from waste-to-energy-plant | https://en.wikipedia.org/wiki/Waste-to-energy_plant |
| 3000 | SE | CONSTANT | 2022-01-01 | Värde från Avfall Sverige. | https://www.avfallsverige.se/fakta-statistik/avfallsbehandling/energiatervinning |
| 3231 | US | CONSTANT | 2019-01-01 | Assumption. |  |


