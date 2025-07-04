---
title: T-2C4-A-3 - Calcination of magnesite for magnesium production
id: calcination_of_magnesite_for_magnesium_production
sector: industry
sustainability: amber
class: activity
name: calcination_of_magnesite_for_magnesium_production
version: 2.0.0
operation:
  growthType: false
  variable: start_year_activity_calcination_of_magnesite_for_magnesium_production
work:
- name: calcination
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: magnesite
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_magnesite_calcination_magnesium_production
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
