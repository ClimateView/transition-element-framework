---
title: T-1B4b-TE-2 - More efficient marine freight transport
id: more_efficient_sea_freight_transportation
sector: transport
sustainability: amber
class: transition
version: 2.0.0
name: more_efficient_sea_freight_transportation
type: update
longName: 'Improve efficiency of marine freight transport to reduce fuel use.'
shortName: 'Efficient marine freight transport'
weightInversionExpression:
  expression: ((1 / ( unknown_x / %[0] )) - 1) / %[1]
  variables:
  - energy_intensity_freight_sea_transport
  - shipping_efficiency_improvement_factor
description: 'Reduce the amount of energy required to operate diesel and electric freight shipping through more efficient sea freight transportation'
unitOfMeasure: tonne_km
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_freight_sea_transport
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - shipping_efficiency_improvement_factor
- update: energy_intensity_freight_electric_sea_transport
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - shipping_efficiency_improvement_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: ship_freight
  - chain: electric_shipping_freight
cobenefits:
- air_quality
- reduced_noise

---

TBD

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Improving the energy efficiency of ships, for example through the use of lighter materials and more efficient engines, reduces the emissions per transport work performed.




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
