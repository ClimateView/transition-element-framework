---
id: resource_proportion_diesel_light_trucks
title: Fuel proportion of diesel for light trucks
type: parameter
parameter_type: RESOURCE_PROPORTION
unit: percent
tags:
  - resource_proportion
  - PRIO_MEDIUM
values:
  - value: 100
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to 100%.
  - value: 95
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzungen, basierend auf deutschen Daten.
    reference: https://climateview.slab.com/public/dkkdj0hw
  - value: 95
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzungen auf Grundlage von bundesdeutscher Statistik.
    reference: https://climateview.slab.com/public/dkkdj0hw
  - value: 72.3
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView modellbeskrivning - biodrivmedel
    reference: https://climateview.slab.com/public/78b9qifq
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 100 | Global | CONSTANT | 2019-01-01 | Initialized to 100%. |  |
| 95 | CH | CONSTANT | 2019-01-01 | Schätzungen, basierend auf deutschen Daten. | https://climateview.slab.com/public/dkkdj0hw |
| 95 | DE | CONSTANT | 2019-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/dkkdj0hw |
| 72.3 | SE | CONSTANT | 2019-01-01 | ClimateView modellbeskrivning - biodrivmedel | https://climateview.slab.com/public/78b9qifq |


