---
title: T-5A3-A-8 - CHP biogas production
id: chp_biogas
sector: energy
sustainability: green
class: activity
version: 2.1.0
progress: 50
name: chp_biogas
operation:
  growthType: false
  variable: stock_chp_biogas
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: 1 / ( %[0] + %[1] )
    variables:
    - energy_efficiency_chp_biogas_to_district_heat
    - energy_efficiency_chp_biogas_to_electricity
  input:
  - resource: biogas
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biogas_kwh_to_co2e
  output:
  - resource: district_heat
    primary: true
    unitOfMeasure: kwh
    workToResource:
      unitOfMeasure: kwh/kwh
      expression: '%[0]'
      variables:
      - energy_efficiency_chp_biogas_to_district_heat
  - resource: electricity
    unitOfMeasure: kwh
    workToResource:
      unitOfMeasure: kwh/kwh
      expression: '%[0]'
      variables:
      - energy_efficiency_chp_biogas_to_electricity
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
