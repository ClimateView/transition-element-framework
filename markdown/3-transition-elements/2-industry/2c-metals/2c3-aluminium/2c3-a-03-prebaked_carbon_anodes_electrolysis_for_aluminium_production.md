---
title: T-2C3-A-3 - Electrolysis of prebaked carbon anodes for aluminium production
id: prebaked_carbon_anodes_electrolysis_for_aluminium_production
name: prebaked_carbon_anodes_electrolysis_for_aluminium_production
sector: industry
sustainability: red
class: activity
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_prebaked_carbon_anodes_electrolysis_for_aluminium_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_prebaked_carbon_anodes_electrolysis_for_aluminium_production
work:
- name: electrolysis
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: prebaked_carbon_anodes
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_prebaked_carbon_anodes_electrolysis_aluminium_production
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
