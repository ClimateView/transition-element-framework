---
id: emission_factor_petrol_kwh_to_co2e
title: Emission factor petrol WTW
type: parameter
parameter_type: EMISSION_FACTOR
unit: g_co2e_kwh
tags:
  - emission_factors
  - PRIO_GLOBAL
  - emission_factor
values:
  - value: 254.6
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK Data Playbook, Sheet Resources
    reference: https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832
  - value: 323
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        EF Deutschland, da BAFU-Wert nur TTW (266g / kWh)
    reference: https://www.kea-bw.de/kommunaler-klimaschutz/angebote/co2-bilanzierung
  - value: 337
    country: DE
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        BISKO Bilanzierungs-Systematik Kommunal 2024, Kapitel 5, Tabelle 10: Benzin, THG-Emissionsfaktoren (Well-to-Wheel) nach Kraftstoffen im Verkehr unter Berücksichtigung der Beimischung von Biokraftstoffen
    reference: https://repository.difu.de/items/a7d15dbd-7d09-461a-a7a5-0be9f526facb
  - value: 254.6
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK Data Playbook, Sheet Resources
    reference: https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832
  - value: 336
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView modellbeskrivning - Drivmedel
    reference: https://climateview.slab.com/public/78b9qifq
  - value: 240.436
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
| 254.6 | Global | CONSTANT | 2019-01-01 | UK Data Playbook, Sheet Resources | https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832 |
| 323 | CH | CONSTANT | 2019-01-01 | EF Deutschland, da BAFU-Wert nur TTW (266g / kWh) | https://www.kea-bw.de/kommunaler-klimaschutz/angebote/co2-bilanzierung |
| 337 | DE | CONSTANT | 2021-01-01 | BISKO Bilanzierungs-Systematik Kommunal 2024, Kapitel 5, Tabelle 10: Benzin, THG-Emissionsfaktoren (Well-to-Wheel) nach Kraftstoffen im Verkehr unter Berücksichtigung der Beimischung von Biokraftstoffen | https://repository.difu.de/items/a7d15dbd-7d09-461a-a7a5-0be9f526facb |
| 254.6 | GB | CONSTANT | 2019-01-01 | UK Data Playbook, Sheet Resources | https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832 |
| 336 | SE | CONSTANT | 2019-01-01 | ClimateView modellbeskrivning - Drivmedel | https://climateview.slab.com/public/78b9qifq |
| 240.436 | US | CONSTANT | 2019-01-01 | EPA GHG Emission Factors Hub | https://www.epa.gov/system/files/documents/2025-01/ghg-emission-factors-hub-2025.pdf |


