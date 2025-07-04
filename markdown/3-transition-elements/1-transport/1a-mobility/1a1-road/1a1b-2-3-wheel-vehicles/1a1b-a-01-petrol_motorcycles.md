---
title: T-1A1b-A-1 - Petrol motorcycles
id: petrol_motorcycles
sector: transport
class: activity
sustainability: red
version: 2.1.0
progress: 80
ipccEmissionSource: 1a3b-road-transportation
name: petrol_motorcycles
operation:
  growthType: true
  variable: stock_motorcycles_petrol
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_motorcycles_petrol
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/vehicle_km
    expression: '%[0]'
    variables:
    - energy_intensity_motorcycles_petrol
  input:
  - resource: ethanol
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_ethanol_motorcycles
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_ethanol_kwh_to_co2e
  - resource: petrol
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_petrol_motorcycles
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_petrol_kwh_to_co2e
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