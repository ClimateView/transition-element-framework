---
title: T-1A1a-TE-11 - Shift to electric bikes
id: shift_to_electric_bikes
sector: transport
sustainability: green
progress: 50
class: transition
version: 2.0.1
ipccMitigationMethod: 1a-02-active-transport-modes
name: shift_to_electric_bikes
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) cars to electric bike.'
shortName: 'Electric bikes'
description: 'Shift vehicle kilometer from petrol,diesel and LPG vehicles to electric bike in vehicle kilometer to fulfill the need of mobility'
unitOfMeasure: person_km
cohort:
  expression: '%[0]'
  variables:
  - proportion_of_personal_vehicles_shiftable_to_electric_bikes
shiftFrom:
  atoc:
    expression: 1 / %[0]
    variables:
    - load_factor_car_average
  chains:
  - chain: petrol_vehicles
  - chain: diesel_vehicles
  - chain: lpg_vehicles
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electric_bikes
cobenefits:
- air_quality
- less_congestion
- reduced_noise

---



#  Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Electric vehicles have zero tailpipe emissions. They are also significantly more energy efficient and quiet than fossil-fueled vehicles. The shift to electric bikes reduces greenhouse gas emissions and helps create a better urban environment.

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
