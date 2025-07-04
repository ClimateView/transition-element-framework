---
title: T-1B3-A-2 - Freight air transport
id: freight_transportation_by_air
sector: transport
sustainability: red
class: activity
name: freight_transportation_by_air
version: 2.1.0
operation:
  growthType: false
  variable: stock_air_freight_transport
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne_km
    expression: '%[0]'
    variables:
    - energy_intensity_air_freight_transportation
  input:
  - resource: aviation_biofuel
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_freight_aviation_biofuel
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_aviation_biofuel_kwh_to_co2e
  - resource: aviation_turbine_fuel
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_freight_aviation_turbine_fuel
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_aviation_turbine_fuel_kwh_to_co2e
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