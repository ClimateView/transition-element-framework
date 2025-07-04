---
id: energy_intensity_heating_new_commercial_standard
title: Energy intensity new commercial buildings (standard)
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
        Assuming same as German kfW-Effizienzhaus
    reference: https://climateview.slab.com/public/zy17l63p
  - value: 55
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Minergie.ch
    reference: https://www.minergie.ch/de/ueber-minergie/neubau/minergie/
  - value: 55
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        entspricht Standard KfW-Effizienzhaus 55
    reference: https://www.energiesparen-im-haushalt.de/energie/bauen-und-modernisieren/hausbau-regenerative-energie/energieverbrauch/kfw-55-haus.html#:~:text=Der%20Name%20ist%20Programm%3A%20Der,den%20KfW%20100%20Standard%20erf%C3%BCllt.
  - value: 55
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Assuming same as German kfW-Effizienzhaus
    reference: https://www.energiesparen-im-haushalt.de/energie/bauen-und-modernisieren/hausbau-regenerative-energie/energieverbrauch/kfw-55-haus.html#:~:text=Der%20Name%20ist%20Programm%3A%20Der,den%20KfW%20100%20Standard%20erf%C3%BCllt.
  - value: 70
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Passiv hus standard
    reference: https://passiv.de/de/02_informationen/02_qualitaetsanforderungen/02_qualitaetsanforderungen.htm
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 70 | Global | CONSTANT | 2019-01-01 | Assuming same as German kfW-Effizienzhaus | https://climateview.slab.com/public/zy17l63p |
| 55 | CH | CONSTANT | 2019-01-01 | Minergie.ch | https://www.minergie.ch/de/ueber-minergie/neubau/minergie/ |
| 55 | DE | CONSTANT | 2019-01-01 | entspricht Standard KfW-Effizienzhaus 55 | https://www.energiesparen-im-haushalt.de/energie/bauen-und-modernisieren/hausbau-regenerative-energie/energieverbrauch/kfw-55-haus.html#:~:text=Der%20Name%20ist%20Programm%3A%20Der,den%20KfW%20100%20Standard%20erf%C3%BCllt. |
| 55 | GB | CONSTANT | 2019-01-01 | Assuming same as German kfW-Effizienzhaus | https://www.energiesparen-im-haushalt.de/energie/bauen-und-modernisieren/hausbau-regenerative-energie/energieverbrauch/kfw-55-haus.html#:~:text=Der%20Name%20ist%20Programm%3A%20Der,den%20KfW%20100%20Standard%20erf%C3%BCllt. |
| 70 | SE | CONSTANT | 2019-01-01 | Passiv hus standard | https://passiv.de/de/02_informationen/02_qualitaetsanforderungen/02_qualitaetsanforderungen.htm |


