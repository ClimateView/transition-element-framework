---
title: T-5B1-TE-1 - Shift to biomass energy in petroleum refinement
id: shift_to_biomass_energy_in_petroleum_refinement
sector: energy
sustainability: amber
class: transition
type: shift
longName: 'Shift from coal combustion to biomass combustion for petroleum refinement energy use'
shortName: 'Biomass energy in petroleum'
name: shift_to_biomass_energy_in_petroleum_refinement                
version: 2.0.0
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: crude_oil_usage_within_petroleum_refinement
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: biomass_usage_within_petroleum_refinement
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
