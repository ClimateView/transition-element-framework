---
id: emission_factor_district_heating_kwh_to_co2e
title: Emission factor district heating
type: parameter
parameter_type: EMISSION_FACTOR
unit: g_co2e_kwh
tags:
  - emission_factors
  - PRIO_LOW
  - emission_factor
values:
  - value: 47.7
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Target 2030 for a UK ClimateView City
    reference: https://climateview.slab.com/public/yddbmggd
  - value: 270
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Schätzung.
  - value: 198
    country: DE
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        Fernwärmemix Deutschland 2021
    reference: https://www.co2online.de/modernisieren-und-bauen/heizung/fernwaerme/
  - value: 179.7
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK Data Playbook, Sheet Resources
    reference: https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832
  - value: 53.7
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Antar att all fjärrvärmeproduktion i Sverige går mot klimatneutralitet
    reference: https://www.energiforetagen.se/statistik/fjarrvarmestatistik/miljovardering-av-fjarrvarme/
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 47.7 | Global | CONSTANT | 2019-01-01 | Target 2030 for a UK ClimateView City | https://climateview.slab.com/public/yddbmggd |
| 270 | CH | CONSTANT | 2019-01-01 | Schätzung. |  |
| 198 | DE | CONSTANT | 2021-01-01 | Fernwärmemix Deutschland 2021 | https://www.co2online.de/modernisieren-und-bauen/heizung/fernwaerme/ |
| 179.7 | GB | CONSTANT | 2019-01-01 | UK Data Playbook, Sheet Resources | https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832 |
| 53.7 | SE | CONSTANT | 2019-01-01 | Antar att all fjärrvärmeproduktion i Sverige går mot klimatneutralitet | https://www.energiforetagen.se/statistik/fjarrvarmestatistik/miljovardering-av-fjarrvarme/ |


