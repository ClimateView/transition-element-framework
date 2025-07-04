---
title: T-5A2-A-13 - District heating by heat pump
id: district_heating_heat_pumps
sector: energy
sustainability: green
class: activity
version: 2.0.1
progress: 50
name: district_heating_heat_pumps
operation:
  growthType: false
  variable: stock_district_heating_heatpumps
work:
- name: unknown
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_district_heating_heatpumps
  input:
  - resource: electricity
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_electricity_current
  output:
  - resource: district_heat
    unitOfMeasure: kwh
    workToResource:
      unitOfMeasure: kwh/kwh
      expression: 1 / %[0]
      variables:
      - energy_intensity_district_heating_heatpumps

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
