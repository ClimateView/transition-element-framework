---
title: T-2C4-TE-2 - Shift to biogas energy in magnesium industries
id: shift_to_biogas_energy_in_magnesium_industries
sector: industry
class: transition
sustainability: green
type: shift
name: shift_to_biogas_energy_in_magnesium_industries
version: 2.0.0
shift: shift_to_biogas_energy_in_magnesium_industries
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: natural_gas_usage_within_magnesium_industries
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: biogas_usage_within_magnesium_industries
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
