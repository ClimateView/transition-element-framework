---
title: T-3C3-A-2 - Rice cultivation
id: rice_cultivation
sector: afolu
sustainability: amber
class: activity
name: rice_cultivation
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_rice_cultivation
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_rice_cultivation
work:
- name: unknown
  unitOfMeasure: ha
  operationToWork:
    unitOfMeasure: ha/ha
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_hectare
  input:
  - resource: flooded_rice_land
    unitOfMeasure: ha
    resourceToWork:
      unitOfMeasure: ha/ha
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/ha
      expression: '%[0]'
      variables:
      - emission_factor_rice_cultivation_ha_to_co2e_gram
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