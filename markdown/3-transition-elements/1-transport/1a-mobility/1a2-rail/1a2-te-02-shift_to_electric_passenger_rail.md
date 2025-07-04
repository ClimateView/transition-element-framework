---
title: T-1A2-TE-2 - Shift to travel by electric rail
id: shift_to_electric_passenger_rail
sector: transport
sustainability: green
progress: 25
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-12-electric-technologies
name: shift_to_electric_passenger_rail
type: shift
longName: 'Shift from diesel rail passenger transport to electric rail passenger transport.'
shortName: 'Electric rail'
description: 'Shift person kilometer from diesel passenger rail to electric passenger rail in person kilometer to fulfill the need of mobility'
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
  - chain: electric_rail
cobenefits:
- air_quality

---


# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Electric vehicles have zero tailpipe emissions. They are also significantly more energy efficient and quiet than fossil-fueled vehicles. The shift to electric passenger rail reduces greenhouse gas emissions.

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
