---
title: T-2C1-TE-4 - Shift to electricity in iron and steel industries
id: shift_to_electricity_in_iron_and_steel_industries
sector: industry
sustainability: green
class: transition
type: shift
longName: 'Shift from coal and natural gas combustion to electricity for iron and steel industries energy use'
shortName: 'Electricity in iron and steel'
name: shift_to_electricity_in_iron_and_steel_industries                
version: 2.0.0
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: coal_usage_within_iron_and_steel_industries
  - chain: natural_gas_usage_within_iron_and_steel_industries
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electricity_usage_within_iron_and_steel_industries
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
