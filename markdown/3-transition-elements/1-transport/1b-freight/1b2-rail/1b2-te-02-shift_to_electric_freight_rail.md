---
title: T-1B2-TE-2 - Shift to electric freight rail transportation
id: shift_to_electric_freight_rail
sector: transport
sustainability: green
class: transition
version: 2.0.0
name: shift_to_electric_freight_rail
type: shift
longName: 'Shift from diesel freight rail transportation to electric freight rail transportation.'
shortName: 'Electric freight rail'
description: 'Shift tonne kilometer from diesel freight tail to electric freight tail in tonne kilometer to fulfill the need for logistics'
unitOfMeasure: tonne_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_rail_freight
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electric_rail_freight
cobenefits:
- air_quality

---

TBD

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Electric vehicles have zero tailpipe emissions. They are also significantly more energy efficient and quiet than fossil-fueled vehicles. The shift to electric freight rail reduces greenhouse gas emissions.




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
