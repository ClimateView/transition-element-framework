---
title: T-4C1-A-5 - CNG construction machinery
id: construction_machinery_cng
sector: buildings
sustainability: red
class: activity
name: construction_machinery_cng
version: 2.0.0
operation:
  growthType: false
  variable: stock_construction_machinery_cng
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_construction_machinery_cng
  input:
  - resource: natural_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_cng_construction_machinery
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
    resourceProportion: resource_proportion_cbg_construction_machinery
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
