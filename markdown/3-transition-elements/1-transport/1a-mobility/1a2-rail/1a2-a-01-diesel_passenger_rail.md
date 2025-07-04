---
title: T-1A2-A-1 - Diesel rail passenger transport
id: diesel_passenger_rail
sector: transport
class: activity
sustainability: red
version: 2.2.0
progress: 80
ipccEmissionSource: 1a3c-railways
name: diesel_passenger_rail
operation:
  growthType: true
  variable: stock_passenger_diesel_rail
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_passenger_diesel_rail
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/person_km
    expression: '%[0]'
    variables:
    - energy_intensity_passenger_diesel_rail
  input:
  - resource: diesel
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_diesel_rail_passenger
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
    resourceProportion: resource_proportion_biodiesel_rail_passenger
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