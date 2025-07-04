---
title: T-1A1c-A-4 - Gas buses
id: gas_buses
sector: transport
class: activity
version: 2.1.0
progress: 80
sustainability: amber
ipccEmissionSource: 1a3b-road-transportation
name: gas_buses
operation:
  growthType: true
  variable: stock_buses_gas
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_buses_gas
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/vehicle_km
    expression: '%[0]'
    variables:
    - energy_intensity_buses_gas
  input:
  - resource: biogas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_biogas_gasbus
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_biogas_kwh_to_co2e
  - resource: natural_gas
    unitOfMeasure: kwh
    resourceProportion: resource_proportion_natural_gas_gasbus
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_natural_gas_kwh_to_co2e
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