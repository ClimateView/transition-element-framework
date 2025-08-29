---
title: T-1B3-A-1 - Electric freight air transport
id: electric_freight_transportation_by_air
name: electric_freight_transportation_by_air
sector: transport
sustainability: green
class: activity
version: 2.2.0
operation:
  growthType: true
  variable: stock_air_freight_transport_electric
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_air_freight_transport_electric
work:
- name: electromagnetism
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne_km
    expression: '%[0]'
    variables:
    - energy_intensity_air_freight_transportation_electric
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