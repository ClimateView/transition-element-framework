---
title: T-2B6-A-2 - Chlorination of rutile for titanium dioxide production
id: chlorination_of_rutile_for_titanium_dioxide_production
sector: industry
sustainability: red
class: activity
name: chlorination_of_rutile_for_titanium_dioxide_production
version: 2.0.0
operation:
  growthType: false
  variable: start_year_activity_chlorination_of_rutile_for_titanium_dioxide_production
work:
- name: chlorination
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: rutile
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_chlorination_of_rutile_titanium_dioxide_production
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