---
title: T-2D1J-A-13 - Asphalt production with natural gas
id: asphalt_production_with_natural_gas
sector: industry
sustainability: amber
class: activity
name: asphalt_production_with_natural_gas
version: 2.0.0
operation:
  growthType: true
  variable: start_year_activity_asphalt_production_with_natural_gas
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_asphalt_production_with_natural_gas
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/tonne
    expression: '%[0]'
    variables:
    - energy_intensity_asphalt_production_with_natural_gas
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

