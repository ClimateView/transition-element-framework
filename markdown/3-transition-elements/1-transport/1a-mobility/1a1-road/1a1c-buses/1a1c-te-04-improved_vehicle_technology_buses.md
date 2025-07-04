---
title: T-1A1c-TE-4 - Improved bus engine technology
id: improved_vehicle_technology_buses
sector: transport
sustainability: amber
class: transition
type: update
longName: 'Improved bus engine technology to reduce fuel use.'
shortName: 'Bus technology'
name: improved_vehicle_technology_buses                
version: 2.0.0
description: Reduce the amount of energy required to drive diesel, petrol, hydrogen, CNG and LPG buses through improved engine technology
weightInversionExpression:
  expression: ((1 / ( unknown_x / %[0] )) - 1) / %[1]
  variables:
  - energy_intensity_buses_diesel
  - bus_efficiency_improvement_factor
unitOfMeasure: vehicle_km
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_buses_diesel
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - bus_efficiency_improvement_factor
- update: energy_intensity_buses_petrol
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - bus_efficiency_improvement_factor
- update: energy_intensity_buses_hydrogen
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - bus_efficiency_improvement_factor
- update: energy_intensity_buses_gas
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - bus_efficiency_improvement_factor
- update: energy_intensity_buses_lpg
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - bus_efficiency_improvement_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_buses
  - chain: petrol_buses
  - chain: hydrogen_buses
  - chain: gas_buses
  - chain: lpg_buses
---

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

TBD

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
