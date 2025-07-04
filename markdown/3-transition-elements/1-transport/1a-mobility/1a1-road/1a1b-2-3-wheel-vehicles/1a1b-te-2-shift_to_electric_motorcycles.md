---
title: T-1A1b-TE-2 - Shift to electric motorcycles
id: shift_to_electric_motorcycles
sector: transport
sustainability: green
progress: 50
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-12-electric-technologies
name: shift_to_electric_motorcycles
type: shift
longName: 'Shift from petrol motorcycles to electric motorcycles.'
shortName: 'Electric motorcycles'
description: 'Shift vehicle kilometer from petrol motorcycles to electric motorcycles in vehicle kilometer to fulfill the need of mobility'
unitOfMeasure: vehicle_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: petrol_motorcycles
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electric_motorcycles
cobenefits:
- air_quality

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Electric vehicles have zero tailpipe emissions. They are also significantly more energy efficient and quiet than fossil-fueled vehicles. The shift to electric motorcycles reduces greenhouse gas emissions and helps create a better urban environment.

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