---
title: T-1B1b-TE-7 - Improved heavy truck engine technology
id: improved_vehicle_technology_heavy_trucks
sector: transport
sustainability: amber
class: transition
version: 2.0.2
name: improved_vehicle_technology_heavy_trucks
ipccMitigationMethod: 1a-15-improved-energy-efficiency-vehicles
type: update
longName: 'Improved Internal Combustion Engine (ICE) heavy truck engine technology to reduce fuel use.'
shortName: 'Heavy truck technology'
weightInversionExpression:
  expression: ((1 / ( unknown_x / %[0] )) - 1) / %[1]
  variables:
  - energy_intensity_freight_heavy_trucks_diesel
  - heavy_truck_efficiency_improvement_factor
description: 'Reduce the amount of energy required to operate diesel, hydrogen and battery electric heavy trucks through improved engine technology'
unitOfMeasure: tonne_km
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_freight_heavy_trucks_diesel
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_efficiency_improvement_factor
- update: energy_intensity_freight_heavy_trucks_bev
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_efficiency_improvement_factor
- update: energy_intensity_freight_heavy_trucks_hydrogen
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_efficiency_improvement_factor
- update: energy_intensity_freight_heavy_trucks_gas
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_efficiency_improvement_factor
- update: energy_intensity_freight_heavy_trucks_petrol
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_efficiency_improvement_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_heavy_trucks
  - chain: battery_electric_heavy_trucks
  - chain: hydrogen_heavy_trucks
  - chain: gas_heavy_trucks
  - chain: petrol_heavy_trucks

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Improved vehicle and engine technology can reduce emissions from fossil-fueled trucks. This shift can help reduce emissions in the short term, until zero-emission technologies reach their full potential.




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
