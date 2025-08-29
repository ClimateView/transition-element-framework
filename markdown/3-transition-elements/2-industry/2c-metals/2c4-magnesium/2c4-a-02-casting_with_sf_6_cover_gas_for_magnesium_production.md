---
title: T-2C4-A-2 - Casting with SF6 cover gas for magnesium production
id: casting_with_sf_6_cover_gas_for_magnesium_production
sector: industry
sustainability: red
class: activity
name: casting_with_sf_6_cover_gas_for_magnesium_production
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_casting_with_sf_6_cover_gas_for_magnesium_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_casting_with_sf_6_cover_gas_for_magnesium_production
work:
- name: casting
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: sf_6
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_sf_6_cover_gas_magnesium_production
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