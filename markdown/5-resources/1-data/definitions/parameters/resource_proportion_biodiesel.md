---
id: resource_proportion_biodiesel
title: Fuel proportion biodiesel for vehicles
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
  - value: 5
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzungen auf Grundlage von bundesdeutscher Statistik.
    reference: https://climateview.slab.com/public/dkkdj0hw
  - value: 4.4
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Model description - Biofuels
    reference: https://climateview.slab.com/public/tsku2vip
  - value: 27.7
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
| 0 | Global | CONSTANT | 2019-01-01 | Initialized to 0%. |  |
| 5 | DE | CONSTANT | 2019-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/dkkdj0hw |
| 4.4 | GB | CONSTANT | 2019-01-01 | ClimateView Model description - Biofuels | https://climateview.slab.com/public/tsku2vip |
| 27.7 | SE | CONSTANT | 2019-01-01 | ClimateView modellbeskrivning - biodrivmedel | https://climateview.slab.com/public/78b9qifq |


