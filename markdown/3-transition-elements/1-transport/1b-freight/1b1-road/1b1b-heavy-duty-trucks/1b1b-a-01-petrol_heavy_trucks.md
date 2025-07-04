---
title: T-1B1b-A-1 - Petrol HGV
id: petrol_heavy_trucks
sector: transport
sustainability: red
class: activity
version: 2.2.0
progress: 50
name: petrol_heavy_trucks
operation:
  growthType: true
  variable: stock_freight_heavy_trucks_petrol
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_freight_heavy_trucks_petrol
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne_km
    expression: '%[0]'
    variables:
    - energy_intensity_freight_heavy_trucks_petrol
  input:
  - resource: petrol
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_petrol_heavy_trucks
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_petrol_kwh_to_co2e
  - resource: ethanol
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_ethanol_heavy_trucks
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_ethanol_kwh_to_co2e
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