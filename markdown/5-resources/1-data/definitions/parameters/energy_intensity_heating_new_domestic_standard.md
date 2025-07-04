---
id: energy_intensity_heating_new_domestic_standard
title: Energy intensity new domestic buildings (standard)
type: parameter
parameter_type: ENERGY_INTENSITY
unit: kwh_m2
tags:
  - energy_intensity
  - PRIO_LOW
values:
  - value: 70
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Calculated from building regulations and taking performance gap into account
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 55
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Minergie.ch
    reference: https://www.minergie.ch/de/ueber-minergie/neubau/minergie/
  - value: 35
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        entspricht Standard KfW-Effizienzhaus 55
    reference: https://www.energiesparen-im-haushalt.de/energie/bauen-und-modernisieren/hausbau-regenerative-energie/energieverbrauch/kfw-55-haus.html#:~:text=Der%20Name%20ist%20Programm%3A%20Der,den%20KfW%20100%20Standard%20erf%C3%BCllt.
  - value: 70
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Calculated from building regulations and taking performance gap into account
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 85
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView modellbeskrivning - Energikonsumtion bostäder och lokaler
    reference: https://climateview.slab.com/public/x7khi1nl
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 70 | Global | CONSTANT | 2019-01-01 | Calculated from building regulations and taking performance gap into account | https://climateview.slab.com/public/zy17l63p |
| 55 | CH | CONSTANT | 2019-01-01 | Minergie.ch | https://www.minergie.ch/de/ueber-minergie/neubau/minergie/ |
| 35 | DE | CONSTANT | 2019-01-01 | entspricht Standard KfW-Effizienzhaus 55 | https://www.energiesparen-im-haushalt.de/energie/bauen-und-modernisieren/hausbau-regenerative-energie/energieverbrauch/kfw-55-haus.html#:~:text=Der%20Name%20ist%20Programm%3A%20Der,den%20KfW%20100%20Standard%20erf%C3%BCllt. |
| 70 | GB | CONSTANT | 2019-01-01 | Calculated from building regulations and taking performance gap into account | https://climateview.slab.com/public/zy17l63p |
| 85 | SE | CONSTANT | 2019-01-01 | ClimateView modellbeskrivning - Energikonsumtion bostäder och lokaler | https://climateview.slab.com/public/x7khi1nl |


