---
title: T-4A1a-TE-5 - Shift to biofuel heating in multi-family buildings
id: heating_multi_family_residential_buildings_with_renewable_solid_biofuels
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.3
name: heating_multi_family_residential_buildings_with_renewable_solid_biofuels
type: shift
longName: Shift from fossil fuels and electric heaters to biofuel in multi-family
  buildings.
shortName: Biomass in multi-family buildings
description: Shift square meter from multi family building heated with gas oil, direct
  electric, coal and LPG to multi family building heated with solid biofuels in square
  meter to fulfill the need of comfortable premises
unitOfMeasure: m2
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: multi_family_building_heating_with_gas
  - chain: multi_family_building_heating_with_propane
  - chain: multi_family_building_heating_with_oil
  - chain: multi_family_building_heating_with_direct_electric
  - chain: multi_family_building_heating_with_coal
  - chain: multi_family_building_heating_with_lpg
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: multi_family_building_heating_with_solid_biofuels
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Oil boilers in homes are being replaced by biofuel boilers that are fuelled by, for example, wood or wood pellets.




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
