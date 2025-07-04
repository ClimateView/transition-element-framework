---
title: T-5A7-A-6 - Fugitive emissions from abandoned coal mines
id: fugitive_emissions_abandoned_coal_mines
sector: energy
sustainability: red
class: activity
version: 2.0.0
progress: 50
name: fugitive_emissions_abandoned_coal_mines
operation:
  growthType: false
  variable: stock_emissions_abandoned_coal_mines
work:
- name: fugitive
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne
    expression: '%[0]'
    variables:
    - energy_content_kwh_natural_gas_per_tonne_natural_gas
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