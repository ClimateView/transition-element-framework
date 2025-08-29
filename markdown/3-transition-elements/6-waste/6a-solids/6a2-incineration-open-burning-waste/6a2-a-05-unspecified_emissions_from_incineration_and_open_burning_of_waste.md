---
title: T-6A2-A-5 - Unspecified emissions from incineration and open burning of waste
id: unspecified_emissions_from_incineration_and_open_burning_of_waste
name: unspecified_emissions_from_incineration_and_open_burning_of_waste
sector: waste
sustainability: red
class: activity
version: 2.2.0
operation:
  growthType: true
  variable: start_year_unspecified_emissions_from_incineration_and_open_burning_of_waste
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_unspecified_emissions_from_incineration_and_open_burning_of_waste
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