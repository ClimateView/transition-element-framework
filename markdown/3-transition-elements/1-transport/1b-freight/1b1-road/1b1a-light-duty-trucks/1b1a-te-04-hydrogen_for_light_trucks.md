---
title: T-1B1a-TE-4 - Shift to hydrogen for light trucks
id: hydrogen_for_light_trucks
sector: transport
sustainability: green
class: transition
version: 2.0.1
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: hydrogen_for_light_trucks
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) light trucks to hydrogen light trucks.'
shortName: 'Hydrogen light trucks'
description: 'Shift vehicle kilometer from diesel light trucks to hydrogen light trucks in vehicle kilometer to fulfill the need of logistics'
unitOfMeasure: vehicle_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_light_trucks
  - chain: petrol_light_trucks
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: hydrogen_light_trucks
cobenefits:
- air_quality
- reduced_noise

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Hydrogen trucks are a type of electric vehicle. They cause no tailpipe emissions, are significantly more energy efficient and produce less noise than fossil-fueled vehicles. The shift to electric trucks will therefore both reduce greenhouse gas emissions and help create a better urban environment.




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
