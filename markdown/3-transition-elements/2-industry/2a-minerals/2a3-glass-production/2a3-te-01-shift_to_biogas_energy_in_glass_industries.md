---
title: T-2A3-TE-1 - Shift to biogas energy in glass industries
id: shift_to_biogas_energy_in_glass_industries
sector: industry
sustainability: green
class: transition
type: shift
longName: 'Shift from natural gas combustion to biogas combustion for glass industries energy use'
shortName: 'Biogas energy in glass'
name: shift_to_biogas_energy_in_glass_industries                
version: 2.0.0
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: natural_gas_usage_within_glass_industries
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: biogas_usage_within_glass_industries
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
