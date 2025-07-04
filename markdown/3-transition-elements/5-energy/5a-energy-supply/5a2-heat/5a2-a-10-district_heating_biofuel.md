---
title: T-5A2-A-10 - District heating by biofuel
id: district_heating_biofuel
sector: energy
sustainability: green
class: activity
version: 2.1.0
progress: 50
name: district_heating_biofuel
operation:
  growthType: false
  variable: initial_operation_dh_biofuel
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_dh_biofuel
  input:
  - resource: biofuel_solid
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biofuel_kwh_to_co2e
  output:
  - resource: district_heat
    unitOfMeasure: kwh
    workToResource:
      unitOfMeasure: kwh/kwh
      expression: 1 / %[0]
      variables:
      - energy_intensity_dh_biofuel
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
