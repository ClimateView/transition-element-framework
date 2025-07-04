---
title: T-6A1-TE-1 - Shift to recycling of solid waste
id: increased_recycling
sector: waste
sustainability: green
progress: 25
class: transition
version: 2.0.0
name: increased_recycling
type: shift
longName: 'Shift from disposal and incineration to recycling of solid waste.'
shortName: 'Recycling waste'
description: 'Shift tonne from solid waste disposal in landfills and open dumps, incineration and open burning of waste to recycling of solid waste in tonne to fulfill the need of waste handling'
unitOfMeasure: tonne
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: solid_waste_disposal_in_landfills_and_open_dumps_etc
  - chain: incineration_and_open_burning_of_waste
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: recycling_of_solid_waste

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Increased recycling facilitates climate change both directly, by saving energy and reducing greenhouse gas emissions from raw material production, and indirectly by retaining rare and important climate change raw materials in society's cycles.

Recycling helps reduce the amount of waste, which in turn reduces greenhouse gas emissions at landfills and waste incineration plants. 


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
