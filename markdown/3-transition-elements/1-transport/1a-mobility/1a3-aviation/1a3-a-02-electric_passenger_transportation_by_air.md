---
title: T-1A3-A-2 - Electric passenger air transport
id: electric_passenger_transportation_by_air
sector: transport
class: activity
sustainability: green
version: 2.1.0
progress: 80
ipccEmissionSource: 1a3a-civil-aviation
name: electric_passenger_transportation_by_air
operation:
  growthType: true
  variable: stock_passenger_air_transport_electric
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_passenger_air_transport_electric
work:
- name: electromagnetism
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/person_km
    expression: '%[0]'
    variables:
    - energy_intensity_air_passenger_transportation_electric
  input:
  - resource: electricity
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_electricity_current
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