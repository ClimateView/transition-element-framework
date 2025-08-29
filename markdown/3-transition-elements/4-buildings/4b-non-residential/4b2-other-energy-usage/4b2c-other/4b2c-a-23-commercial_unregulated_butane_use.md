---
title: T-4B2c-A-23 - Commercial other butane use
id: commercial_unregulated_butane_use
sector: buildings
sustainability: red
class: activity
name: commercial_unregulated_butane_use
version: 2.1.0
operation:
  growthType: true
  variable: stock_commercial_unregulated_butane_use
  growthFactor:
    unitOfMeasure: per_capita
    expression: '%[0]'
    variables:
    - stock_growth_commercial_unregulated_butane_use
work:
- name: combustion
  unitOfMeasure: kwh
  operationToWork:
    unitOfMeasure: kwh/kwh
    expression: '%[0]'
    variables:
    - energy_intensity_direct_resource_use_kwh
  input:
  - resource: butane
    unitOfMeasure: kwh
    resourceToWork:
      unitOfMeasure: kwh/kwh
      expression: '1'
    emissionFactor:
      unitOfMeasure: g_co2e/kwh
      expression: '%[0]'
      variables:
      - emission_factor_butane_kwh_to_co2e
---
