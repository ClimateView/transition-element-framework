---
title: T-2C1-A-5 - Electric arc furnace for steel production
id: electric_arc_furnace_for_steel_production
name: electric_arc_furnace_for_steel_production
sector: industry
sustainability: green
class: activity
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_electric_arc_furnace_for_steel_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_electric_arc_furnace_for_steel_production
work:
- name: oxidation
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: electric_arc_furnace_raw_material_mix
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_electric_arc_furnace_for_steel_production
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
