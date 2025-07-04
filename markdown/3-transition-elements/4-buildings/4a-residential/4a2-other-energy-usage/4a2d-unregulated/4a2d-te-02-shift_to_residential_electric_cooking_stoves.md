---
title: T-4A2d-TE-2 - Shift to residential electric cooking stoves
id: shift_to_residential_electric_cooking_stoves
sector: buildings
sustainability: green
class: transition
type: shift
longName: 'Shift from residential gas cooking stoves to residential electric cooking stoves.'
shortName: 'Electric cooking stoves'
name: shift_to_residential_electric_cooking_stoves                
version: 2.0.0
description: 'Shift kWh from residential cooking gas stoves to residential electric cooking stoves in kWh to fullfill the need for cooking'
unitOfMeasure: households
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '%[0]'
    variables:
    - annual_residential_gas_stove_energy_consumption
  chains:
  - chain: residential_gas_cooking_stoves
shiftTo:
  atoc:
    expression: '%[0]'
    variables:
    - annual_residential_electric_stove_energy_consumption
  chains:
  - chain: residential_electric_cooking_stoves
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
