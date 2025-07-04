---
id: emission_factor_biogas_kwh_to_co2e
title: Emission factor biogas
type: parameter
parameter_type: EMISSION_FACTOR
unit: g_co2e_kwh
tags:
  - emission_factors
  - PRIO_GLOBAL
  - emission_factor
values:
  - value: 0.23
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK Data Playbook, Sheet Resources
    reference: https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832
  - value: 130
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        KBOB Empfehlung
    reference: https://www.ecobau.ch/resources/uploads/News%20ab%202021/2022/KBOB-Empfehlung_2009-1-2022_220422_v1_0.pdf
  - value: 124
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        BISKO Bilanzierungs-Systematik Kommunal 2024, Kapitel 4, Tabelle 4: Biogas (Gülle) BHKW TA-Luft, THG Emissionsfaktor mit Vorkette bezogen auf den Heizwert
    reference: https://repository.difu.de/items/a7d15dbd-7d09-461a-a7a5-0be9f526facb
  - value: 0.23
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK Data Playbook, Sheet Resources
    reference: https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832
  - value: 0.882
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
| 0.23 | Global | CONSTANT | 2019-01-01 | UK Data Playbook, Sheet Resources | https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832 |
| 130 | CH | CONSTANT | 2019-01-01 | KBOB Empfehlung | https://www.ecobau.ch/resources/uploads/News%20ab%202021/2022/KBOB-Empfehlung_2009-1-2022_220422_v1_0.pdf |
| 124 | DE | CONSTANT | 2019-01-01 | BISKO Bilanzierungs-Systematik Kommunal 2024, Kapitel 4, Tabelle 4: Biogas (Gülle) BHKW TA-Luft, THG Emissionsfaktor mit Vorkette bezogen auf den Heizwert | https://repository.difu.de/items/a7d15dbd-7d09-461a-a7a5-0be9f526facb |
| 0.23 | GB | CONSTANT | 2019-01-01 | UK Data Playbook, Sheet Resources | https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832 |
| 0.882 | US | CONSTANT | 2019-01-01 | EPA GHG Emission Factors Hub | https://www.epa.gov/system/files/documents/2025-01/ghg-emission-factors-hub-2025.pdf |


