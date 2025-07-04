---
id: non_residential_heating_energy_intensity_savings_factor
title: Energy efficiency savings factor for non-residential buildings
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: percent
tags:
  - target_stretch
  - PRIO_LOW
  - socioeconomic_parameter
values:
  - value: 63
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView model description -buildings
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 33.5
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Daten aus Deutschland.
    reference: https://climateview.slab.com/public/wvziauke
  - value: 33.5
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 63
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView model description -buildings
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 67
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Modelbeskrivning ClimateView - Övriga lokaler
    reference: https://climateview.slab.com/public/x7khi1nl
  - value: 30
    country: US
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Assumption.
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 63 | Global | CONSTANT | 2019-01-01 | ClimateView model description -buildings | https://climateview.slab.com/public/zy17l63p |
| 33.5 | CH | CONSTANT | 2019-01-01 | Daten aus Deutschland. | https://climateview.slab.com/public/wvziauke |
| 33.5 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 63 | GB | CONSTANT | 2019-01-01 | ClimateView model description -buildings | https://climateview.slab.com/public/zy17l63p |
| 67 | SE | CONSTANT | 2019-01-01 | Modelbeskrivning ClimateView - Övriga lokaler | https://climateview.slab.com/public/x7khi1nl |
| 30 | US | CONSTANT | 2019-01-01 | Assumption. |  |


