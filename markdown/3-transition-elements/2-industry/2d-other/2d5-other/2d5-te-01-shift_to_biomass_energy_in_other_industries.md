---
title: T-2D5-TE-1 - Shift to biomass energy in other industries
id: shift_to_biomass_energy_in_other_industries
sector: industry
sustainability: green
class: transition
type: shift
name: shift_to_biomass_energy_in_other_industries
version: 2.0.0
shift: shift_to_biomass_energy_in_other_industries
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: industrial_unregulated_coal_use
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: industrial_unregulated_biomass_use
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
