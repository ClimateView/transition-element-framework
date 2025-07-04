---
title: T-1A1a-TE-10 - Shift to walking and cycling
id: increased_proportion_of_walking_and_cycling
sector: transport
sustainability: green
progress: 50
class: transition
version: 2.1.1
ipccMitigationMethod: 1a-02-active-transport-modes
name: increased_proportion_of_walking_and_cycling
type: shift
longName: Shift from Internal Combustion Engine (ICE) cars to walking and cycling.
shortName: Walking and cycling
description: Shift vehicle kilometer from petrol, diesel, LPG and gas vehicles to
  walking cycling in person kilometer to fulfill the need of commuting
unitOfMeasure: commutes
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: 1 / %[0]
    variables:
    - load_factor_car_average
  chains:
  - chain: petrol_vehicles
  - chain: diesel_vehicles
  - chain: lpg_vehicles
  - chain: gas_vehicles
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: walking_cycling
cobenefits:
- air_quality
- reduced_noise
- reduced_accidents
- less_congestion
---
#  Background


Cycling and walking cause no greenhouse gas emissions, no particulate emissions and no noise. Shifting from cars to cycling and walking can greatly improve both public health and the urban environment.

Cycling and walking are both fully emission-free modes of transport. Replacing short-distance car trips with cycling or walking therefore leads to significantly less emissions.

Cycling and walking also have several other positive effects, such as improved air quality, better public health and reduced noise levels.

For more information see {{ ipcc_mitigation_link() }}.

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
