---
title: T-1A1a-TE-4 - Improved car engine technology
id: improved_vehicle_technology
sector: transport
sustainability: amber
progress: 50
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-15-improved-energy-efficiency-vehicles
name: improved_vehicle_technology
type: update
longName: 'Improved Internal Combustion Engine (ICE) car engine technology to reduce fuel use.'
shortName: 'Car technology'
weightInversionExpression:
  expression: ((1 / ( unknown_x / %[0] )) - 1) / %[1]
  variables:
  - energy_intensity_personal_vehicles_petrol
  - personal_vehicle_efficiency_improvement_factor
description: 'Reduce the amount of energy required to drive petrol and diesel vehicles through improved engine technology'
unitOfMeasure: vehicle_km
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_personal_vehicles_petrol
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - personal_vehicle_efficiency_improvement_factor
- update: energy_intensity_personal_vehicles_diesel
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - personal_vehicle_efficiency_improvement_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: petrol_vehicles
  - chain: diesel_vehicles

---


#  Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Improved vehicle and engine technology - as well as reduced vehicle weight - can reduce emissions from fossil-fueled cars. This shift can help reduce emissions in the short term, until e-mobility and other zero-emission transport modes reach their full potential.

Improved vehicle and engine technology - as well as reduced vehicle weight - can reduce emissions from fossil-fuelled cars.

This shift can help reduce emissions in the short term, until e-mobility and other zero-emission transport modes reach their full potential.

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
