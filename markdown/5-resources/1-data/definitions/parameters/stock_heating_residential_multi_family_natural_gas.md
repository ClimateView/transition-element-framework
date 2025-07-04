---
id: stock_heating_residential_multi_family_natural_gas
title: Stock gas heating of multi-family buildings
type: parameter
parameter_type: OPERATIONS
unit: m2
tags:
  - operations
  - PRIO_HIGH
values:
  - value: 4
    global: True
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 5.59
    country: CA
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada -  Heating - Residential
    reference: https://climateview.slab.com/public/4h572llp
  - value: 0.78
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Quebec - Heating - Residential
    reference: https://climateview.slab.com/public/posts/cpb5mavl
  - value: 9.53
    country: CH
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 12.33
    country: DE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 15.2397
    country: ES
    scalingType: PER_CAPITA
    validFrom: 2020-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating
  - value: 6.2039
    country: FR
    scalingType: PER_CAPITA
    validFrom: 2016-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hvdfv-tableau-3-chauffage-des-appartements-5
  - value: 4
    country: GB
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 0.2065
    country: SE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från statistik från energimyndigheten och SCB.
    reference: https://climateview.slab.com/public/uui9yijv
  - value: 4.86
    country: US
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US national statistics.
    reference: https://climateview.slab.com/public/posts/f34d3tuu
  - value: 3.06
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/8ebqlj1p
  - value: 1.75
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/saj38uul
  - value: 5.37
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/c5my1ifd
  - value: 1.75
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/saj38uul
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 4 | Global | PER_CAPITA | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/zy17l63p |
| 5.59 | CA | PER_CAPITA | 2019-01-01 | Model description ClimateView - Canada -  Heating - Residential | https://climateview.slab.com/public/4h572llp |
| 0.78 | CA-QC | PER_CAPITA | 2019-01-01 | Model description ClimateView - Quebec - Heating - Residential | https://climateview.slab.com/public/posts/cpb5mavl |
| 9.53 | CH | PER_CAPITA | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 12.33 | DE | PER_CAPITA | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 15.2397 | ES | PER_CAPITA | 2020-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating |
| 6.2039 | FR | PER_CAPITA | 2016-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hvdfv-tableau-3-chauffage-des-appartements-5 |
| 4 | GB | PER_CAPITA | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/zy17l63p |
| 0.2065 | SE | PER_CAPITA | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/uui9yijv |
| 4.86 | US | PER_CAPITA | 2019-01-01 | Value based on US national statistics. | https://climateview.slab.com/public/posts/f34d3tuu |
| 3.06 | US-CA | PER_CAPITA | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/8ebqlj1p |
| 1.75 | US-FL | PER_CAPITA | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/saj38uul |
| 5.37 | US-IN | PER_CAPITA | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/c5my1ifd |
| 1.75 | US-VA | PER_CAPITA | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/saj38uul |


