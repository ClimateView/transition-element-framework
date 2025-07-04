---
title: T-5A2-A-12 - District heating by geothermal heat
id: district_heating_geothermal_heat
sector: energy
sustainability: green
class: activity
version: 1.1.0
progress: 50
name: district_heating_geothermal_heat
operation:
  growthType: false
  variable: initial_operations_dh_geothermal_heat
work:
- name: unknown
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_dh_geothermal_heat
  input:
  - resource: geothermal_heat
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_geothermal_heat_kwh_to_co2e
  output:
  - resource: district_heat
    unitOfMeasure: kwh
    workToResource:
      unitOfMeasure: kwh/kwh
      expression: 1 / %[0]
      variables:
      - energy_intensity_dh_geothermal_heat
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
