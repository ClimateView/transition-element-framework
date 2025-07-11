---
title: T-1A2-A-3 - Hydrogen passenger rail
id: hydrogen_passenger_rail
sector: transport
class: activity
sustainability: green
version: 2.1.0
progress: 80
ipccEmissionSource: 1a3c-railways
name: hydrogen_passenger_rail
operation:
  growthType: false
  variable: stock_passenger_hydrogen_rail
work:
- name: hydrogen_oxidation
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/person_km
    expression: '%[0]'
    variables:
    - energy_intensity_passenger_hydrogen_railway
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