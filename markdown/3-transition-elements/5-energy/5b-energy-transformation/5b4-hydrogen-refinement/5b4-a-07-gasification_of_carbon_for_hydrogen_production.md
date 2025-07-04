---
title: T-5B4-A-7 - Gasification of carbon for hydrogen production
id: gasification_of_carbon_for_hydrogen_production
name: gasification_of_carbon_for_hydrogen_production
sector: energy
sustainability: red
class: activity
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_gasification_of_carbon_for_hydrogen_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_gasification_of_carbon_for_hydrogen_production
work:
- name: gasification
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: coal
    resourceProportion: resource_proportion_coal_gasification_for_hydrogen_production
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_gasification_of_coal_for_hydrogen_production
  - resource: biofuel_solid
    resourceProportion: resource_proportion_biomass_gasification_for_hydrogen_production
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_gasification_of_biomass_for_hydrogen_production
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
