---
title: T-4C1-A-4 - Low-carbon construction of commercial buildings
id: non_residential_commercial_low_carbon_construction
sector: buildings
sustainability: green
class: activity
version: 2.2.0
progress: 50
name: non_residential_commercial_low_carbon_construction
operation:
  growthType: true
  variable: stock_construction_low_carbon_non_residential_commercial
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_construction_non_residential_commercial_low_carbon
work:
- name: construction
  unitOfMeasure: m2
  operationToWork:
    unitOfMeasure: m2/m2
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_m2
  input:
  - resource: timber_construction
    unitOfMeasure: m2
    resourceToWork:
      unitOfMeasure: m2/m2
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/m2
      expression: '%[0]'
      variables:
      - emission_factor_low_carbon_construction
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
