---
title: T-1A4-TE-1 - Shift to LNG fuel for marine passenger transport
id: shift_to_lng_fuel_for_sea_passenger_transportation
sector: transport
sustainability: amber
progress: 25
class: transition
version: 2.0.0
ipccMitigationMethod: 1c-01-alternative-fuels-shipping
name: shift_to_lng_fuel_for_sea_passenger_transportation
type: shift
longName: 'Shift from conventional fueled to LNG marine passenger transport.'
shortName: 'LNG marine passenger transport'
description: 'Shift person kilometer from ship passenger to LNG shipping passenger in person kilometer to fulfill the need of mobility'
unitOfMeasure: person_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: ship_passenger
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: lng_shipping_passenger
cobenefits:
- air_quality

---


# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

TBD

{{ te_sustainability() }}

# Transition Element

{{ get_te_description_table() }}


# Activities

{{ get_te_activities() }}


# Parameters

{{ generate_parameter_table() }}


# YAML Specification

```yaml
{{ json_to_yaml() }}
```
