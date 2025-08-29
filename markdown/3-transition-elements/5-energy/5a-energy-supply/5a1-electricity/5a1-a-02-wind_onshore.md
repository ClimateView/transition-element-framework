---
title: T-5A1-A-2 - Electricity from wind onshore
id: wind_onshore
sector: energy
sustainability: green
class: activity
version: 2.1.0
progress: 50
name: wind_onshore
operation:
  growthType: false
  variable: initial_operation_wind_onshore
work:
- name: wind_power
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_direct_resource_use_kwh
  input:
  - resource: wind_onshore
    unitOfMeasure: kw
    resourceToWork:
      unitOfMeasure: kw/kwh
      expression: '%[0]'
      variables:
      - stock_per_work_coefficient_wind_onshore
    emissionFactor:
      unitOfMeasure: g_co2e/kw/year
      expression: '%[0]'
      variables:
      - emission_factor_wind_onshore_production
  output:
  - resource: electricity
    unitOfMeasure: kwh
    workToResource:
      unitOfMeasure: kwh/kwh
      expression: '1'
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