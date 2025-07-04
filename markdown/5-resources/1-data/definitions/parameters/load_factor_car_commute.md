---
id: load_factor_car_commute
title: Load factor car commute
type: parameter
parameter_type: SOCIOECONOMIC_PARAMETER
unit: persons
tags:
  - atoc
  - PRIO_MEDIUM
  - socioeconomic_parameter
values:
  - value: 1.13
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        NTM model
    reference: https://www.transportmeasures.org/en/wiki/evaluation-transport-suppliers/car-traffic-baselines-2017/
  - value: 1.1
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Mikrozensus Verkehrsverhalten der Bevölkerung (2015)
    reference: https://ethz.ch/content/dam/ethz/associates/services/organisation/Schulleitung/mobilitaetsplattform/images/Mikrozensus_Verkehrsverhalten%20der%20Bev%C3%B6lkerung%202015_BFS_ARE_de.pdf
  - value: 1.3
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        SRV 2018 TU Dresden
    reference: https://climateview.slab.com/public/z1katuv7
  - value: 1.13
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        NTM model
    reference: https://www.transportmeasures.org/en/wiki/evaluation-transport-suppliers/car-traffic-baselines-2017/
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 1.13 | Global | CONSTANT | 2019-01-01 | NTM model | https://www.transportmeasures.org/en/wiki/evaluation-transport-suppliers/car-traffic-baselines-2017/ |
| 1.1 | CH | CONSTANT | 2019-01-01 | Mikrozensus Verkehrsverhalten der Bevölkerung (2015) | https://ethz.ch/content/dam/ethz/associates/services/organisation/Schulleitung/mobilitaetsplattform/images/Mikrozensus_Verkehrsverhalten%20der%20Bev%C3%B6lkerung%202015_BFS_ARE_de.pdf |
| 1.3 | DE | CONSTANT | 2019-01-01 | SRV 2018 TU Dresden | https://climateview.slab.com/public/z1katuv7 |
| 1.13 | SE | CONSTANT | 2019-01-01 | NTM model | https://www.transportmeasures.org/en/wiki/evaluation-transport-suppliers/car-traffic-baselines-2017/ |


