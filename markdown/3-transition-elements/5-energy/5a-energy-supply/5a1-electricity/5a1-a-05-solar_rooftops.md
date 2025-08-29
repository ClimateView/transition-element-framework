---
title: T-5A1-A-5 - Electricity from solar rooftops
id: solar_rooftops
sector: energy
sustainability: green
class: activity
version: 2.1.0
progress: 50
name: solar_rooftops
operation:
  growthType: false
  variable: initial_operation_solar_rooftop
work:
- name: photovoltaic
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_direct_resource_use_kwh
  input:
  - resource: solar_panel_rooftop
    unitOfMeasure: kwp
    resourceToWork:
      unitOfMeasure: kwp/kwh
      expression: '%[0]'
      variables:
      - stock_per_work_coefficient_solar_rooftop
    emissionFactor:
      unitOfMeasure: g_co2e/kwp/year
      expression: '%[0]'
      variables:
      - emission_factor_solar_panel_rooftop_production
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