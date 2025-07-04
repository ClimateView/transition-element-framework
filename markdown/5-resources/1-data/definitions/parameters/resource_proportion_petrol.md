---
id: resource_proportion_petrol
title: Fuel proportion petrol
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
  - value: 95.9
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Daten aus Deutschland.
    reference: https://climateview.slab.com/public/dkkdj0hw
  - value: 95.9
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzungen auf Grundlage von bundesdeutscher Statistik.
    reference: https://climateview.slab.com/public/dkkdj0hw
  - value: 96.8
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - fuels
    reference: https://climateview.slab.com/public/tsku2vip
  - value: 95.6
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
| 100 | Global | CONSTANT | 2019-01-01 | Initialized to 100%. |  |
| 95.9 | CH | CONSTANT | 2019-01-01 | Daten aus Deutschland. | https://climateview.slab.com/public/dkkdj0hw |
| 95.9 | DE | CONSTANT | 2019-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/dkkdj0hw |
| 96.8 | GB | CONSTANT | 2019-01-01 | Model description ClimateView - fuels | https://climateview.slab.com/public/tsku2vip |
| 95.6 | SE | CONSTANT | 2019-01-01 | Modellbeskrivning ClimateView drivmedel | https://climateview.slab.com/public/78b9qifq |


