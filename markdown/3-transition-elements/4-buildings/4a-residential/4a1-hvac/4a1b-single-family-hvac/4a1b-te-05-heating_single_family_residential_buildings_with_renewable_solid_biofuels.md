---
title: T-4A1b-TE-5 - Shift to biofuel heating in single-family buildings
id: heating_single_family_residential_buildings_with_renewable_solid_biofuels
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.4
name: heating_single_family_residential_buildings_with_renewable_solid_biofuels
type: shift
longName: Shift from fossil fuels and electric heaters to biofuel in single-family
  buildings .
shortName: Biomass in single-family buildings
description: Shift square meter from single-family buildings heated with gas, oil,
  direct electric heaters, coal and LPG to single-family buildings heated with solid
  biofuels in square meter to fulfill the need for comfortable premises
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
  - chain: single_family_building_heating_with_solid_biofuels
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
