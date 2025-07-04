---
title: T-2B1-A-1 - Reforming of methane for ammonia production
id: reforming_of_methane_for_ammonia_production
name: reforming_of_methane_for_ammonia_production
sector: industry
sustainability: amber
class: activity
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_reforming_of_methane_for_ammonia_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_reforming_of_methane_for_ammonia_production
work:
- name: reforming
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: natural_gas
    resourceProportion: resource_proportion_natural_gas_reforming_for_ammonia_production
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_reforming_of_natural_gas_for_ammonia_production
  - resource: biogas
    resourceProportion: resource_proportion_biogas_reforming_for_ammonia_production
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_reforming_of_biogas_for_ammonia_production
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
