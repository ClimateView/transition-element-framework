---
title: T-2B2-A-1 - Oxidation of ammonia for nitric acid production
id: oxidation_of_ammonia_for_nitric_acid_production
sector: industry
sustainability: red
class: activity
name: oxidation_of_ammonia_for_nitric_acid_production
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_oxidation_of_ammonia_for_nitric_acid_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_oxidation_of_ammonia_for_nitric_acid_production
work:
- name: oxidation
  unitOfMeasure: tonne
  operationToWork:
    unitOfMeasure: tonne/tonne
    expression: '%[0]'
    variables:
    - work_intensity_direct_operations_use_tonne
  input:
  - resource: ammonia
    unitOfMeasure: tonne
    resourceToWork:
      unitOfMeasure: tonne/tonne
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/tonne
      expression: '%[0]'
      variables:
      - emission_factor_oxidation_of_ammonia_nitric_acid_production
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