---
title: T-4A1a-A-5 - Residential blocks with heat pumps
id: multi_family_building_heating_with_heatpump
sector: buildings
sustainability: green
class: activity
version: 2.1.0
progress: 50
name: multi_family_building_heating_with_heatpump
operation:
  growthType: false
  variable: stock_heating_residential_multi_family_heat_pumps
  primaryStock:
    name: heat_pumps_multi_family_buildings
work:
- name: unknown
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/m2
    expression: '%[0]'
    variables:
    - energy_intensity_heating_residential_multi_family_buildings_heat_pumps
  input:
  - resource: electricity
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_electricity_current
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
