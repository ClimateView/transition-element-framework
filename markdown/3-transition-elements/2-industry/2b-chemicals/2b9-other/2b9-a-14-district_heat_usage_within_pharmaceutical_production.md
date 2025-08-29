---
title: T-2B9-A-14 - District heat usage within pharmaceutical production
id: district_heat_usage_within_pharmaceutical_production
sector: industry
class: activity
name: district_heat_usage_within_pharmaceutical_production
version: 2.0.0
operation:
  growthType: true
  variable: start_year_activity_district_heat_usage_within_pharmaceutical_production
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_district_heat_usage_within_pharmaceutical_production
work:
- name: unknown
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_direct_resource_use_kwh
  input:
  - resource: district_heat
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_district_heating_kwh_to_co2e
---


# Definition
This emission source is defined by the IPCC in {{ ipcc_emission_link() }}.

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

