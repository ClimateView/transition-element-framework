---
title: T-5B1-A-5 - Emissions from venting in oil and gas production (WTT)
id: venting_gas_and_oil_production_wtt
name: venting_gas_and_oil_production_wtt
sector: energy
sustainability: red
class: activity
version: 2.0.0
operation:
  growthType: false
  variable: stock_gas_vented_wtt
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


