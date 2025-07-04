---
id: energy_intensity_district_heating_heatpumps
title: Energy intensity district heating heatpumps
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_kwh
tags:
  - energy_intensity
  - PRIO_LOW
values:
  - value: 0.333
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView -District heating
    reference: https://climateview.slab.com/public/yddbmggd
  - value: 0.333
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Daten aus Deutschland.
    reference: https://climateview.slab.com/public/amazedb1
  - value: 0.333
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
| 0.333 | Global | CONSTANT | 2019-01-01 | Model description ClimateView -District heating | https://climateview.slab.com/public/yddbmggd |
| 0.333 | CH | CONSTANT | 2019-01-01 | Daten aus Deutschland. | https://climateview.slab.com/public/amazedb1 |
| 0.333 | DE | CONSTANT | 2019-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/amazedb1 |


