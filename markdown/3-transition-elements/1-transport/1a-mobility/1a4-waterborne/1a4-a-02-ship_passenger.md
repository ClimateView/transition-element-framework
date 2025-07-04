---
title: T-1A4-A-2 - Passenger transport by boat
id: ship_passenger
sector: transport
class: activity
sustainability: red
version: 2.1.0
progress: 80
ipccEmissionSource: 1a3d-water-borne-navigation
name: ship_passenger
operation:
  growthType: true
  variable: stock_passenger_ships
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_passenger_ships
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/person_km
    expression: '%[0]'
    variables:
    - energy_intensity_passenger_sea_transport
  input:
  - resource: marine_diesel
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_passenger_shipping_marine_diesel
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_marine_diesel_kwh_to_co2e
  - resource: marine_biodiesel
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_passenger_shipping_marine_biodiesel
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_marine_biodiesel_kwh_to_co2e
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
