---
title: T-2B9-TE-4 - Shift to hydrogen energy in chemical industries
id: shift_to_hydrogen_energy_in_chemical_industries
sector: industry
sustainability: green
class: transition
type: shift
longName: 'Shift from natural gas combustion to hydrogen combustion for chemical industries energy use'
shortName: 'Hydrogen energy in chemical'
name: shift_to_hydrogen_energy_in_chemical_industries                
version: 2.0.0
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: natural_gas_usage_within_chemical_industries
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: hydrogen_usage_within_chemical_industries
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
