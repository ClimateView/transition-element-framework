---
title: T-3C2-A-9 - Pasture manure horse
id: pasture_manure_horse
sector: afolu
sustainability: amber
class: activity
name: pasture_manure_horse
version: 2.0.0
operation:
  growthType: false
  variable: start_year_activity_pasture_manure_horse
work:
- name: fertilising
  unitOfMeasure: tonne_N
  operationToWork:
    unitOfMeasure: tonne_N/tonne_N
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne_N
  input:
  - resource: horse_manure_nitrogen
    unitOfMeasure: tonne_N
    resourceToWork:
      unitOfMeasure: tonne_N/tonne_N
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne_N
      expression: '%[0]'
      variables:
      - emission_factor_pasture_manure_horse_tonne_to_co2e_gram
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
