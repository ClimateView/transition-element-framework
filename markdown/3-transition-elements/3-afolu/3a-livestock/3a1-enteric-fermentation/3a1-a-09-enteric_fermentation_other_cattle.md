---
title: T-3A1-A-9 - Enteric fermentation from other cattle
id: enteric_fermentation_other_cattle
sector: afolu
sustainability: red
class: activity
name: enteric_fermentation_other_cattle
version: 2.0.0
operation:
  growthType: false
  variable: start_year_activity_enteric_fermentation_other_cattle
work:
- name: enteric_fermentation
  unitOfMeasure: head
  operationToWork:
    unitOfMeasure: head/head
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_head
  input:
  - resource: other_cattle
    unitOfMeasure: head
    resourceToWork:
      unitOfMeasure: head/head
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/head
      expression: '%[0]'
      variables:
      - emission_factor_enteric_fermentation_other_cattle_head_to_co2e_gram
---
# Definition
This emission source is defined by the IPCC in {{ ipcc_emission_link() }}.


{{ activity_sustainability() }}

# Transition Elements

This activity has the following mitigation options modelled as transition elements:

{{ transition_element_list() }}

# Activity Model
This emission source is modelled with {{ generate_work_link() }} as:

{{ activity_model() }}

## Parameters

{{ generate_parameter_table() }}

# YAML Specification

```yaml
{{ json_to_yaml() }}
```
