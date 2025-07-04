---
title: T-4B1a-TE-4 - Shift to biofuel in commercial buildings
id: heating_non_residential_commercial_buildings_with_renewable_solid_biofuels
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.4
name: heating_non_residential_commercial_buildings_with_renewable_solid_biofuels
type: shift
longName: Shift from fossil fuels and electric heaters to biofuel in commercial buildings.
shortName: Biomass in commercial buildings
description: Shift square meter from commercial buildings heated with gas, oil, direct
  electric heaters, coal and LPG to commercial buildings heated with solid biofuels
  in square meter to fulfill the need for comfortable premises
unitOfMeasure: m2
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: commercial_building_heating_with_gas
  - chain: commercial_building_heating_with_propane
  - chain: commercial_building_heating_with_oil
  - chain: commercial_building_heating_with_direct_electric_heaters
  - chain: commercial_building_heating_with_coal
  - chain: commercial_building_heating_with_lpg
  - chain: commercial_building_heating_with_gas_oil
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: commercial_building_heating_with_solid_biofuels
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Oil boilers are being replaced by biofuel boilers that are fuelled by, for example, wood or wood pellets.




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
