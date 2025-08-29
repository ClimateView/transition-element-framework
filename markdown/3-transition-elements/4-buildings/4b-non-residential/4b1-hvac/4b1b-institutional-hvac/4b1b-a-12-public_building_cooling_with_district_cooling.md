---
title: T-4B1b-A-12 - Public buildings cooled with district cooling
id: public_building_cooling_with_district_cooling
sector: buildings
sustainability: green
class: activity
version: 2.2.0
progress: 50
name: public_building_cooling_with_district_cooling
operation:
  growthType: true
  variable: stock_cooling_public_district_cooling
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_cooling_public_district_cooling
work:
- name: unknown
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/m2
    expression: '%[0]'
    variables:
    - energy_intensity_cooling_non_residential_public_district_cooling
  input:
  - resource: district_cold
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_district_cooling_kwh_to_co2e
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