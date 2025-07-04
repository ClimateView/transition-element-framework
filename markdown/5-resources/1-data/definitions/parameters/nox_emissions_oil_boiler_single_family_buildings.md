---
id: nox_emissions_oil_boiler_single_family_buildings
title: NOx emissions (combustion, small scale oil boilers)
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
  - value: 0.11
    country: DE
    scalingType: CONSTANT
    validFrom: 2010-01-01
    comment: |
        Preliminary economic data.
    reference: https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs
  - value: 0.11
    country: NL
    scalingType: CONSTANT
    validFrom: 2010-01-01
    comment: |
        Based on German data.
    reference: https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs
  - value: 0.11
    country: ES
    scalingType: CONSTANT
    validFrom: 2010-01-01
    comment: |
        Preliminary economic data based on European data.
    reference: https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs
  - value: 0.11
    country: GB
    scalingType: CONSTANT
    validFrom: 2023-01-01
    comment: |
        Preliminary economic data based on European data
    reference: https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs
  - value: 0.11
    country: SE
    scalingType: CONSTANT
    validFrom: 2010-01-01
    comment: |
        Preliminary economic data.
    reference: https://docs.climateview.global/heating/economic-data/heating-economic-case/
  - value: 0.12
    country: US
    scalingType: CONSTANT
    validFrom: 2010-01-01
    comment: |
        Preliminary economic data based on US data
    reference: https://docs.climateview.global/us/stationary-energy/economic-data/heating/
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2022-01-01 | No global estimates for economic data. |  |
| 0.11 | DE | CONSTANT | 2010-01-01 | Preliminary economic data. | https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs |
| 0.11 | NL | CONSTANT | 2010-01-01 | Based on German data. | https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs |
| 0.11 | ES | CONSTANT | 2010-01-01 | Preliminary economic data based on European data. | https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs |
| 0.11 | GB | CONSTANT | 2023-01-01 | Preliminary economic data based on European data | https://climateview.slab.com/posts/economic-data-heating-beta-h37ihmvs |
| 0.11 | SE | CONSTANT | 2010-01-01 | Preliminary economic data. | https://docs.climateview.global/heating/economic-data/heating-economic-case/ |
| 0.12 | US | CONSTANT | 2010-01-01 | Preliminary economic data based on US data | https://docs.climateview.global/us/stationary-energy/economic-data/heating/ |


