---
title: T-1A1a-TE-18 - Shift to trams, light rail and subway
id: increased_proportion_of_public_transport_by_trams_and_light_rail
sector: transport
sustainability: green
progress: 50
class: transition
version: 2.1.1
ipccMitigationMethod: 1a-03-public-transit
name: increased_proportion_of_public_transport_by_trams_and_light_rail
type: shift
longName: Shift from Internal Combustion Engine (ICE) car to trams, light rail and
  subway.
shortName: Trams, light rail and subway
description: Shift vehicle kilometer from petrol, diesel, LPG and gas vehicles to
  tram and light rail in vehicle kilometer to fulfill the need of commuting
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
    expression: 1 / %[0]
    variables:
    - load_factor_tram_average
  chains:
  - chain: tram_and_light_rail
cobenefits:
- air_quality
- reduced_noise
- reduced_accidents
- less_congestion
---
#  Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Public transport can move large numbers of people efficiently, causing lower emissions, reduced noise levels, less congestion and an improved urban environment.

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
