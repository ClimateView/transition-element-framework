---
title: T-2D5-A-17 - Industrial other distillate fuel oil no 6
id: industrial_unregulated_distillate_fuel_oil_no_6_use
sector: industry
sustainability: red
class: activity
name: industrial_unregulated_distillate_fuel_oil_no_6_use
version: 2.1.0
operation:
  growthType: true
  variable: stock_industrial_unregulated_distillate_fuel_oil_no_6_use
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_industrial_unregulated_distillate_fuel_oil_no_6_use
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_direct_resource_use_kwh
  input:
  - resource: distillate_fuel_oil_no_6
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_distillate_fuel_oil_no_6_kwh_to_co2e
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