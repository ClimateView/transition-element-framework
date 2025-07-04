---
title: T-1A1a-A-4 - Hydrogen vehicles
id: hydrogen_vehicles
sector: transport
class: activity
sustainability: green
version: 2.1.0
progress: 80
ipccEmissionSource: 1a3b-road-transportation
name: hydrogen_vehicles
operation:
  growthType: true
  variable: stock_personal_vehicles_hydrogen
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_personal_vehicles_hydrogen
work:
- name: hydrogen_oxidation
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/vehicle_km
    expression: '%[0]'
    variables:
    - energy_intensity_personal_vehicles_hydrogen
  input:
  - resource: hydrogen
    unitOfMeasure: kwh
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