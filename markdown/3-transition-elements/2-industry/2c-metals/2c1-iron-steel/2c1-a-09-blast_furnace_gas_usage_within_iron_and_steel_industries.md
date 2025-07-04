---
title: T-2C1-A-9 - Blast furnace gas usage within iron and steel industries
id: blast_furnace_gas_usage_within_iron_and_steel_industries
name: blast_furnace_gas_usage_within_iron_and_steel_industries
sector: industry
sustainability: amber
class: activity
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_blast_furnace_gas_usage_within_iron_and_steel_industries
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_blast_furnace_gas_usage_within_iron_and_steel_industries
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_direct_resource_use_kwh
  input:
  - resource: blast_furnace_gas
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_blast_furnace_gas_kwh_to_co2e
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
