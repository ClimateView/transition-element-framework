---
title: T-4A2d-TE-1 - Energy efficient residential electrical appliances
id: energy_efficient_other_residential_electric_appliances
sector: buildings
sustainability: amber
class: transition
type: update
longName: 'Upgrade residential electrical appliances to reduce electricity use.'
shortName: 'Efficient residential appliances'
name: energy_efficient_other_residential_electric_appliances                
version: 2.0.0
description: 'Reduce the amount of energy required to operate residential electrical appliances'
unitOfMeasure: kwh
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_residential_unregulated_electricity_use
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - residential_other_electric_appliances_savings_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: residential_unregulated_electricity_use
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
