---
title: T-2C3-TE-1 - Shift to inert anodes in aluminium industries
id: shift_to_inert_anodes_in_aluminium_industries
sector: industry
sustainability: green
class: transition
type: shift
longName: 'Shift from carbon anodes to inert anodes in aluminium industries'
shortName: 'Inert anodes in aluminium'
name: shift_to_inert_anodes_in_aluminium_industries                
version: 2.0.0
unitOfMeasure: tonne
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: prebaked_carbon_anodes_electrolysis_for_aluminium_production
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electrolysis_of_inert_anodes_for_aluminium_production
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
