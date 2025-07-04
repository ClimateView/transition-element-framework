---
title: T-5A3-A-4 - CHP landfill gas production
id: chp_landfill_gas
sector: energy
sustainability: amber
class: activity
version: 2.1.0
progress: 50
name: chp_landfill_gas
operation:
  growthType: false
  variable: stock_chp_landfill_gas
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: 1 / ( %[0] + %[1] )
    variables:
    - energy_efficiency_chp_landfill_gas_to_district_heat
    - energy_efficiency_chp_landfill_gas_to_electricity
  input:
  - resource: landfill_gas
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_landfill_gas_kwh_to_co2e
  output:
  - resource: district_heat
    primary: true
    unitOfMeasure: kwh
    workToResource:
      unitOfMeasure: kwh/kwh
      expression: '%[0]'
      variables:
      - energy_efficiency_chp_landfill_gas_to_district_heat
  - resource: electricity
    unitOfMeasure: kwh
    workToResource:
      unitOfMeasure: kwh/kwh
      expression: '%[0]'
      variables:
      - energy_efficiency_chp_landfill_gas_to_electricity
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
