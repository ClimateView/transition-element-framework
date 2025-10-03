---
title: T-2C4-TE-1 - Shift to electricity in magnesium industries
id: shift_to_electricity_in_magnesium_industries
sector: industry
sustainability: green
class: transition
type: shift
name: shift_to_electricity_in_magnesium_industries
version: 2.0.0
shift: shift_to_electricity_in_magnesium_industries
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: coal_usage_within_magnesium_industries
  - chain: oil_usage_within_magnesium_industries
  - chain: natural_gas_usage_within_magnesium_industries
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electricity_usage_within_magnesium_industries
---

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

TBD



# Transition Element

- **Type of shift**: `{{ get_te_shift_type() }}`
- **Activity**: TBD
- **Operation**: TBD
- **ATOC**: TBD


# Activities

{{ get_te_activities() }}


# Parameters

{{ generate_parameter_table() }}


# YAML Specification

```yaml
{{ json_to_yaml() }}
```
