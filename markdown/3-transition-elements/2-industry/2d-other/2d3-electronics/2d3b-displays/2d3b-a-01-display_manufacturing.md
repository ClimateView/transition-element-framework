---
title: T-2D3b-A-1 - Display manufacturing
id: display_manufacturing
sector: industry
sustainability: amber
class: activity
name: display_manufacturing
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_display_manufacturing
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_display_manufacturing
work:
- name: fugitive
  unitOfMeasure: m2
  operationToWork:
    unitOfMeasure: m2/m2
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_m2
  input:
  - resource: display_raw_materials
    unitOfMeasure: m2
    resourceToWork:
      unitOfMeasure: m2/m2
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/m2
      expression: '%[0]'
      variables:
      - emission_factor_display_manufacturing
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
