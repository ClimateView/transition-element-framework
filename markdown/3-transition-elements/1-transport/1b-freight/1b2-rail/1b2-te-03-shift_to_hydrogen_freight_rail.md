---
title: T-1B2-TE-3 - Shift to hydrogen freight rail transportation
id: shift_to_hydrogen_freight_rail
sector: transport
sustainability: green
class: transition
version: 2.0.0
name: shift_to_hydrogen_freight_rail
type: shift
longName: 'Shift from diesel freight rail transportation to hydrogen freight rail transportation.'
shortName: 'Hydrogen freight rail'
description: 'Shift tonne kilometer from diesel freight tail to hydrogen freight tail in tonne kilometer to fulfill the need for logistics'
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
  - chain: hydrogen_rail_freight
cobenefits:
- air_quality

---

TBD

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Hydrogen vehicles have zero tailpipe emissions. They are also significantly more energy efficient and quiet than fossil-fueled vehicles. The shift to hydrogen freight rail reduces greenhouse gas emissions given that the production of the hydrogen is from a low emission source.




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
