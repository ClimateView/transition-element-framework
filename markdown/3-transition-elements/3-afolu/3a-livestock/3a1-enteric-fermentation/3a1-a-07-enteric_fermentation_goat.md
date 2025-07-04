---
title: T-3A1-A-7 - Enteric fermentation from goats
id: enteric_fermentation_goat
sector: afolu
sustainability: amber
class: activity
name: enteric_fermentation_goat
version: 2.0.0
operation:
  growthType: false
  variable: start_year_activity_enteric_fermentation_goat
work:
- name: enteric_fermentation
  unitOfMeasure: head
  operationToWork:
    unitOfMeasure: head/head
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_head
  input:
  - resource: goat
    unitOfMeasure: head
    resourceToWork:
      unitOfMeasure: head/head
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/head
      expression: '%[0]'
      variables:
      - emission_factor_enteric_fermentation_goat_head_to_co2e_gram
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
