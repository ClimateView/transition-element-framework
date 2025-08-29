---
title: T-6B1-A-4 - Anaerobic decomposition in a lagoon
id: lagoon_anaerobic_decomposition
sector: waste
sustainability: red
class: activity
name: lagoon_anaerobic_decomposition
version: 2.1.0
chains: null
operation:
  growthType: true
  variable: start_year_activity_lagoon_anaerobic_decomposition
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_lagoon_anaerobic_decomposition
work:
- name: anaerobic_decomposition
  unitOfMeasure: kg_BOD
  operationToWork:
    unitOfMeasure: kg_BOD/kg_BOD
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_kg_BOD
  input:
  - resource: organic_matter
    unitOfMeasure: kg_BOD
    resourceToWork:
      unitOfMeasure: kg_BOD/kg_BOD
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kg_BOD
      expression: '%[0]'
      variables:
      - emission_factor_anaerobic_decomposition_in_lagoon
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