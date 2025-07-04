---
id: resource_proportion_ethanol
title: Fuel proportion ethanol
type: parameter
parameter_type: RESOURCE_PROPORTION
unit: percent
tags:
  - resource_proportion
  - PRIO_MEDIUM
values:
  - value: 0
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to 0%.
  - value: 4.1
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Daten aus Deutschland.
    reference: https://climateview.slab.com/public/dkkdj0hw
  - value: 4.1
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzungen auf Grundlage von bundesdeutscher Statistik.
    reference: https://climateview.slab.com/public/dkkdj0hw
  - value: 3.2
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - fuels
    reference: https://climateview.slab.com/public/tsku2vip
  - value: 4.4
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Modellbeskrivning ClimateView drivmedel
    reference: https://climateview.slab.com/public/78b9qifq
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2019-01-01 | Initialized to 0%. |  |
| 4.1 | CH | CONSTANT | 2019-01-01 | Daten aus Deutschland. | https://climateview.slab.com/public/dkkdj0hw |
| 4.1 | DE | CONSTANT | 2019-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/dkkdj0hw |
| 3.2 | GB | CONSTANT | 2019-01-01 | Model description ClimateView - fuels | https://climateview.slab.com/public/tsku2vip |
| 4.4 | SE | CONSTANT | 2019-01-01 | Modellbeskrivning ClimateView drivmedel | https://climateview.slab.com/public/78b9qifq |


