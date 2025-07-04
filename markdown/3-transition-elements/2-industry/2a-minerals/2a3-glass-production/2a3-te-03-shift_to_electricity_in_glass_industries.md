---
title: T-2A3-TE-3 - Shift to electricity in glass industries
id: shift_to_electricity_in_glass_industries
sector: industry
sustainability: green
class: transition
type: shift
longName: 'Shift from coal, oil and natural gas combustion to electricity for glass industries energy use'
shortName: 'Electricity in glass'
name: shift_to_electricity_in_glass_industries                
version: 2.0.0
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: coal_usage_within_glass_industries
  - chain: oil_usage_within_glass_industries
  - chain: natural_gas_usage_within_glass_industries
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electricity_usage_within_glass_industries
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
