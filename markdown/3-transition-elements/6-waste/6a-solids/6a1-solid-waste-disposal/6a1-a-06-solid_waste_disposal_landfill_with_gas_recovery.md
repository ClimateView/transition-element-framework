---
title: T-6A1-A-6 - Landfill waste with gas recovery
id: solid_waste_disposal_landfill_with_gas_recovery
sector: waste
sustainability: amber
class: activity
name: solid_waste_disposal_landfill_with_gas_recovery
version: 2.0.0
operation:
  growthType: true
  variable: stock_waste_landfill_gas_recovery
  growthFactor:
    expression: '%[0]'
    variables:
    - stock_growth_waste_landfill_gas_recovery
work:
- name: anaerobic_digestion
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: waste_landfill
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_landfill_gas_recovery_tonne_to_co2e
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
