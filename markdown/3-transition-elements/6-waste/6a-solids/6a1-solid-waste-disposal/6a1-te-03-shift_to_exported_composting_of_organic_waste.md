---
title: T-6A1-TE-3 - Shift to exported composting of organic waste
id: shift_to_exported_composting_of_organic_waste
sector: waste
sustainability: green
class: transition
type: shift
longName: 'Shift from landfilling organic waste to exported composting of organic waste'
shortName: 'Exported composting of organic waste'
description: 'Shift tonne from solid waste disposal in landfills to exported composting of organic waste in tonne to fulfill the need of waste handling'
name: shift_to_exported_composting_of_organic_waste                
version: 2.0.0
shift: shift_to_exported_composting_of_organic_waste
unitOfMeasure: tonne
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: solid_waste_disposal_in_landfills_and_open_dumps_etc
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: waste_exported_for_composting
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
