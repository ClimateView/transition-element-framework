---
title: T-4B2c-A-6 - Commercial other electricity use
id: commercial_unregulated_electricity_use
sector: buildings
sustainability: green
class: activity
version: 2.3.0
progress: 50
name: commercial_unregulated_electricity_use
operation:
  growthType: true
  variable: stock_commercial_unregulated_electricity_use
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_commercial_unregulated_electricity_use
work:
- name: electromagnetism
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_commercial_unregulated_electricity_use
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