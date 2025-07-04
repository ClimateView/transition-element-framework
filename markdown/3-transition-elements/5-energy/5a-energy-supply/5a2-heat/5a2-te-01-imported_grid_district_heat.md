---
title: T-5A2-TE-1 - District heat from imported grid
id: imported_grid_district_heat
sector: energy
sustainability: amber
progress: 10
class: transition
version: 2.0.0
name: imported_grid_district_heat
type: supplyAlteration
longName: 'Alter the amount of heat imported by district heat grid'
shortName: 'Imported district heat'
description: 'Alter the amount of district heat produced by imported grid district heat'
unitOfMeasure: kwh
cohort:
  expression: '1'
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: imported_grid_district_heat

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
