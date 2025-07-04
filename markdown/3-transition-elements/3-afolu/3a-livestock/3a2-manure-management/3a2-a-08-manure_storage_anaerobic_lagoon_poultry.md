---
title: T-3A2-A-8 - Anaerobic lagoon manure storage for poultry
id: manure_storage_anaerobic_lagoon_poultry
sector: afolu
sustainability: amber
class: activity
name: manure_storage_anaerobic_lagoon_poultry
version: 2.0.0
operation:
  growthType: false
  variable: start_year_activity_manure_storage_anaerobic_lagoon_poultry
work:
- name: unknown
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: poultry_manure
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_manure_storage_anaerobic_lagoon_poultry_tonne_to_co2e_gram
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
