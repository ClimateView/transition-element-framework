---
title: T-3A1-A-3 - Enteric Fermentation from Swine
id: enteric_fermentation_swine
sector: afolu
sustainability: amber
progress: 80
ipccEmissionSource: 3a1h-swine
name: enteric_fermentation_swine
class: activity
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_enteric_fermentation_swine
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_activity_enteric_fermentation_swine
work:
- name: enteric_fermentation
  unitOfMeasure: head
  operationToWork:
    unitOfMeasure: head/head
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_head
  input:
  - resource: swine
    unitOfMeasure: head
    resourceToWork:
      unitOfMeasure: head/head
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/head
      expression: '%[0]'
      variables:
      - emission_factor_enteric_fermentation_swine_head_to_co2e_gram
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