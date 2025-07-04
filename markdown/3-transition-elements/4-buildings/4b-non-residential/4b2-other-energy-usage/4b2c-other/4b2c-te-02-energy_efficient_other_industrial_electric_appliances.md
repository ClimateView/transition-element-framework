---
title: T-4B2c-TE-2 - Energy efficient industrial electrical appliances
id: energy_efficient_other_industrial_electric_appliances
sector: buildings
sustainability: green
class: transition
type: update
longName: 'Upgrade industrial electrical appliances to reduce electricity use'
shortName: 'Efficient industrial appliances'
name: energy_efficient_other_industrial_electric_appliances                
version: 2.0.0
description: 'Reduce the amount of energy required to operate industrial electrical appliances'
unitOfMeasure: kwh
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_industrial_unregulated_electricity_use
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - industrial_other_electric_appliances_savings_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: industrial_unregulated_electricity_use
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
