---
title: T-1B4b-TE-1 - Shift to LNG fuel for marine freight transport
id: shift_to_lng_fuel_for_sea_freight_transportation
sector: transport
sustainability: amber
class: transition
version: 2.0.1
name: shift_to_lng_fuel_for_sea_freight_transportation
type: shift
longName: Shift from diesel marine freight transport to LNG marine freight.
shortName: LNG marine freight transportion
description: Shift tonne kilometer from ship freight to LNG shipping freight in tonne kilometer to fulfill the need of logistics
unitOfMeasure: tonne_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: ship_freight
  - chain: gas_oil_shipping_freight
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: lng_shipping_freight
cobenefits:
- air_quality
---
TBD

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Switching to liquefied natural gas (LNG) can reduce greenhouse gas emissions by 15 percent while also reducing the emissions of dust, soot, nitrogen oxides and sulfur.




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
