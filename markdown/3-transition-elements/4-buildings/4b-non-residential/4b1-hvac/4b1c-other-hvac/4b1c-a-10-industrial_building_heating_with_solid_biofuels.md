---
title: T-4B1c-A-10 - Industrial buildings heated with biomass
id: industrial_building_heating_with_solid_biofuels
sector: buildings
sustainability: green
class: activity
version: 2.2.0
progress: 50
name: industrial_building_heating_with_solid_biofuels
operation:
  growthType: true
  variable: stock_heating_industrial_solid_biofuel
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_heating_industrial_solid_biofuel
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/m2
    expression: '%[0]'
    variables:
    - energy_intensity_heating_non_residential_industrial_biofuel
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