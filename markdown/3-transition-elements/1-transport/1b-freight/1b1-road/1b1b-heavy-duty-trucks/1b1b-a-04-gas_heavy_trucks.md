---
title: T-1B1b-A-4 - Shift to gas heavy trucks
id: gas_heavy_trucks
sector: transport
sustainability: amber
class: activity
version: 2.0.0
progress: 50
name: gas_heavy_trucks
operation:
  growthType: true
  variable: stock_freight_heavy_trucks_gas
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_freight_heavy_trucks_gas
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne_km
    expression: '%[0]'
    variables:
    - energy_intensity_freight_heavy_trucks_gas
  input:
  - resource: biogas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_biogas_heavy_trucks
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biogas_kwh_to_co2e
  - resource: natural_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_natural_gas_heavy_trucks
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_natural_gas_kwh_to_co2e

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
