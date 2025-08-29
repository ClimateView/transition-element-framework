---
title: T-1C1-A-4 - Petrol recreational machinery
id: recreational_machinery_petrol
sector: transport
sustainability: red
class: activity
name: recreational_machinery_petrol
version: 2.1.0
operation:
  growthType: true
  variable: stock_recreational_machinery_petrol
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_recreational_machinery_petrol
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_recreational_machinery_petrol
  input:
  - resource: petrol
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_petrol_recreational_machinery
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_petrol_kwh_to_co2e
  - resource: ethanol
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_ethanol_recreational_machinery
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_ethanol_kwh_to_co2e
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