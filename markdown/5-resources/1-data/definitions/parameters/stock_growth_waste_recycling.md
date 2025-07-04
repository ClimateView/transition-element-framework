---
id: stock_growth_waste_recycling
title: Growth of waste recycling operations
type: parameter
parameter_type: GROWTH_FACTOR
unit: tonne_percapita
tags:
  - operations_growth
values:
  - value: 0.18
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita value based on average of our customers.
    reference: https://climateview.slab.com/public/oqhcpcsi
  - value: 0.25
    country: CA
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada -  Waste
    reference: https://climateview.slab.com/public/urqtndqm
  - value: 0.53
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung.
  - value: 3.5
    country: DE
    scalingType: CONSTANT
    validFrom: 2018-01-01
    comment: |
        Schätzungen auf Grundlage von bundesdeutscher Statistik.
    reference: https://climateview.slab.com/public/w94s9azz
  - value: 1.0375
    country: ES
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/waste-spain-90ujr6vf#hnrmr-solid-waste
  - value: 3.2205
    country: FR
    scalingType: CONSTANT
    validFrom: 2018-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/waste-france-pixaibja#hoqfe-dechets-solides
  - value: 0.18
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita value based on average of our customers.
    reference: https://climateview.slab.com/public/oqhcpcsi
  - value: 0.2302
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från avfallsverige.se
    reference: https://climateview.slab.com/public/tbf8luyb
  - value: 0.1919
    country: US
    scalingType: CONSTANT
    validFrom: 2018-01-01
    comment: |
        Value based on US national statistics.
    reference: https://climateview.slab.com/posts/waste-wyk6jfas
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.18 | Global | CONSTANT | 2019-01-01 | Per capita value based on average of our customers. | https://climateview.slab.com/public/oqhcpcsi |
| 0.25 | CA | CONSTANT | 2019-01-01 | Model description ClimateView - Canada -  Waste | https://climateview.slab.com/public/urqtndqm |
| 0.53 | CH | CONSTANT | 2019-01-01 | Schätzung. |  |
| 3.5 | DE | CONSTANT | 2018-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/w94s9azz |
| 1.0375 | ES | CONSTANT | 2019-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/waste-spain-90ujr6vf#hnrmr-solid-waste |
| 3.2205 | FR | CONSTANT | 2018-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/waste-france-pixaibja#hoqfe-dechets-solides |
| 0.18 | GB | CONSTANT | 2019-01-01 | Per capita value based on average of our customers. | https://climateview.slab.com/public/oqhcpcsi |
| 0.2302 | SE | CONSTANT | 2019-01-01 | Per capitavärde framräknat från avfallsverige.se | https://climateview.slab.com/public/tbf8luyb |
| 0.1919 | US | CONSTANT | 2018-01-01 | Value based on US national statistics. | https://climateview.slab.com/posts/waste-wyk6jfas |


