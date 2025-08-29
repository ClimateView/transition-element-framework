---
title: T-5D1-A-2 - Gas use, non-specified sources
id: gas_use_non_specified_sources
sector: energy
sustainability: amber
class: activity
version: 2.2.0
progress: 50
name: gas_use_non_specified_sources
operation:
  growthType: true
  variable: stock_gas_use_unspecified_sources
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_gas_use_unspecified_sources
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_direct_resource_use_kwh
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