---
title: T-1B1a-TE-7 - Route optimisation for light trucks
id: route_optimisation_light_trucks
sector: transport
sustainability: amber
class: transition
version: 2.0.1
ipccMitigationMethod: 1a-08-supply-chain-management
name: route_optimisation_light_trucks
type: upshift
longName: 'Route optimisation for light trucks to reduce distance driven.'
shortName: 'Route optimisation'
description: 'Reduce the amount of vehicle kilometer from diesel light trucks to fulfill the need of logistics through route optimisation'
unitOfMeasure: delivery_route
cohort:
  expression: '1'
variablesToUpdate:
- update: average_route_distance_light_trucks
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - savings_route_optimisation
carbonCausalChains:
  atoc:
    expression: '%[0]'
    variables:
    - average_route_distance_light_trucks
  chains:
  - chain: diesel_light_trucks
  - chain: hydrogen_light_trucks
  - chain: battery_electric_light_trucks
  - chain: petrol_light_trucks
  - chain: gas_light_trucks

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Route optimisation, for instance through mixed loading and joint distribution centers, reduces the distance needed for a truck to reach the end destination.




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
