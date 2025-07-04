---
id: emission_factor_coal_kwh_to_co2e
title: Emission factor coal
type: parameter
parameter_type: EMISSION_FACTOR
unit: g_co2e_kwh
tags:
  - emission_factors
  - PRIO_GLOBAL
  - emission_factor
values:
  - value: 333.68
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK Data Playbook, Sheet Resources
    reference: https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832
  - value: 433
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        BISKO Bilanzierungs-Systematik Kommunal 2024, Kapitel 4, Tabelle 3: Kohle Brikett Heizung DE, THG Emissionsfaktor mit Vorkette bezogen auf den Heizwert
    reference: https://repository.difu.de/items/a7d15dbd-7d09-461a-a7a5-0be9f526facb
  - value: 333.68
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK Data Playbook, Sheet Resources
    reference: https://climateview.slab.com/public/tsku2vip
  - value: 325.613
    country: US
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        EPA GHG Emission Factors Hub
    reference: https://www.epa.gov/system/files/documents/2025-01/ghg-emission-factors-hub-2025.pdf
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 333.68 | Global | CONSTANT | 2019-01-01 | UK Data Playbook, Sheet Resources | https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832 |
| 433 | DE | CONSTANT | 2019-01-01 | BISKO Bilanzierungs-Systematik Kommunal 2024, Kapitel 4, Tabelle 3: Kohle Brikett Heizung DE, THG Emissionsfaktor mit Vorkette bezogen auf den Heizwert | https://repository.difu.de/items/a7d15dbd-7d09-461a-a7a5-0be9f526facb |
| 333.68 | GB | CONSTANT | 2019-01-01 | UK Data Playbook, Sheet Resources | https://climateview.slab.com/public/tsku2vip |
| 325.613 | US | CONSTANT | 2019-01-01 | EPA GHG Emission Factors Hub | https://www.epa.gov/system/files/documents/2025-01/ghg-emission-factors-hub-2025.pdf |


