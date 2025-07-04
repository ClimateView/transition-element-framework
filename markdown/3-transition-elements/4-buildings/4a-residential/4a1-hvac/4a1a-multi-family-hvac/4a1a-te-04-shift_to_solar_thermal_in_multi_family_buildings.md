---
title: T-4A1a-TE-4 - Shift to solar thermal in multi-family buildings
id: shift_to_solar_thermal_in_multi_family_buildings
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.2
name: shift_to_solar_thermal_in_multi_family_buildings
type: shift
longName: Shift from fossil fuels and electric heaters to solar thermal in multi-family
  buildings.
shortName: Solar thermal in multi-family buildings
description: Shift square meter from multi family building heated with gas, oil, direct
  electric and coal to multi family building heated with solar thermal in square meter
  to fulfill the need of comfortable premises
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
  - chain: multi_family_building_heating_with_solar_thermal
cobenefits:
- air_quality
- indoor_climate_and_air_quality
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Solar thermal multi-family houses




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
