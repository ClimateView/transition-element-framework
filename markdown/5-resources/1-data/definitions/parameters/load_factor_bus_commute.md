---
id: load_factor_bus_commute
title: Commute load factor for bus
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: persons
tags:
  - atoc
  - PRIO_MEDIUM
  - socioeconomic_parameter
values:
  - value: 12
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK national statistics methodology paper p. 60
    reference: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/901692/conversion-factors-2020-methodology.pdf
  - value: 16
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Daten aus Deutschland.
    reference: https://climateview.slab.com/public/z1katuv7
  - value: 16
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Städtische Verkehrsbetriebe?
    reference: https://climateview.slab.com/public/z1katuv7
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 12 | Global | CONSTANT | 2019-01-01 | UK national statistics methodology paper p. 60 | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/901692/conversion-factors-2020-methodology.pdf |
| 16 | CH | CONSTANT | 2019-01-01 | Daten aus Deutschland. | https://climateview.slab.com/public/z1katuv7 |
| 16 | DE | CONSTANT | 2019-01-01 | Städtische Verkehrsbetriebe? | https://climateview.slab.com/public/z1katuv7 |


