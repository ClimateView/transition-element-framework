---
title: T-4A1a-A-10 - Residential blocks heated with biomass
id: multi_family_building_heating_with_solid_biofuels
sector: buildings
sustainability: green
class: activity
version: 2.1.0
progress: 50
name: multi_family_building_heating_with_solid_biofuels
operation:
  growthType: false
  variable: stock_heating_residential_multi_family_solid_biofuel
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/m2
    expression: '%[0]'
    variables:
    - energy_intensity_heating_residential_multi_family_buildings_biofuel
  input:
  - resource: biofuel_solid
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biofuel_kwh_to_co2e
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
