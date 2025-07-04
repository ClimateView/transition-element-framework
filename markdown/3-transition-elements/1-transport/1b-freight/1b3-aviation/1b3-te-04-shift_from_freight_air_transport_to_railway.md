---
title: T-1B3-TE-4 - Shift from freight air transport to electric rail freight
id: shift_from_freight_air_transport_to_railway
sector: transport
sustainability: green
class: transition
type: shift
longName: 'Shift from air freight transport to electric rail freight transport.'
shortName: 'Freight air to electric rail'
name: shift_from_freight_air_transport_to_railway                
version: 2.0.0
description: 'Shift tonne kilometer from freight transportation by air to electric rail in tonne kilometer to fulfill the need of logistics'
unitOfMeasure: tonne_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: freight_transportation_by_air
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electric_rail_freight
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
