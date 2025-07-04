---
id: retrofitting_savings_factor_residential_single_family
title: Retrofitting savings factor for single-family houses
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: percent
tags:
  - target_stretch
  - PRIO_MEDIUM
  - socioeconomic_parameter
values:
  - value: 70
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Retrofitting potential
    reference: https://climateview.slab.com/public/jpyhzloj
  - value: 40
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Stiftung Klimarappen, Schlussbericht Gebäudeprogramm
    reference: https://www.klimarappen.ch/resources/Schlussbericht_Gebaeudeprogramm.pdf#page=47
  - value: 33.5
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 70
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Retrofitting potential
    reference: https://climateview.slab.com/public/jpyhzloj
  - value: 70
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Energieffektiviseringspotential vid retrofitting
    reference: https://climateview.slab.com/public/c6jdlip2
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
| 70 | Global | CONSTANT | 2019-01-01 | Retrofitting potential | https://climateview.slab.com/public/jpyhzloj |
| 40 | CH | CONSTANT | 2019-01-01 | Stiftung Klimarappen, Schlussbericht Gebäudeprogramm | https://www.klimarappen.ch/resources/Schlussbericht_Gebaeudeprogramm.pdf#page=47 |
| 33.5 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 70 | GB | CONSTANT | 2019-01-01 | Retrofitting potential | https://climateview.slab.com/public/jpyhzloj |
| 70 | SE | CONSTANT | 2019-01-01 | Energieffektiviseringspotential vid retrofitting | https://climateview.slab.com/public/c6jdlip2 |
| 30 | US | CONSTANT | 2019-01-01 | Assumption. |  |


