---
title: T-4B1c-A-7 - Industrial buildings heated with liquefied petrol gas (LPG)
id: industrial_building_heating_with_lpg
sector: buildings
sustainability: red
class: activity
version: 2.1.0
progress: 50
name: industrial_building_heating_with_lpg
operation:
  growthType: false
  variable: stock_heating_industrial_lpg
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/m2
    expression: '%[0]'
    variables:
    - energy_intensity_heating_non_residential_industrial_lpg
  input:
  - resource: liquefied_petroleum_gas
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_liquefied_petroleum_gas
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