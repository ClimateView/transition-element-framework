---
title: T-6A1-A-3 - Recycling solid waste
id: recycling_of_solid_waste
sector: waste
sustainability: green
class: activity
version: 2.1.0
progress: 50
name: recycling_of_solid_waste
operation:
  growthType: true
  variable: stock_waste_recycling
  growthFactor:
    expression: '%[0]'
    variables:
    - stock_growth_waste_recycling
work:
- name: recycling
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - tonne_recycling_per_tonne_solid_waste_recycled
  input:
  - resource: waste_recycling
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_solid_waste_recycled_tonne_to_co2e
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
