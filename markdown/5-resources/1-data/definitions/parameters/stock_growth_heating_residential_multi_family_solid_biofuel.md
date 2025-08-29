---
id: stock_growth_heating_residential_multi_family_solid_biofuel
title: Growth heating by solid biofuel (multi-family), per capita
type: parameter
parameter_type: GROWTH_FACTOR
unit: m2_percapita
tags:
  - operations_growth
values:
  - value: 0
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0.26
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von Schweizer Städten
  - value: 1
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2019-01-01 | Initialized to zero. |  |
| 0.26 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von Schweizer Städten |  |
| 1 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |


