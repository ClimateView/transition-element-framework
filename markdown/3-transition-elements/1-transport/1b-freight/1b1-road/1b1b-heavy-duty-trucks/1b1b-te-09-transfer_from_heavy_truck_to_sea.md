---
title: T-1B1b-TE-9 - Shift from heavy truck to sea
id: transfer_from_heavy_truck_to_sea
sector: transport
sustainability: amber
class: transition
version: 2.0.1
name: transfer_from_heavy_truck_to_sea
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) heavy trucks to diesel marine freight transport.'
shortName: 'Heavy truck to diesel marine'
description: 'Shift tonne kilometer from diesel heavy trucks to ship freight in tonne kilometer to fulfill the need of logistics'
unitOfMeasure: tonne_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_heavy_trucks
  - chain: petrol_heavy_trucks
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: ship_freight
cobenefits:
- air_quality
- reduced_noise
- reduced_accidents
- less_congestion

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Sea transport is a relatively efficient mode of transport, with lower emissions per unit of weight and distance. However, shipping is associated with other environmental hazards such as water, air and sound pollution.




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
