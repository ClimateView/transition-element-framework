---
title: T-2C5-TE-1 - Shift to biogas energy in lead industries
id: shift_to_biogas_energy_in_lead_industries
sector: industry
sustainability: green
class: transition
type: shift
name: shift_to_biogas_energy_in_lead_industries
version: 2.0.0
shift: shift_to_biogas_energy_in_lead_industries
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: natural_gas_usage_within_lead_industries
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: biogas_usage_within_lead_industries
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
