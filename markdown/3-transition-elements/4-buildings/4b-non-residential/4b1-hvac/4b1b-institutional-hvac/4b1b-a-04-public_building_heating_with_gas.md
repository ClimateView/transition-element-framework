---
title: T-4B1b-A-4 - Public  buildings heated with gas
id: public_building_heating_with_gas
sector: buildings
sustainability: amber
class: activity
version: 2.1.0
progress: 50
name: public_building_heating_with_gas
operation:
  growthType: true
  variable: stock_heating_public_buildings_natural_gas
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_heating_public_buildings_gas
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/m2
    expression: '%[0]'
    variables:
    - energy_intensity_heating_non_residential_public_natural_gas
  input:
  - resource: natural_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_non_residential_public_heating_natural_gas
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_natural_gas_kwh_to_co2e
  - resource: biogas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_non_residential_public_heating_bio_gas
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biogas_kwh_to_co2e
  - resource: hydrogen
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_non_residential_public_heating_hydrogen
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_climate_neutral_hydrogen_kwh_to_co2e
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
