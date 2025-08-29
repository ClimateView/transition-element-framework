---
title: T-3B5a-A-1 - Trees in settlements
id: trees_in_settlements
sector: afolu
class: activity
name: trees_in_settlements
version: 2.0.0
operation:
  growthType: false
  variable: start_year_activity_trees_in_settlements
work:
- name: unknown
  unitOfMeasure: ha
  operationToWork:
    unitOfMeasure: ha/ha
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_hectare
  input:
  - resource: trees_in_settlements
    unitOfMeasure: ha
    resourceToWork:
      unitOfMeasure: ha/ha
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/ha
      expression: '%[0]'
      variables:
      - emission_factor_trees_in_settlements_ha_to_co2e_gram
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

