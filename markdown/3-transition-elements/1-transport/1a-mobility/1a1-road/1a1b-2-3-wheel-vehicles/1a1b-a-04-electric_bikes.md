---
title: T-1A1b-A-4 - Electric bikes
id: electric_bikes
sector: transport
class: activity
sustainability: green
version: 2.1.0
progress: 80
ipccEmissionSource: 1a3b-road-transportation
name: electric_bikes
operation:
  growthType: true
  variable: stock_electric_bikes
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_electric_bikes
work:
- name: electromagnetism
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/vehicle_km
    expression: '%[0]'
    variables:
    - energy_intensity_electric_bikes
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
