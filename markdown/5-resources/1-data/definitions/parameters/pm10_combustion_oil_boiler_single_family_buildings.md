---
id: pm10_combustion_oil_boiler_single_family_buildings
title: PM 10 Particles emitted from combustion (small scale oil boilers)
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
  - value: 0.00612
    country: DE
    scalingType: CONSTANT
    validFrom: 2005-01-01
    comment: |
        Preliminary economic data.
    reference: https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs
  - value: 0.00612
    country: NL
    scalingType: CONSTANT
    validFrom: 2005-01-01
    comment: |
        Based on German data.
    reference: https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs
  - value: 0.00612
    country: ES
    scalingType: CONSTANT
    validFrom: 2005-01-01
    comment: |
        Preliminary economic data based on European data.
    reference: https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs
  - value: 0.00612
    country: GB
    scalingType: CONSTANT
    validFrom: 2023-01-01
    comment: |
        Preliminary economic data based on European data
    reference: https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs
  - value: 0.00612
    country: SE
    scalingType: CONSTANT
    validFrom: 2005-01-01
    comment: |
        Preliminary economic data.
    reference: https://docs.climateview.global/heating/economic-data/heating-economic-case/
  - value: 0.022
    country: US
    scalingType: CONSTANT
    validFrom: 2003-01-01
    comment: |
        Preliminary economic data based on US data
    reference: https://docs.climateview.global/us/stationary-energy/economic-data/heating/
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2022-01-01 | No global estimates for economic data. |  |
| 0.00612 | DE | CONSTANT | 2005-01-01 | Preliminary economic data. | https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs |
| 0.00612 | NL | CONSTANT | 2005-01-01 | Based on German data. | https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs |
| 0.00612 | ES | CONSTANT | 2005-01-01 | Preliminary economic data based on European data. | https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs |
| 0.00612 | GB | CONSTANT | 2023-01-01 | Preliminary economic data based on European data | https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs |
| 0.00612 | SE | CONSTANT | 2005-01-01 | Preliminary economic data. | https://docs.climateview.global/heating/economic-data/heating-economic-case/ |
| 0.022 | US | CONSTANT | 2003-01-01 | Preliminary economic data based on US data | https://docs.climateview.global/us/stationary-energy/economic-data/heating/ |


