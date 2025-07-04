---
id: proportion_working
title: Proportion of active workers
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: percent
tags:
  - cohorts
  - PRIO_MEDIUM
  - socioeconomic_parameter
values:
  - value: 50
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView model description Remote Working
    reference: https://climateview.slab.com/public/vacos11z
  - value: 95
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Daten aus Basel 2018
    reference: https://climateview.slab.com/public/2u2f4bsl
  - value: 54
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Sozialversicherungspflichtig Beschäftigte am Arbeitsort
    reference: https://climateview.slab.com/public/1uepz7y1
  - value: 40
    country: FR
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView model description Remote Working
    reference: https://climateview.slab.com/public/9305id09
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 50 | Global | CONSTANT | 2019-01-01 | ClimateView model description Remote Working | https://climateview.slab.com/public/vacos11z |
| 95 | CH | CONSTANT | 2019-01-01 | Daten aus Basel 2018 | https://climateview.slab.com/public/2u2f4bsl |
| 54 | DE | CONSTANT | 2019-01-01 | Sozialversicherungspflichtig Beschäftigte am Arbeitsort | https://climateview.slab.com/public/1uepz7y1 |
| 40 | FR | CONSTANT | 2019-01-01 | ClimateView model description Remote Working | https://climateview.slab.com/public/9305id09 |


