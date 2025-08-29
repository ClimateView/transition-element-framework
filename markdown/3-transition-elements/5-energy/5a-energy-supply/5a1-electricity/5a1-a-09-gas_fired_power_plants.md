---
title: T-5A1-A-9 - Gas fired power plant
id: gas_fired_power_plants
sector: energy
sustainability: amber
class: activity
version: 2.1.0
progress: 50
name: gas_fired_power_plants
operation:
  growthType: false
  variable: initial_operation_gas_fired_power_plants
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_direct_resource_use_kwh
  input:
  - resource: biogas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_pp_biogas
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '%[0]'
      variables:
      - work_intensity_electricity_generation_gas
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biogas_kwh_to_co2e
  - resource: landfill_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_pp_landfill_gas
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '%[0]'
      variables:
      - work_intensity_electricity_generation_gas
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_landfill_gas_kwh_to_co2e
  - resource: natural_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_pp_natural_gas
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '%[0]'
      variables:
      - work_intensity_electricity_generation_gas
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_natural_gas_kwh_to_co2e
  output:
  - resource: electricity
    unitOfMeasure: kwh
    workToResource:
      unitOfMeasure: kwh/kwh
      expression: '1'
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