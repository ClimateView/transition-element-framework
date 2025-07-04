---
id: energy_intensity_mobility_railway
title: Energy intensity railway
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_person_km
tags:
  - energy_intensity
  - PRIO_MEDIUM
values:
  - value: 0.145666
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Energy intensity for mixed electrified and non-electrified railway.
    reference: https://climateview.slab.com/public/qpohg68o
  - value: 0.42
    country: CA
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada -  Personal Transportation
    reference: https://climateview.slab.com/public/posts/ird2eslu
  - value: 0.0543
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Energy intensity for electric railway, based on Swedish statistics.
    reference: https://climateview.slab.com/public/rz36acpx
  - value: 0.0543
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Baserat på statistik från TRAFA.
    reference: https://climateview.slab.com/public/rz36acpx
  - value: 0.1692
    country: US
    scalingType: CONSTANT
    validFrom: 2013-01-01
    comment: |
        Value based on US national statistics.
    reference: https://climateview.slab.com/posts/rail-transportation-vov14r6c#h7xsh-table-4-energy-intensities-passenger-rail
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.145666 | Global | CONSTANT | 2019-01-01 | Energy intensity for mixed electrified and non-electrified railway. | https://climateview.slab.com/public/qpohg68o |
| 0.42 | CA | CONSTANT | 2019-01-01 | Model description ClimateView - Canada -  Personal Transportation | https://climateview.slab.com/public/posts/ird2eslu |
| 0.0543 | CH | CONSTANT | 2019-01-01 | Energy intensity for electric railway, based on Swedish statistics. | https://climateview.slab.com/public/rz36acpx |
| 0.0543 | SE | CONSTANT | 2019-01-01 | Baserat på statistik från TRAFA. | https://climateview.slab.com/public/rz36acpx |
| 0.1692 | US | CONSTANT | 2013-01-01 | Value based on US national statistics. | https://climateview.slab.com/posts/rail-transportation-vov14r6c#h7xsh-table-4-energy-intensities-passenger-rail |


