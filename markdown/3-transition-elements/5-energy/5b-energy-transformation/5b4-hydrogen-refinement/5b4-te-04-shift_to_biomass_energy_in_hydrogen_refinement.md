---
title: T-5B4-TE-4 - Shift to biomass energy in hydrogen refinement
id: shift_to_biomass_energy_in_hydrogen_refinement
sector: energy
sustainability: green
class: transition
type: shift
longName: 'Shift from coal combustion to biomass combustion for hydrogen refinement energy use'
shortName: 'Biomass energy in hydrogen'
name: shift_to_biomass_energy_in_hydrogen_refinement                
version: 2.0.0
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: coal_usage_within_hydrogen_refinement
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: biomass_usage_within_hydrogen_refinement
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
