---
title: T-1A4-TE-2 - More efficient marine passenger transport
id: more_efficient_sea_passenger_transportation
sector: transport
sustainability: amber
progress: 25
class: transition
version: 2.0.1
ipccMitigationMethod: 1c-03-improved-energy-efficiency-shipping
name: more_efficient_sea_passenger_transportation
type: update
longName: Improve efficiency of marine passenger transport to reduce fuel use.
shortName: Efficient marine passenger transport
weightInversionExpression:
  expression: ((1 / ( unknown_x / %[0] )) - 1) / %[1]
  variables:
  - energy_intensity_passenger_sea_transport
  - shipping_passenger_efficiency_improvement_factor
description: Reduce the amount of energy required to operate diesel, LNG passenger shipping through more more efficient sea passenger transportation
unitOfMeasure: person_km
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_passenger_sea_transport
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - shipping_passenger_efficiency_improvement_factor
- update: energy_intensity_passenger_electric_sea_transport
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - shipping_passenger_efficiency_improvement_factor
- update: energy_intensity_passenger_lng_sea_transport
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - shipping_passenger_efficiency_improvement_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: ship_passenger
  - chain: gas_oil_shipping_passenger
  - chain: electric_shipping_passenger
  - chain: lng_shipping_passenger
cobenefits:
- air_quality
- reduced_noise
---

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

TBD

{{ te_sustainability() }}

# Transition Element

{{ get_te_description_table() }}


# Activities

{{ get_te_activities() }}


# Parameters

{{ generate_parameter_table() }}


# YAML Specification

```yaml
{{ json_to_yaml() }}
```
