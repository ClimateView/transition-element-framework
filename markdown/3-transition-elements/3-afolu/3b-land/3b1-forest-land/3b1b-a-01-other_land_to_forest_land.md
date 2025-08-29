---
title: T-3B1b-A-1 - Other land converted to forest land
id: other_land_to_forest_land
sector: afolu
class: activity
name: other_land_to_forest_land
version: 2.0.0
operation:
  growthType: false
  variable: start_year_other_land_to_forest_land
work:
- name: unknown
  unitOfMeasure: ha
  operationToWork:
    unitOfMeasure: ha/ha
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_hectare
  input:
  - resource: other_land
    unitOfMeasure: ha
    resourceToWork:
      unitOfMeasure: ha/ha
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/ha
      expression: '%[0]'
      variables:
      - emission_factor_other_land_to_forest_land_ha_to_co2e_gram
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

