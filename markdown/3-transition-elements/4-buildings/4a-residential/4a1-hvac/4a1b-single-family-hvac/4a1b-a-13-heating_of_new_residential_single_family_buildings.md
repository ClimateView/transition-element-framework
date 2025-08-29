---
title: T-4A1b-A-13 - Heating of newly constructed domestic houses
id: heating_of_new_residential_single_family_buildings
sector: buildings
sustainability: green
class: activity
version: 2.2.0
progress: 50
name: heating_of_new_residential_single_family_buildings
operation:
  growthType: true
  variable: stock_heating_new_residential_single_family
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_heating_new_residential_single_family_buildings
work:
- name: unknown
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/m2
    expression: '%[0]'
    variables:
    - energy_intensity_heating_residential_single_family_new_buildings
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