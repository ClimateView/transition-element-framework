---
id: energy_intensity_heating_residential_single_family_new_buildings
title: Energy intensity new single family buildings
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
        https://www.minergie.ch/de/ueber-minergie/neubau/minergie/
    reference: https://www.minergie.ch/de/ueber-minergie/neubau/minergie/
  - value: 55
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
  - value: 95
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        ClimateView model beskrivning - Energikonsumtion bostäder och lokaler
    reference: https://climateview.slab.com/public/x7khi1nl
  - value: 45
    country: US
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Assumption
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 70 | Global | CONSTANT | 2019-01-01 | Calculated from building regulations and taking performance gap into account | https://climateview.slab.com/public/zy17l63p |
| 55 | CH | CONSTANT | 2019-01-01 | https://www.minergie.ch/de/ueber-minergie/neubau/minergie/ | https://www.minergie.ch/de/ueber-minergie/neubau/minergie/ |
| 55 | DE | CONSTANT | 2019-01-01 | entspricht Standard KfW-Effizienzhaus 55 | https://www.energiesparen-im-haushalt.de/energie/bauen-und-modernisieren/hausbau-regenerative-energie/energieverbrauch/kfw-55-haus.html#:~:text=Der%20Name%20ist%20Programm%3A%20Der,den%20KfW%20100%20Standard%20erf%C3%BCllt. |
| 70 | GB | CONSTANT | 2019-01-01 | Calculated from building regulations and taking performance gap into account | https://climateview.slab.com/public/zy17l63p |
| 95 | SE | CONSTANT | 2019-01-01 | ClimateView model beskrivning - Energikonsumtion bostäder och lokaler | https://climateview.slab.com/public/x7khi1nl |
| 45 | US | CONSTANT | 2019-01-01 | Assumption |  |


