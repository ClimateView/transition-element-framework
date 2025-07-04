---
title: T-1B1a-TE-1 - Shift to gas light trucks
id: gas_light_trucks
sector: transport
sustainability: amber
class: transition
version: 2.1.0
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: gas_light_trucks
type: shift
longName: Shift from Internal Combustion Engine (ICE) light trucks to compressed natural
  gas (CNG) light trucks.
shortName: CNG light trucks
description: Shift vehicle kilometer from diesel light trucks to gas light trucks
  in vehicle kilometer to fulfill the need of logistics
unitOfMeasure: vehicle_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_light_trucks
  - chain: petrol_light_trucks
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: gas_light_trucks
cobenefits:
- air_quality
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
