---
title: T-1A1a-TE-14 - Shift to travel by LPG bus
id: increased_proportion_of_public_transport_by_lpg_bus
sector: transport
sustainability: amber
progress: 50
class: transition
version: 1.1.1
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: increased_proportion_of_public_transport_by_lpg_bus
type: shift
longName: Shift from Internal Combustion Engine (ICE) car to travel by LPG bus.
shortName: LPG bus
description: Shift vehicle kilometer from petrol and diesel vehicles to LPG buses
  in vehicle kilometer to fulfill the need of commuting
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
shiftTo:
  atoc:
    expression: 1 / %[0]
    variables:
    - load_factor_bus_average
  chains:
  - chain: lpg_buses
cobenefits:
- reduced_accidents
- less_congestion
---
#  Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Public transport generates significantly less emissions per passenger than cars. Shifting from cars to public transport will therefore be an essential part of the long-term transition to a sustainable transport system. Public transport has the capacity to transport large numbers of people efficiently, leading to lower levels of congestion, reduced noise levels and an improved urban environment.

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
