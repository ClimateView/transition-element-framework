---
title: T-1B1b-A-6 - LNG LGV
id: lng_light_trucks
name: lng_light_trucks
class: activity
sector: transport
sustainability: amber
version: 2.1.0
operation:
  growthType: true
  variable: stock_freight_light_trucks_lng
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_freight_light_trucks_lng
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/vehicle_km
    expression: '%[0]'
    variables:
    - energy_intensity_freight_light_trucks_lng
  input:
  - resource: liquefied_natural_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_lng_light_trucks
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_liquefied_natural_gas_kwh_to_co2e
  - resource: liquefied_bio_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_lbg_light_trucks
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_liquefied_bio_gas_kwh_to_co2e
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
