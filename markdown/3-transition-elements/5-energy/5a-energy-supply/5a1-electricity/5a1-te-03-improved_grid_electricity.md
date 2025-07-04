---
title: T-5A1-TE-3 - Improved Grid Electricity
id: improved_grid_electricity
sector: energy
sustainability: amber
progress: 10
class: transition
version: 2.0.0
name: improved_grid_electricity
type: shift
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: grid_current
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: grid_future

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Reduced climate impact from electricity delivered via the grid. Used to calculate emission reductions related to reduced emissions from electricity production outside the system limit.



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
