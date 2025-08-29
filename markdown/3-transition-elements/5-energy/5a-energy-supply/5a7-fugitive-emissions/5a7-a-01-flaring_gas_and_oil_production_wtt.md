---
title: T-5A7-A-1 - Emissions from flaring in oil and gas production (WTT)
id: flaring_gas_and_oil_production_wtt
sector: energy
sustainability: red
class: activity
version: 2.2.0
progress: 50
name: flaring_gas_and_oil_production_wtt
operation:
  growthType: true
  variable: stock_gas_flared_oil_and_gas_production_wtt
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_gas_flared_oil_and_gas_production_wtt
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne
    expression: '%[0]'
    variables:
    - energy_content_kwh_natural_gas_per_tonne_natural_gas
  input:
  - resource: natural_gas
    unitOfMeasure: kwh
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