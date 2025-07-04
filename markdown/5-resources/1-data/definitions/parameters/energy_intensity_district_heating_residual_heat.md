---
id: energy_intensity_district_heating_residual_heat
title: Energy intensity district heating residual heat
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_kwh
tags:
  - energy_intensity
  - PRIO_LOW
values:
  - value: 1
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView -District heating
    reference: https://climateview.slab.com/public/yddbmggd
  - value: 1
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Daten aus Deutschland.
    reference: https://climateview.slab.com/public/amazedb1
  - value: 1
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
| 1 | Global | CONSTANT | 2019-01-01 | Model description ClimateView -District heating | https://climateview.slab.com/public/yddbmggd |
| 1 | CH | CONSTANT | 2019-01-01 | Daten aus Deutschland. | https://climateview.slab.com/public/amazedb1 |
| 1 | DE | CONSTANT | 2019-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/amazedb1 |


