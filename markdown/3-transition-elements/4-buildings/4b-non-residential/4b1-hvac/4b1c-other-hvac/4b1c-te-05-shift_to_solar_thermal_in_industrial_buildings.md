---
title: T-4B1c-TE-5 - Shift to solar thermal in industrial buildings
id: shift_to_solar_thermal_in_industrial_buildings
sector: buildings
sustainability: green
progress: 10
class: transition
version: 2.0.1
name: shift_to_solar_thermal_in_industrial_buildings
type: shift
longName: Shift from fossil fuels and electric heaters to solar thermal in industrial
  buildings.
shortName: Solar thermal in industrial buildings
description: Shift square meter from industrial building heated with gas, oil, direct
  electric heaters, coal, LPG to industrial building heated with solar thermal in
  square meter to fulfill the need of comfortable premises
unitOfMeasure: m2
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: industrial_building_heating_with_gas
  - chain: industrial_building_heating_with_oil
  - chain: industrial_building_heating_with_direct_electric_heaters
  - chain: industrial_building_heating_with_lpg
  - chain: industrial_building_heating_with_coal
  - chain: industrial_building_heating_with_gas_oil
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: industrial_building_heating_with_solar_thermal
cobenefits:
- air_quality
- indoor_climate_and_air_quality
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Solar thermal industrial buildings.




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
