---
title: T-2C5-A-2 - Oil usage within lead industries
id: oil_usage_within_lead_industries
sector: industry
sustainability: red
class: activity
name: oil_usage_within_lead_industries
version: 2.1.0
operation:
  growthType: true
  variable: start_year_activity_oil_usage_within_lead_industries
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - growth_activity_oil_usage_within_lead_industries
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_direct_resource_use_kwh
  input:
  - resource: oil
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_oil_burning_resources
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