---
title: T-1C1-A-2 - Diesel recreational machinery
id: recreational_machinery_diesel
sector: transport
sustainability: red
class: activity
name: recreational_machinery_diesel
version: 2.1.0
operation:
  growthType: true
  variable: stock_recreational_machinery_diesel
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_recreational_machinery_diesel
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_recreational_machinery_diesel
  input:
  - resource: diesel
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_diesel_recreational_machinery
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_diesel_kwh_to_co2e
  - resource: hvo_biodiesel
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_biodiesel_recreational_machinery
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biodiesel_kwh_to_co2e
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