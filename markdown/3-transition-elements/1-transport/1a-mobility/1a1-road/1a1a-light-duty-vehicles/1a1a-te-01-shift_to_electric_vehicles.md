---
title: T-1A1a-TE-1 - Shift to electric cars
id: shift_to_electric_vehicles
sector: transport
sustainability: green
progress: 50
ipccMitigationMethod: 1a-12-electric-technologies
class: transition
version: 2.0.1
name: shift_to_electric_vehicles
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) cars to electric cars.'
shortName: 'Electric cars'
description: 'Shift vehicle kilometer from petrol, diesel, LPG and gas vehicles to battery electric vehicles in vehicle kilometer to fulfill the need of mobility'
unitOfMeasure: vehicles
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '%[0]'
    variables:
    - distance_per_car
  chains:
  - chain: petrol_vehicles
  - chain: diesel_vehicles
  - chain: lpg_vehicles
  - chain: gas_vehicles
shiftTo:
  atoc:
    expression: '%[0]'
    variables:
    - distance_per_car
  chains:
  - chain: battery_electric_vehicles
cobenefits:
- air_quality
- reduced_noise
---


#  Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Electric vehicles cause no tailpipe emissions. They are also significantly more energy efficient and produce less noise than fossil-fueled vehicles. The shift to electric cars will therefore both reduce greenhouse gas emissions and help create a better urban environment.

Electric vehicles cause more emissions in the production phase than internal combustion engine cars, but cause less emissions over the lifetime of the car.

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
