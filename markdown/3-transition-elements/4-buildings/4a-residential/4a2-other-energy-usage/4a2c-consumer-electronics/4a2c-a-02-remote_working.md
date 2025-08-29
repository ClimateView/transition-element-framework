---
title: T-4A2c-A-2 - Remote working
id: remote_working
sector: buildings
sustainability: green
class: activity
version: 2.2.0
progress: 50
name: remote_working
operation:
  growthType: true
  variable: stock_remote_working
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_remote_working
work:
- name: unknown
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/h
    expression: '%[0]'
    variables:
    - energy_intensity_remote_working
  input:
  - resource: electricity
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_electricity_current
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