---
title: T-3C2-A-8 - Crop residue incorporation
id: crop_residue_incorporation
sector: afolu
sustainability: green
class: activity
name: crop_residue_incorporation
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_crop_residue_incorporation
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_crop_residue_incorporation
work:
- name: fertilising
  unitOfMeasure: tonne_N
  operationToWork:
    unitOfMeasure: tonne_N/tonne_N
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne_N
  input:
  - resource: crop_residue_nitrogen
    unitOfMeasure: tonne_N
    resourceToWork:
      unitOfMeasure: tonne_N/tonne_N
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne_N
      expression: '%[0]'
      variables:
      - emission_factor_crop_residue_incorporation_tonne_to_co2e_gram
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