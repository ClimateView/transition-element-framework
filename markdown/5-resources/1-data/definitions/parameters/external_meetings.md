---
id: external_meetings
title: External meetings
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: meetings_day
tags:
  - cohorts
  - PRIO_LOW
  - socioeconomic_parameter
values:
  - value: 0.2
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView model description Remote Working
    reference: https://climateview.slab.com/public/vacos11z
  - value: 0.2
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung, basierend auf deutschen Daten.
    reference: https://climateview.slab.com/public/1uepz7y1
  - value: 0.2
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung
    reference: https://climateview.slab.com/public/1uepz7y1
  - value: 0.2
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
| 0.2 | Global | CONSTANT | 2019-01-01 | ClimateView model description Remote Working | https://climateview.slab.com/public/vacos11z |
| 0.2 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung, basierend auf deutschen Daten. | https://climateview.slab.com/public/1uepz7y1 |
| 0.2 | DE | CONSTANT | 2019-01-01 | Schätzung | https://climateview.slab.com/public/1uepz7y1 |
| 0.2 | FR | CONSTANT | 2019-01-01 | ClimateView model description Remote Working | https://climateview.slab.com/public/9305id09 |


