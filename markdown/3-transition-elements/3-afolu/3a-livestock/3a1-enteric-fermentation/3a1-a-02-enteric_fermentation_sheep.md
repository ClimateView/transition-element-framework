---
title: T-3A1-A-2 - Enteric Fermentation from Sheep
id: enteric_fermentation_sheep
sector: afolu
sustainability: red
progress: 80
ipccEmissionSource: 3a1c-sheep
name: enteric_fermentation_sheep
class: activity
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_enteric_fermentation_sheep
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_enteric_fermentation_sheep
work:
- name: enteric_fermentation
  unitOfMeasure: head
  operationToWork:
    unitOfMeasure: head/head
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_head
  input:
  - resource: sheep
    unitOfMeasure: head
    resourceToWork:
      unitOfMeasure: head/head
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/head
      expression: '%[0]'
      variables:
      - emission_factor_enteric_fermentation_sheep_head_to_co2e_gram
---
# Definition
This emission source is defined by the IPCC in {{ ipcc_emission_link() }}.


{{ activity_sustainability() }}

# Transition Elements

This activity has the following mitigation options modelled as transition elements:

{{ transition_element_list() }}

# Activity Model
This emission source is modelled with [Enteric Fermentation](/5-resources/5-about/work-types.md#enteric-fermentation) as:

*TBD*.

## Parameters

{{ generate_parameter_table() }}

# YAML Specification

```yaml
{{ json_to_yaml() }}
```