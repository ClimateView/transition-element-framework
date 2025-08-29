---
title: T-4B1b-A-1 - Public buildings heated with coal
id: public_building_heating_with_coal
sector: buildings
sustainability: red
class: activity
version: 2.2.0
progress: 50
name: public_building_heating_with_coal
operation:
  growthType: true
  variable: stock_heating_public_buildings_coal
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_heating_public_buildings_coal
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/m2
    expression: '%[0]'
    variables:
    - energy_intensity_heating_non_residential_public_coal
  input:
  - resource: coal
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_coal_kwh_to_co2e
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