---
id: stock_district_heating_electricity
title: District heating electricity
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
    country: CH
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Annahme: 0.
  - value: 0
    country: DE
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Schätzungen auf Grundlage von bundesdeutscher Statistik.
    reference: https://climateview.slab.com/public/amazedb1
  - value: 0
    country: GB
    scalingType: PER_CAPITA
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/posts/yddbmggd
  - value: 174.2157
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
| 0 | CH | PER_CAPITA | 2019-01-01 | Annahme: 0. |  |
| 0 | DE | PER_CAPITA | 2019-01-01 | Schätzungen auf Grundlage von bundesdeutscher Statistik. | https://climateview.slab.com/public/amazedb1 |
| 0 | GB | PER_CAPITA | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/posts/yddbmggd |
| 174.2157 | SE | PER_CAPITA | 2019-01-01 | Per capitavärdet beräknat från SCB och energiföretagen.se | https://climateview.slab.com/public/qwledwax |


