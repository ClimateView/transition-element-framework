---
id: energy_intensity_heating_non_residential_industrial_biofuel
title: Energy intensity biofuel industrial
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_m2
tags:
  - energy_intensity
  - PRIO_HIGH
values:
  - value: 165
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Assuming same as for residential buildings
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 83
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Bundesamt für Energie, BFE
    reference: https://pubdb.bfe.admin.ch/de/publication/download/9498
  - value: 305.2
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Durchschnitt Deutschland
    reference: https://climateview.slab.com/public/wvziauke
  - value: 165
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Assuming same as for residential buildings
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 129
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimatView modellbeskrivning - Energikonsumtion bostäder och lokaler
    reference: https://climateview.slab.com/public/x7khi1nl
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 165 | Global | CONSTANT | 2019-01-01 | Assuming same as for residential buildings | https://climateview.slab.com/public/zy17l63p |
| 83 | CH | CONSTANT | 2019-01-01 | Bundesamt für Energie, BFE | https://pubdb.bfe.admin.ch/de/publication/download/9498 |
| 305.2 | DE | CONSTANT | 2019-01-01 | Durchschnitt Deutschland | https://climateview.slab.com/public/wvziauke |
| 165 | GB | CONSTANT | 2019-01-01 | Assuming same as for residential buildings | https://climateview.slab.com/public/zy17l63p |
| 129 | SE | CONSTANT | 2019-01-01 | ClimatView modellbeskrivning - Energikonsumtion bostäder och lokaler | https://climateview.slab.com/public/x7khi1nl |


