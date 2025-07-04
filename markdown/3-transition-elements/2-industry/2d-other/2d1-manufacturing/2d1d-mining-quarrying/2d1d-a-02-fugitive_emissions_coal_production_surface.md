---
title: T-2D1d-A-2 - Fugitive emissions from coal production (surface mines)
id: fugitive_emissions_coal_production_surface
name: fugitive_emissions_coal_production_surface
sector: industry
sustainability: red
class: activity
version: 2.1.0
operation:
  growthType: false
  variable: stock_coal_produced_surface_mines
work:
- name: fugitive
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne
    expression: '%[0]'
    variables:
    - energy_loss_kwh_gas_per_tonne_coal_produced_surface
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
