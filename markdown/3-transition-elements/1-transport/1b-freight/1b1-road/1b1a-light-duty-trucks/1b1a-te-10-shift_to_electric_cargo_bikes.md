---
title: T-1B1a-TE-10 - Shift to electric cargo bikes
id: shift_to_electric_cargo_bikes
sector: transport
sustainability: green
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-12-electric-technologies
name: shift_to_electric_cargo_bikes
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) light trucks to electric cargo bikes.'
shortName: 'Electric cargo bikes'
description: 'Shift vehicle kilometer from diesel and petrol light truck to electric carg bikes in vehicle kilometer to fulfill the need of logistics'
unitOfMeasure: vehicle_km
cohort:
  expression: '%[0]'
  variables:
  - proportion_of_light_trucks_with_short_routes
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_light_trucks
  - chain: petrol_light_trucks
shiftTo:
  atoc:
    expression: 1 + %[0]
    variables:
    - additional_electric_cargo_bikes_per_light_truck
  chains:
  - chain: electric_cargo_bikes
cobenefits:
- air_quality
- less_congestion
- reduced_noise

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Electric vehicles have zero tailpipe emissions. They are also significantly more energy efficient and quiet than fossil-fueled vehicles. The shift to electric cargo bikes reduces greenhouse gas emissions and helps create a better urban environment.




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
