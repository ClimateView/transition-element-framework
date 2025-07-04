---
title: T-4B1b-TE-2 - Shift to district cooling in public buildings
id: shift_to_district_cooling_in_public_buildings
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.0
name: shift_to_district_cooling_in_public_buildings
type: shift
longName: 'Shift from AC to district cooling in public buildings.'
shortName: 'District cooling in public buildings'
description: 'Shift square meter from industrial building cooling with AC to industrial building cooling with district cooling in square meter to fulfill the need of comfortable premises'
unitOfMeasure: m2
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: public_building_cooling_with_ac
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: public_building_cooling_with_district_cooling

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

District cooling is an efficient way of generating and distributing cooling, allowing for a broad range of energy sources while utilising its large scale.




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
