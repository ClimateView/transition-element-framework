---
title: T-6B1-A-1 - Wastewater treatment and discharge
id: wastewater_treatment_and_discharge
sector: waste
sustainability: amber
class: activity
version: 2.1.0
progress: 50
name: wastewater_treatment_and_discharge
operation:
  growthType: true
  variable: stock_m3_domestic_wastewater_treated
  growthFactor:
    expression: '%[0]'
    variables:
    - stock_growth_m3_domestic_wastewater_treated
work:
- name: wastewater_treatment
  unitOfMeasure: m3
  operationToWork:
    unitOfMeasure: m3/m3
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_m3
  input:
  - resource: domestic_wastewater
    unitOfMeasure: m3
    resourceToWork:
      unitOfMeasure: m3/m3
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/m3
      expression: '%[0]'
      variables:
      - emission_wastewater_treatment_m3_to_co2e
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
