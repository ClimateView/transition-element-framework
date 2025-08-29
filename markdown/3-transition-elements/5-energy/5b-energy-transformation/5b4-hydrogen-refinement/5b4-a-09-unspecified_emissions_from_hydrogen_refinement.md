---
title: T-5B4-A-9 - Unspecified emissions from hydrogen refinement
id: unspecified_emissions_from_hydrogen_refinement
sector: energy
class: activity
name: unspecified_emissions_from_hydrogen_refinement
version: 2.0.0
operation:
  growthType: true
  variable: start_year_activity_unspecified_emissions_from_hydrogen_refinement
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_unspecified_emissions_from_hydrogen_refinement
work:
- name: unknown
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: carbon_dioxide_equivalents
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_co2e_tonne_to_co2e_gram
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

