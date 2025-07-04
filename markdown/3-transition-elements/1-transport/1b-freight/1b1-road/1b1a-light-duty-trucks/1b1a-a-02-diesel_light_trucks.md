---
title: T-1B1a-A-2 - Diesel LGV
id: diesel_light_trucks
sector: transport
sustainability: red
class: activity
version: 2.1.0
progress: 50
name: diesel_light_trucks
operation:
  growthType: true
  variable: stock_freight_light_trucks_diesel
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_freight_light_trucks_diesel
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/vehicle_km
    expression: '%[0]'
    variables:
    - energy_intensity_freight_light_trucks_diesel
  input:
  - resource: hvo_biodiesel
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_biodiesel_light_trucks
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biodiesel_kwh_to_co2e
  - resource: diesel
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_diesel_light_trucks
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_diesel_kwh_to_co2e
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