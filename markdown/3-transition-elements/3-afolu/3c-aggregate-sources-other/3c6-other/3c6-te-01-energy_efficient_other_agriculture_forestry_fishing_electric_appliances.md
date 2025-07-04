---
title: T-3C6-TE-1 - Energy efficient agriculture, forestry and fishing electrical appliances
id: energy_efficient_other_agriculture_forestry_fishing_electric_appliances
sector: afolu
sustainability: green
class: transition
type: update
longName: 'Upgrade agriculture, forestry and fishing electrical appliances to reduce electricity use'
shortName: 'Efficient agriculture, forestry and fishing appliances'
name: energy_efficient_other_agriculture_forestry_fishing_electric_appliances                
version: 2.0.0
description: 'Reduce the amount of energy required to operate agriculture, forestry and fishing electrical appliances'
unitOfMeasure: kwh
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_agriculture_forestry_fishing_unregulated_electricity_use
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - agriculture_forestry_fishing_other_electric_appliances_savings_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: agriculture_forestry_fishing_unregulated_electricity_use
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
