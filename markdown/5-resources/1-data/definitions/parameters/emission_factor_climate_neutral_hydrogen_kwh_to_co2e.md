---
id: emission_factor_climate_neutral_hydrogen_kwh_to_co2e
title: Emission factor hydrogen (climate neutral)
type: parameter
parameter_type: EMISSION_FACTOR
unit: g_co2e_kwh
tags:
  - emission_factors
  - PRIO_GLOBAL
  - emission_factor
values:
  - value: 20
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView model description - H2
    reference: https://climateview.slab.com/public/7z3rwu55
  - value: 50
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Daten aus Deutschland.
    reference: https://www.dihk.de/resource/blob/24872/fd2c89df9484cf912199041a9587a3d6/dihk-faktenpapier-wasserstoff-data.pdf
  - value: 50
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Deutsche Industrie und Handelskammern
    reference: https://www.dihk.de/resource/blob/24872/fd2c89df9484cf912199041a9587a3d6/dihk-faktenpapier-wasserstoff-data.pdf
  - value: 20
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView model description - H2
    reference: https://climateview.slab.com/public/7z3rwu55
  - value: 20
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView modellbeskrivning  - vätgas
    reference: https://climateview.slab.com/public/ck83bl0f
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 20 | Global | CONSTANT | 2019-01-01 | ClimateView model description - H2 | https://climateview.slab.com/public/7z3rwu55 |
| 50 | CH | CONSTANT | 2019-01-01 | Daten aus Deutschland. | https://www.dihk.de/resource/blob/24872/fd2c89df9484cf912199041a9587a3d6/dihk-faktenpapier-wasserstoff-data.pdf |
| 50 | DE | CONSTANT | 2019-01-01 | Deutsche Industrie und Handelskammern | https://www.dihk.de/resource/blob/24872/fd2c89df9484cf912199041a9587a3d6/dihk-faktenpapier-wasserstoff-data.pdf |
| 20 | GB | CONSTANT | 2019-01-01 | ClimateView model description - H2 | https://climateview.slab.com/public/7z3rwu55 |
| 20 | SE | CONSTANT | 2019-01-01 | ClimateView modellbeskrivning  - vätgas | https://climateview.slab.com/public/ck83bl0f |


