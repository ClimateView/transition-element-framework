---
title: T-5B4-A-6 - Electrolysis of water for hydrogen production
id: electrolysis_of_water_for_hydrogen_production
name: electrolysis_of_water_for_hydrogen_production
sector: energy
sustainability: green
class: activity
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_electrolysis_of_water_for_hydrogen_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_electrolysis_of_water_for_hydrogen_production
work:
- name: electrolysis
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne
    expression: '%[0]'
    variables:
    - energy_intensity_electrolysis_of_water_for_hydrogen_production
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
