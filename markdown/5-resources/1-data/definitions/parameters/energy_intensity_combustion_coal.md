---
id: energy_intensity_combustion_coal
title: Energy intensity combustion of coal
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_kwh
tags:
  - energy_intensity
  - PRIO_GLOBAL
values:
  - value: 1.25
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView -District heating
    reference: https://climateview.slab.com/public/yddbmggd
  - value: 1.25
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Daten aus Deutschland.
    reference: https://climateview.slab.com/public/amazedb1
  - value: 1.25
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzungen auf Grundlage von bundesdeutscher Statistik.
    reference: https://climateview.slab.com/public/amazedb1
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 1.25 | Global | CONSTANT | 2019-01-01 | Model description ClimateView -District heating | https://climateview.slab.com/public/yddbmggd |
| 1.25 | CH | CONSTANT | 2019-01-01 | Daten aus Deutschland. | https://climateview.slab.com/public/amazedb1 |
| 1.25 | DE | CONSTANT | 2019-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/amazedb1 |


