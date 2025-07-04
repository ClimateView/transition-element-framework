---
title: T-1A2-TE-3 - Shift to travel by hydrogen rail
id: shift_to_hydrogen_passenger_rail
sector: transport
sustainability: green
progress: 25
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: shift_to_hydrogen_passenger_rail
type: shift
longName: 'Shift from diesel rail passenger transport to hydrogen rail passenger transport.'
shortName: 'Hydrogen rail'
description: 'Shift person kilometer from diesel passenger rail to hydrogen passenger rail in person kilometer to fulfill the need of mobility'
unitOfMeasure: person_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_passenger_rail
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: hydrogen_passenger_rail
cobenefits:
- air_quality

---


# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Hydrogen vehicles have zero tailpipe emissions. They are also significantly more energy efficient and quiet than fossil-fueled vehicles. The shift to hydrogen passenger rail reduces greenhouse gas emissions given that the production of the hydrogen is from a low emission source.

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
