---
id: emission_factor_diesel_kwh_to_co2e
title: Emission factor fossil diesel WTW
type: parameter
parameter_type: EMISSION_FACTOR
unit: g_co2e_kwh
tags:
  - emission_factors
  - PRIO_GLOBAL
  - emission_factor
values:
  - value: 268.08
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK Data Playbook, Sheet Resources
    reference: https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832
  - value: 326
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        EF Deutschland, da BAFU-Wert nur TTW (264 g/kWh)
    reference: https://www.bafu.admin.ch/dam/bafu/de/dokumente/klima/fachinfo-daten/CO2_Emissionsfaktoren_THG_Inventar.pdf.download.pdf/CO2_Emissionsfaktoren.pdf
  - value: 331
    country: DE
    scalingType: CONSTANT
    validFrom: 2021-01-01
    comment: |
        BISKO Bilanzierungs-Systematik Kommunal 2024, Kapitel 5, Tabelle 10: Diesel, THG-Emissionsfaktoren (Well-to-Wheel) nach Kraftstoffen im Verkehr unter Berücksichtigung der Beimischung von Biokraftstoffen
    reference: https://repository.difu.de/items/a7d15dbd-7d09-461a-a7a5-0be9f526facb
  - value: 268.08
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        UK Data Playbook, Sheet Resources
    reference: https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832
  - value: 342
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView modellbeskrivning - Drivmedel
    reference: https://climateview.slab.com/public/78b9qifq
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 268.08 | Global | CONSTANT | 2019-01-01 | UK Data Playbook, Sheet Resources | https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832 |
| 326 | CH | CONSTANT | 2019-01-01 | EF Deutschland, da BAFU-Wert nur TTW (264 g/kWh) | https://www.bafu.admin.ch/dam/bafu/de/dokumente/klima/fachinfo-daten/CO2_Emissionsfaktoren_THG_Inventar.pdf.download.pdf/CO2_Emissionsfaktoren.pdf |
| 331 | DE | CONSTANT | 2021-01-01 | BISKO Bilanzierungs-Systematik Kommunal 2024, Kapitel 5, Tabelle 10: Diesel, THG-Emissionsfaktoren (Well-to-Wheel) nach Kraftstoffen im Verkehr unter Berücksichtigung der Beimischung von Biokraftstoffen | https://repository.difu.de/items/a7d15dbd-7d09-461a-a7a5-0be9f526facb |
| 268.08 | GB | CONSTANT | 2019-01-01 | UK Data Playbook, Sheet Resources | https://docs.google.com/spreadsheets/d/17hr9o90tcxP3xX9T000uWcXSrzm5b5D3UfPwcq7LzgA/edit?gid=1982830832#gid=1982830832 |
| 342 | SE | CONSTANT | 2019-01-01 | ClimateView modellbeskrivning - Drivmedel | https://climateview.slab.com/public/78b9qifq |


