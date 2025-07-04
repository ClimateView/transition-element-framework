---
id: stock_waste_incineration
title: Stock of incinerated waste
type: parameter
parameter_type: OPERATIONS
unit: tonne
tags:
  - operations
  - PRIO_HIGH
values:
  - value: 0.17
    global: True
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita value based on average of our customers.
    reference: https://climateview.slab.com/public/oqhcpcsi
  - value: 0.02
    country: CA
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada -  Waste
    reference: https://climateview.slab.com/public/urqtndqm
  - value: 0.3
    country: CH
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Schätzung.
  - value: 0.58
    country: DE
    scalingType: PER_CAPITA
    validFrom: 2018-01-01
    comment: |
        Schätzungen auf Grundlage von bundesdeutscher Statistik.
    reference: https://climateview.slab.com/public/w94s9azz
  - value: 0.0831
    country: ES
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/waste-spain-90ujr6vf#hnrmr-solid-waste
  - value: 0.0649
    country: FR
    scalingType: PER_CAPITA
    validFrom: 2018-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/waste-france-pixaibja#hoqfe-dechets-solides
  - value: 0.00270102716
    country: GB
    scalingType: PER_CAPITA
    validFrom: 2020-01-01
    comment: |
        Based on national statistics
  - value: 0.2372
    country: SE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capitavärde framräknat från avfallsverige.se
    reference: https://climateview.slab.com/public/tbf8luyb
  - value: 0
    country: US
    scalingType: PER_CAPITA
    validFrom: 2018-01-01
    comment: |
        Value based on US national statistics.
    reference: https://climateview.slab.com/posts/waste-wyk6jfas
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.17 | Global | PER_CAPITA | 2019-01-01 | Per capita value based on average of our customers. | https://climateview.slab.com/public/oqhcpcsi |
| 0.02 | CA | PER_CAPITA | 2019-01-01 | Model description ClimateView - Canada -  Waste | https://climateview.slab.com/public/urqtndqm |
| 0.3 | CH | PER_CAPITA | 2019-01-01 | Schätzung. |  |
| 0.58 | DE | PER_CAPITA | 2018-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/w94s9azz |
| 0.0831 | ES | PER_CAPITA | 2019-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/waste-spain-90ujr6vf#hnrmr-solid-waste |
| 0.0649 | FR | PER_CAPITA | 2018-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/waste-france-pixaibja#hoqfe-dechets-solides |
| 0.00270102716 | GB | PER_CAPITA | 2020-01-01 | Based on national statistics |  |
| 0.2372 | SE | PER_CAPITA | 2019-01-01 | Per capitavärde framräknat från avfallsverige.se | https://climateview.slab.com/public/tbf8luyb |
| 0 | US | PER_CAPITA | 2018-01-01 | Value based on US national statistics. | https://climateview.slab.com/posts/waste-wyk6jfas |


