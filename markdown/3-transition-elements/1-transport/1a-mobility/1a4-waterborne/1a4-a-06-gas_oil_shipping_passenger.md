---
title: T-1A4-A-6 - Passenger transport by gas oil ship
id: gas_oil_shipping_passenger
sector: transport
class: activity
name: gas_oil_shipping_passenger
version: 1.0.0
operation:
  growthType: true
  variable: stock_shipping_passenger_gas_oil
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_shipping_passenger_gas_oil
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/person_km
    expression: '%[0]'
    variables:
    - energy_intensity_passenger_gas_oil_sea_transport
  input:
  - resource: marine_gas_oil
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_marine_gas_oil_kwh_to_co2e
---


# Definition
This emission source is defined by the IPCC in {{ ipcc_emission_link() }}.

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

