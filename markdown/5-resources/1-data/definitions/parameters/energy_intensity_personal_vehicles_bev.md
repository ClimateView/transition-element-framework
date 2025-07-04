---
id: energy_intensity_personal_vehicles_bev
title: Energy intensity personal BEV
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_vehicle_km
tags:
  - energy_intensity
  - PRIO_HIGH
values:
  - value: 0.2262
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Energy used to move a vehicle 1 km ( average BEV car)
    reference: https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2020
  - value: 0.202
    country: ES
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        Calculations based on European data.
    reference: https://climateview.slab.com/posts/road-transport-esqm8w27#hg9yu-table-7-personal-vehicles
  - value: 0.202
    country: US
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Value based on currently available BEV models on the market.
    reference: https://climateview.slab.com/posts/personal-transportation-wtgg2hlu#hzp8v-table-6-energy-intensities-personal-transport
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.2262 | Global | CONSTANT | 2019-01-01 | Energy used to move a vehicle 1 km ( average BEV car) | https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2020 |
| 0.202 | ES | CONSTANT | 2021-01-01 | Calculations based on European data. | https://climateview.slab.com/posts/road-transport-esqm8w27#hg9yu-table-7-personal-vehicles |
| 0.202 | US | CONSTANT | 2019-01-01 | Value based on currently available BEV models on the market. | https://climateview.slab.com/posts/personal-transportation-wtgg2hlu#hzp8v-table-6-energy-intensities-personal-transport |


