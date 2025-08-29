---
title: T-1B1b-TE-1 - Shift to gas heavy trucks
id: gas_heavy_trucks
sector: transport
sustainability: amber
class: transition
version: 2.0.1
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: gas_heavy_trucks
type: shift
longName: Shift from Internal Combustion Engine (ICE) heavy trucks to compressed natural gas (CNG) heavy trucks.
shortName: CNG heavy trucks
description: Shift tonne kilometer from diesel heavy trucks to gas heavy trucks in tonne kilometer to fulfill the need of logistics
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
  - chain: gas_heavy_trucks
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
