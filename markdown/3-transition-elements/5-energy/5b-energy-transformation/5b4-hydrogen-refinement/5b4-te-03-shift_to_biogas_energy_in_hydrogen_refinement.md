---
title: T-5B4-TE-3 - Shift to biogas energy in hydrogen refinement
id: shift_to_biogas_energy_in_hydrogen_refinement
sector: energy
sustainability: green
class: transition
type: shift
longName: 'Shift from natural gas combustion to biogas combustion for hydrogen refinement energy use'
shortName: 'Biogas energy in hydrogen'
name: shift_to_biogas_energy_in_hydrogen_refinement                
version: 2.0.0
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: natural_gas_usage_within_hydrogen_refinement
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: biogas_usage_within_hydrogen_refinement
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
