---
title: T-3C6-A-16 - CNG agricultural machinery
id: agricultural_machinery_cng
sector: afolu
sustainability: amber
class: activity
name: agricultural_machinery_cng
version: 2.1.0
operation:
  growthType: true
  variable: stock_agricultural_machinery_cng
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_agricultural_machinery_cng
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_agricultural_machinery_cng
  input:
  - resource: natural_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_cng_agricultural_machinery
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_natural_gas_kwh_to_co2e
  - resource: biogas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_cbg_agricultural_machinery
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biogas_kwh_to_co2e
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