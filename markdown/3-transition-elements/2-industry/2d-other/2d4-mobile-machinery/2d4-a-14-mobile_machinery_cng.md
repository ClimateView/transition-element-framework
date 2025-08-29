---
title: T-2D4-A-14 - CNG other mobile machinery
id: mobile_machinery_cng
sector: industry
class: activity
name: mobile_machinery_cng
version: 2.0.0
operation:
  growthType: true
  variable: stock_non_road_mobile_machinery_cng
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_non_road_mobile_machinery_cng
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_machinery_cng
  input:
  - resource: natural_gas
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_natural_gas_kwh_to_co2e
---


# Definition
This emission source is defined by the IPCC in {{ ipcc_emission_link() }}.

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

