---
title: T-6B1-A-6 - Aerobic treatment - nitrification/denitrification
id: aerobic_treatment_nitrification_denitrification
sector: waste
sustainability: amber
class: activity
name: aerobic_treatment_nitrification_denitrification
version: 2.0.0
chains: null
operation:
  growthType: false
  variable: start_year_activity_aerobic_treatment_nitrification_denitrification
work:
- name: nitrification_denitrification
  unitOfMeasure: kg_N
  operationToWork:
    unitOfMeasure: kg_N/kg_N
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_kg_N
  input:
  - resource: ammoniacal_nitrogen
    unitOfMeasure: kg_N
    resourceToWork:
      unitOfMeasure: kg_N/kg_N
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kg_N
      expression: '%[0]'
      variables:
      - emission_factor_nitrification_denitrification_in_aerobic_treatment
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
