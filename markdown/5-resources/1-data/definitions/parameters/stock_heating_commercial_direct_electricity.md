---
id: stock_heating_commercial_direct_electricity
title: Stock direct electricity (non-residential, commercial)
type: parameter
parameter_type: OPERATIONS
unit: m2
tags:
  - operations
  - PRIO_HIGH
values:
  - value: 0.6745
    global: True
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 3.35
    country: CA
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada - Heating - Non-Residential
    reference: https://climateview.slab.com/public/posts/nbl9oykl
  - value: 6.3
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Quebec - Heating - Non-Residential
    reference: https://climateview.slab.com/public/posts/qqekk96z
  - value: 0
    country: CH
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 0.42
    country: DE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 3.8617
    country: ES
    scalingType: PER_CAPITA
    validFrom: 2017-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#h8e8m-commercial-space-heating
  - value: 2.380497944
    country: FR
    scalingType: PER_CAPITA
    validFrom: 2020-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-france-lvoxv5kr#hyhlj-tableau-4-chauffage-des-locaux-pour-le-secteur-commercial-et-tertiaire
  - value: 0.6745
    country: GB
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 0.4671
    country: SE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från statistik från energimyndigheten och SCB.
    reference: https://climateview.slab.com/public/posts/dgkomg2d
  - value: 5.74
    country: US
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US national statistics.
    reference: https://climateview.slab.com/public/posts/l99gvehv
  - value: 7.98
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/isr8bsbe
  - value: 12.83
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/6xxnzvjq
  - value: 4.17
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/iqe8m8wy
  - value: 12.83
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/6xxnzvjq
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.6745 | Global | PER_CAPITA | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 3.35 | CA | PER_CAPITA | 2019-01-01 | Model description ClimateView - Canada - Heating - Non-Residential | https://climateview.slab.com/public/posts/nbl9oykl |
| 6.3 | CA-QC | PER_CAPITA | 2019-01-01 | Model description ClimateView - Quebec - Heating - Non-Residential | https://climateview.slab.com/public/posts/qqekk96z |
| 0 | CH | PER_CAPITA | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 0.42 | DE | PER_CAPITA | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 3.8617 | ES | PER_CAPITA | 2017-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#h8e8m-commercial-space-heating |
| 2.380497944 | FR | PER_CAPITA | 2020-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/stationary-energy-non-residential-france-lvoxv5kr#hyhlj-tableau-4-chauffage-des-locaux-pour-le-secteur-commercial-et-tertiaire |
| 0.6745 | GB | PER_CAPITA | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 0.4671 | SE | PER_CAPITA | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/posts/dgkomg2d |
| 5.74 | US | PER_CAPITA | 2019-01-01 | Value based on US national statistics. | https://climateview.slab.com/public/posts/l99gvehv |
| 7.98 | US-CA | PER_CAPITA | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/isr8bsbe |
| 12.83 | US-FL | PER_CAPITA | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/6xxnzvjq |
| 4.17 | US-IN | PER_CAPITA | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/iqe8m8wy |
| 12.83 | US-VA | PER_CAPITA | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/6xxnzvjq |


