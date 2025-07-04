---
title: T-2D3C-A-1 - Photovoltaic cell manufacturing
id: photovoltaic_cell_manufacturing
sector: industry
sustainability: green
class: activity
name: photovoltaic_cell_manufacturing
version: 2.0.0
operation:
  growthType: false
  variable: start_year_activity_photovoltaic_cell_manufacturing
work:
- name: fugitive
  unitOfMeasure: m2
  operationToWork:
    unitOfMeasure: m2/m2
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_m2
  input:
  - resource: photovoltaic_cell_raw_materials
    unitOfMeasure: m2
    resourceToWork:
      unitOfMeasure: m2/m2
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/m2
      expression: '%[0]'
      variables:
      - emission_factor_photovoltaic_cell_manufacturing
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
