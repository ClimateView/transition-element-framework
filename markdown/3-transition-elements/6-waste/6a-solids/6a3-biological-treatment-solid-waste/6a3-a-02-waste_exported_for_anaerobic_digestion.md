---
title: T-6A3-A-2 - Waste exported for anaerobic digestion
id: waste_exported_for_anaerobic_digestion
sector: waste
sustainability: green
class: activity
version: 2.1.0
progress: 50
name: waste_exported_for_anaerobic_digestion
operation:
  growthType: true
  variable: stock_exported_waste_anaerobic_digestion
  growthFactor:
    expression: '%[0]'
    variables:
    - stock_growth_exported_waste_anaerobic_digestion
work:
- name: anaerobic_digestion
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: waste_fermentation
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_solid_waste_anaerobic_waste_digestion_tonne_to_co2e
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
