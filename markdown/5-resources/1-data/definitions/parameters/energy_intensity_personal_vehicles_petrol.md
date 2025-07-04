---
id: energy_intensity_personal_vehicles_petrol
title: Energy intensity petrol ICE
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_vehicle_km
tags:
  - energy_intensity
  - PRIO_HIGH
values:
  - value: 0.7228
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Energy used to move a vehicle 1 km (average petrol car)
    reference: https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2020
  - value: 0.82
    country: CA
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada - Personal Transportation
    reference: https://climateview.slab.com/public/posts/ird2eslu
  - value: 0.7212
    country: ES
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        Calculations based on European data.
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
| 0.7228 | Global | CONSTANT | 2019-01-01 | Energy used to move a vehicle 1 km (average petrol car) | https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2020 |
| 0.82 | CA | CONSTANT | 2019-01-01 | Model description ClimateView - Canada - Personal Transportation | https://climateview.slab.com/public/posts/ird2eslu |
| 0.7212 | ES | CONSTANT | 2021-01-01 | Calculations based on European data. | https://climateview.slab.com/posts/road-transport-esqm8w27#hg9yu-table-7-personal-vehicles |
| 1.0662 | US | CONSTANT | 2019-01-01 | Value based on US national statistics. | https://climateview.slab.com/posts/personal-transportation-wtgg2hlu#hzp8v-table-6-energy-intensities-personal-transport |


