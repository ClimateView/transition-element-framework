---
id: stock_district_heating_biogas
title: District heating biogas
type: parameter
parameter_type: OPERATIONS
unit: kwh
tags:
  - operations
  - PRIO_LOW
values:
  - value: 0
    global: True
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0
    country: CA
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 0
    country: CH
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Annahme: 0.
  - value: 115.64
    country: DE
    scalingType: PER_CAPITA
    validFrom: 2020-01-01
    comment: |
        Schätzungen auf Grundlage von bundesdeutscher Statistik.
    reference: https://climateview.slab.com/public/amazedb1
  - value: 0
    country: GB
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Initialized to zero.
  - value: 101.890393978495
    country: SE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capitavärdet beräknat från SCB och energiföretagen.se
    reference: https://climateview.slab.com/public/qwledwax
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0 | CA | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 0 | CH | PER_CAPITA | 2019-01-01 | Annahme: 0. |  |
| 115.64 | DE | PER_CAPITA | 2020-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/amazedb1 |
| 0 | GB | PER_CAPITA | 2019-01-01 | Initialized to zero. |  |
| 101.890393978495 | SE | PER_CAPITA | 2019-01-01 | Per capitavärdet beräknat från SCB och energiföretagen.se | https://climateview.slab.com/public/qwledwax |


