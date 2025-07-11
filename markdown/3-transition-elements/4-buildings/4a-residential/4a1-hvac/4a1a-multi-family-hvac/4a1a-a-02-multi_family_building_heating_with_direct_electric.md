---
title: T-4A1a-A-2 - Residential blocks heated with electric heating
id: multi_family_building_heating_with_direct_electric
sector: buildings
sustainability: amber
class: activity
version: 2.1.0
progress: 50
name: multi_family_building_heating_with_direct_electric
operation:
  growthType: true
  variable: stock_heating_residential_multi_family_direct_electricity
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_heating_residential_multi_family_direct_electricity
  primaryStock:
    name: electric_boiler_multi_family_buildings
work:
- name: unknown
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/m2
    expression: '%[0]'
    variables:
    - energy_intensity_heating_residential_multi_family_buildings_direct_electricity
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
