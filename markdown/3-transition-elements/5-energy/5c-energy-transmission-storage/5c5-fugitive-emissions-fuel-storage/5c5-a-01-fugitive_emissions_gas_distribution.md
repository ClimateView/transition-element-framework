---
title: T-5C5-A-1 - Fugitive emissions from gas distribution
id: fugitive_emissions_gas_distribution
name: fugitive_emissions_gas_distribution
sector: energy
sustainability: red
class: activity
version: 2.1.0
operation:
  growthType: false
  variable: stock_gas_distributed
work:
- name: fugitive
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_loss_kwh_gas_per_kwh_gas_distributed
  input:
  - resource: methane
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_atmospheric_methane_kwh_to_co2e
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
