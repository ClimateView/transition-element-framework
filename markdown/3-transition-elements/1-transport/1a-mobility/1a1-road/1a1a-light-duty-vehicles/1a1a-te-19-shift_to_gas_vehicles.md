---
title: T-1A1a-TE-19 - Shift to gas cars
id: shift_to_gas_vehicles
sector: transport
sustainability: amber
progress: 50
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: shift_to_gas_vehicles
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) cars to compressed natural gas (CNG) cars.'
shortName: 'CNG cars'
description: 'Shift vehicle kilometer from petrol and diesel vehicles to gas vehicles in vehicle kilometer to fulfill the need of mobility'
unitOfMeasure: vehicles
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '%[0]'
    variables:
    - distance_per_car
  chains:
  - chain: petrol_vehicles
  - chain: diesel_vehicles
shiftTo:
  atoc:
    expression: '%[0]'
    variables:
    - distance_per_car
  chains:
  - chain: gas_vehicles
cobenefits:
- air_quality

---



#  Background

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
