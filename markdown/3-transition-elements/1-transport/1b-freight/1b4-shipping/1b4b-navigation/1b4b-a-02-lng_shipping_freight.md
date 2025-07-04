---
title: T-1B4b-A-2 - Liquefied natural gas sea freight
id: lng_shipping_freight
sector: transport
sustainability: amber
class: activity
version: 2.2.0
progress: 50
name: lng_shipping_freight
operation:
  growthType: true
  variable: stock_shipping_freight_lng
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_shipping_freight_lng
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne_km
    expression: '%[0]'
    variables:
    - energy_intensity_freight_lng_sea_transport
  input:
  - resource: liquefied_natural_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_liquefied_natural_gas_shipping_freight
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
    resourceProportion: resource_proportion_liquefied_bio_gas_shipping_freight
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
