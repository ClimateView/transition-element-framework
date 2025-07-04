---
title: T-4A1b-TE-2 - Shift to district heating in single-family buildings
id: shift_to_district_heating_in_single_family_houses
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.3
name: shift_to_district_heating_in_single_family_houses
type: shift
longName: Shift from fossil fuels and electric heaters to district heating in single-family
  buildings.
shortName: District heating single-family buildings
description: Shift square meter from single family building heated with gas, oil,
  direct electric heaters, coal and LPG to single family building heating with district
  heating in square meter to fulfill the need of comfortable premises
unitOfMeasure: m2
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: single_family_building_heating_with_gas
  - chain: single_family_building_heating_with_propane
  - chain: single_family_building_heating_with_oil
  - chain: single_family_building_heating_with_direct_electric_heaters
  - chain: single_family_building_heating_with_coal
  - chain: single_family_building_heating_with_lpg
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: single_family_building_heating_with_district_heating
cobenefits:
- indoor_climate_and_air_quality
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

District heating is an efficient way of generating and distributing heat, allowing for a broad range of energy sources while utilising its large scale.

District heating is an efficient way of generating and distributing heat, allowing for a broad range of local energy sources while utilising its large scale.


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
