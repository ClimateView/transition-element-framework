---
id: stock_growth_heating_residential_multi_family_heat_pumps
title: Growth heating by heat pumps (multi-family), per capita
type: parameter
parameter_type: GROWTH_FACTOR
unit: m2_percapita
tags:
  - operations_growth
values:
  - value: 0.01
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 0
    country: CA
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada -  Heating - Residential
    reference: https://climateview.slab.com/public/4h572llp
  - value: 0.21
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Quebec - Heating - Residential
    reference: https://climateview.slab.com/public/posts/cpb5mavl
  - value: 0.02
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von Schweizer Städten
  - value: 0.65
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 0
    country: ES
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating
  - value: 0
    country: FR
    scalingType: CONSTANT
    validFrom: 2016-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hvdfv-tableau-3-chauffage-des-appartements-5
  - value: 0.01
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 0.8259
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från statistik från energimyndigheten och SCB.
    reference: https://climateview.slab.com/public/uui9yijv
  - value: 0
    country: US
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Value based on US national statistics.
    reference: https://climateview.slab.com/public/posts/f34d3tuu
  - value: 0
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/8ebqlj1p
  - value: 0
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/saj38uul
  - value: 0
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/c5my1ifd
  - value: 0
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Value based on US regional statistics.
    reference: https://climateview.slab.com/public/posts/saj38uul
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.01 | Global | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/zy17l63p |
| 0 | CA | CONSTANT | 2019-01-01 | Model description ClimateView - Canada -  Heating - Residential | https://climateview.slab.com/public/4h572llp |
| 0.21 | CA-QC | CONSTANT | 2019-01-01 | Model description ClimateView - Quebec - Heating - Residential | https://climateview.slab.com/public/posts/cpb5mavl |
| 0.02 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von Schweizer Städten |  |
| 0.65 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 0 | ES | CONSTANT | 2020-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-residential-5b7n1rw0#hsv7b-space-heating |
| 0 | FR | CONSTANT | 2016-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/stationary-energy-residential-france-bnynu72j#hvdfv-tableau-3-chauffage-des-appartements-5 |
| 0.01 | GB | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/zy17l63p |
| 0.8259 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/uui9yijv |
| 0 | US | CONSTANT | 2019-01-01 | Value based on US national statistics. | https://climateview.slab.com/public/posts/f34d3tuu |
| 0 | US-CA | CONSTANT | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/8ebqlj1p |
| 0 | US-FL | CONSTANT | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/saj38uul |
| 0 | US-IN | CONSTANT | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/c5my1ifd |
| 0 | US-VA | CONSTANT | 2019-01-01 | Value based on US regional statistics. | https://climateview.slab.com/public/posts/saj38uul |


