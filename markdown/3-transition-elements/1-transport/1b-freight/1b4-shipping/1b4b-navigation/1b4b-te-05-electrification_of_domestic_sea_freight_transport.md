---
title: T-1B4b-TE-5 - Shift to electric marine freight transportion
id: electrification_of_domestic_sea_freight_transport
sector: transport
sustainability: green
class: transition
version: 2.0.0
name: electrification_of_domestic_sea_freight_transport
type: shift
longName: 'Shift from diesel marine freight transportation to electric marine freight.'
shortName: 'Electric marine freight transportion'
description: 'Shift tonne kilometer from ship freight to electric shipping freight in tonne kilometer to fulfill the need of logistics'
unitOfMeasure: tonne_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: ship_freight
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electric_shipping_freight
cobenefits:
- air_quality
- reduced_noise

---

TBD

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Switching to electric propulsion can help greatly reduce greenhouse gas emissions and fully reduce particulate emissions.




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
