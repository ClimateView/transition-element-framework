---
title: T-2B5-A-1 - Carbothermal reduction of silica for silicon carbide production
id: carbothermal_reduction_of_silica_for_silicon_carbide_production
sector: industry
sustainability: red
class: activity
name: carbothermal_reduction_of_silica_for_silicon_carbide_production
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_carbothermal_reduction_of_silica_for_silicon_carbide_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_carbothermal_reduction_of_silica_for_silicon_carbide_production
work:
- name: reduction
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: silica
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_carbothermal_reduction_of_silica_for_silicon_carbide_production
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