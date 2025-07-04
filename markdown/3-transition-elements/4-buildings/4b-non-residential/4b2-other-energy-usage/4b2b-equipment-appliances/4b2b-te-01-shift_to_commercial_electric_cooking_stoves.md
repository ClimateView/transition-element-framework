---
title: T-4B2b-TE-1 - Shift to commercial electric cooking stoves
id: shift_to_commercial_electric_cooking_stoves
sector: buildings
sustainability: green
class: transition
type: shift
longName: 'Shift from commercial gas cooking stoves to commercial electric cooking stoves'
shortName: 'Electric cooking stoves'
name: shift_to_commercial_electric_cooking_stoves                
version: 2.0.0
description: 'Shift kWh from commercial cooking gas stoves to commercial electric cooking stoves in kWh to fullfill the need for cooking'
unitOfMeasure: facilities
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '%[0]'
    variables:
    - annual_commercial_gas_stove_energy_consumption
  chains:
  - chain: commercial_gas_cooking_stoves
shiftTo:
  atoc:
    expression: '%[0]'
    variables:
    - annual_commercial_electric_stove_energy_consumption
  chains:
  - chain: commercial_electric_cooking_stoves
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
