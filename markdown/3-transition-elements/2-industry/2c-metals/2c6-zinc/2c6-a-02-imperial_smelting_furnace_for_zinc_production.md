---
title: T-2C6-A-2 - Imperial smelting furnace for zinc production
id: imperial_smelting_furnace_for_zinc_production
sector: industry
sustainability: red
class: activity
name: imperial_smelting_furnace_for_zinc_production
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_imperial_smelting_furnace_for_zinc_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_imperial_smelting_furnace_for_zinc_production
work:
- name: smelting
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: zinc_concentrate
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_imperial_smelting_furnace_for_zinc_production
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