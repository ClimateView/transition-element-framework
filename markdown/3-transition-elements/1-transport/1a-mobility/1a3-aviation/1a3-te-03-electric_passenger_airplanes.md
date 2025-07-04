---
title: T-1A3-TE-3 - Shift to electric air passenger transport
id: electric_passenger_airplanes
sector: transport
sustainability: green
progress: 25
class: transition
version: 2.0.0
ipccMitigationMethod: 1b-02-alternative-fuels-aircraft
name: electric_passenger_airplanes
type: shift
longName: 'Shift from conventional fueled to electric air passenger transport.'
shortName: 'Electric airplanes'
description: 'Shift person kilometer from passenger transportation by air to electric passenger transportation by air in person kilometer to fulfill the need of mobility'
unitOfMeasure: person_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: passenger_transportation_by_air
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electric_passenger_transportation_by_air
cobenefits:
- air_quality
- reduced_noise

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
