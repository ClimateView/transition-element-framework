---
id: energy_intensity_dh_water_sourced_heatpumps
title: Energy intensity water sourced heat pumps in DH
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_kwh
tags:
  - energy_intensity
  - PRIO_LOW
values:
  - value: 0.333
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Value based on German data.
    reference: https://hd-kohlefrei.de/energiewende-in-der-waermeversorgung/flusswaerme/
  - value: 0.333
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Beispiel Heidelberg. (Energieintensität = 1 / Jahresarbeitszahl)
    reference: https://hd-kohlefrei.de/energiewende-in-der-waermeversorgung/flusswaerme/
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0.333 | Global | CONSTANT | 2019-01-01 | Value based on German data. | https://hd-kohlefrei.de/energiewende-in-der-waermeversorgung/flusswaerme/ |
| 0.333 | DE | CONSTANT | 2019-01-01 | Beispiel Heidelberg. (Energieintensität = 1 / Jahresarbeitszahl) | https://hd-kohlefrei.de/energiewende-in-der-waermeversorgung/flusswaerme/ |


