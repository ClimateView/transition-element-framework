---
id: energy_intensity_personal_vehicles_natural_gas
title: Energy intensity personal vehicle CNG
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_vehicle_km
tags:
  - energy_intensity
  - PRIO_LOW
values:
  - value: 0.857
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Energy used to move a vehicle 1 km ( average CNG car)
    reference: https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2020
  - value: 0.8601
    country: ES
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        Assumed 0.
    reference: https://climateview.slab.com/posts/road-transport-esqm8w27#hg9yu-table-7-personal-vehicles
  - value: 1.0662
    country: US
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Value based on US national statistics.
    reference: https://climateview.slab.com/posts/personal-transportation-wtgg2hlu#hzp8v-table-6-energy-intensities-personal-transport
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.857 | Global | CONSTANT | 2019-01-01 | Energy used to move a vehicle 1 km ( average CNG car) | https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2020 |
| 0.8601 | ES | CONSTANT | 2021-01-01 | Assumed 0. | https://climateview.slab.com/posts/road-transport-esqm8w27#hg9yu-table-7-personal-vehicles |
| 1.0662 | US | CONSTANT | 2019-01-01 | Value based on US national statistics. | https://climateview.slab.com/posts/personal-transportation-wtgg2hlu#hzp8v-table-6-energy-intensities-personal-transport |


