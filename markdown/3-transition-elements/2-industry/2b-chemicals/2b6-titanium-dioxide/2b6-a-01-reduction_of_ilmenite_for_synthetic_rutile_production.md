---
title: T-2B6-A-1 - Reduction of ilmenite for synthetic rutile production
id: reduction_of_ilmenite_for_synthetic_rutile_production
sector: industry
sustainability: red
class: activity
name: reduction_of_ilmenite_for_synthetic_rutile_production
version: 2.0.0
operation:
  growthType: false
  variable: start_year_activity_reduction_of_ilmenite_for_synthetic_rutile_production
work:
- name: reduction
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: ilmenite
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_reduction_of_ilmenite_synthetic_rutile_production
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