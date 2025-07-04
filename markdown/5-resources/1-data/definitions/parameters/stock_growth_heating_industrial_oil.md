---
id: stock_growth_heating_industrial_oil
title: Growth heating by oil (industrial), per capita
type: parameter
parameter_type: GROWTH_FACTOR
unit: m2_percapita
tags:
  - operations_growth
values:
  - value: 0.1625
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/agxgteq0
  - value: 0.2
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten
  - value: 1.34
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung basierend auf Durchschnittswerten von deutschen Großstädten
    reference: https://climateview.slab.com/public/wvziauke
  - value: 2.4569
    country: ES
    scalingType: CONSTANT
    validFrom: 2017-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#hvhq4-industrial-floor-area-and-space-heating
  - value: 0
    country: FR
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        La plupart des villes n'ont pas de centrales électriques ou chaleur, donc 0. Veuillez vérifier la source pour savoir où trouver des estimations.
    reference: https://climateview.slab.com/posts/energy-industries-france-jdab43ho#hsf52-production-energetique
  - value: 0.0268
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från statistik från energimyndigheten och SCB.
    reference: https://climateview.slab.com/public/posts/dgkomg2d
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.1625 | Global | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/agxgteq0 |
| 0.2 | CH | CONSTANT | 2019-01-01 | ClimateView Schätzung basierend auf Durchschnittswerten von schweizer Städten |  |
| 1.34 | DE | CONSTANT | 2019-01-01 | Schätzung basierend auf Durchschnittswerten von deutschen Großstädten | https://climateview.slab.com/public/wvziauke |
| 2.4569 | ES | CONSTANT | 2017-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/stationary-energy-non-residential-baavcf13#hvhq4-industrial-floor-area-and-space-heating |
| 0 | FR | CONSTANT | 2021-01-01 | La plupart des villes n'ont pas de centrales électriques ou chaleur, donc 0. Veuillez vérifier la source pour savoir où trouver des estimations. | https://climateview.slab.com/posts/energy-industries-france-jdab43ho#hsf52-production-energetique |
| 0.0268 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från statistik från energimyndigheten och SCB. | https://climateview.slab.com/public/posts/dgkomg2d |


