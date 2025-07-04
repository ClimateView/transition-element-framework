---
title: T-1A1b-A-3 - Active travel
id: walking_cycling
sector: transport
class: activity
sustainability: green
version: 2.1.1
progress: 80
ipccEmissionSource: 1a3b-road-transportation
name: walking_cycling
operation:
  growthType: true
  variable: stock_mobility_walking_biking
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_mobility_walking_biking
  primaryStock:
    name: personal_vehicles_bicycle
work:
- name: biomechanics
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/person_km
    expression: '%[0]'
    variables:
    - energy_intensity_walking_biking
  input:
  - resource: metabolic_energy
    unitOfMeasure: joule
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_active_travel
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