---
title: T-1B3-TE-2 - Shift to electric freight air transportation
id: electric_freight_airplanes
sector: transport
sustainability: green
class: transition
type: shift
longName: 'Shift from conventional fueled ones to electric freight air transportation.'
shortName: 'Electric freight airplanes'
name: electric_freight_airplanes                
version: 2.0.0
description: 'Shift tonne kilometer from freight transportation by air to electric freight transportation by air in tonne kilometer to fulfill the need of logistics'
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
  - chain: electric_freight_transportation_by_air
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
