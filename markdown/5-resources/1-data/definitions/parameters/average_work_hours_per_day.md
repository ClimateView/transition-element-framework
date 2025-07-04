---
id: average_work_hours_per_day
title: Average working hours per day
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: h
tags:
  - atoc
  - PRIO_LOW
  - socioeconomic_parameter
values:
  - value: 8
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Normal working day in many countries
  - value: 8
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Bundesamt für Energie, BFE
    reference: https://www.gaav.de/arbeitsrecht/arbeitszeit.html#:~:text=%C3%9Cblicherweise%20werden%20in%20der%20Schweiz,5%20Stunden%20pro%20Woche%20gearbeitet.
  - value: 7.5
    country: FR
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Hours worked, Insee
    reference: https://dares.travail-emploi.gouv.fr/donnees/la-duree-individuelle-du-travail
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 8 | Global | CONSTANT | 2019-01-01 | Normal working day in many countries |  |
| 8 | CH | CONSTANT | 2019-01-01 | Bundesamt für Energie, BFE | https://www.gaav.de/arbeitsrecht/arbeitszeit.html#:~:text=%C3%9Cblicherweise%20werden%20in%20der%20Schweiz,5%20Stunden%20pro%20Woche%20gearbeitet. |
| 7.5 | FR | CONSTANT | 2019-01-01 | Hours worked, Insee | https://dares.travail-emploi.gouv.fr/donnees/la-duree-individuelle-du-travail |


