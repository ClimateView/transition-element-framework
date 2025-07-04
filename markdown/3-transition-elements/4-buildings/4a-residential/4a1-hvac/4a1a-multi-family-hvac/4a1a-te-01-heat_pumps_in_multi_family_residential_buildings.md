---
title: T-4A1a-TE-1 - Shift to heat pumps in multi-family buildings
id: heat_pumps_in_multi_family_residential_buildings
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.3
name: heat_pumps_in_multi_family_residential_buildings
type: shift
longName: Shift from fossil fuels and electric heaters to heat pumps in multi-family
  buildings.
shortName: Heat pump in multi-family buildings
description: Shift square meter from multi-family buildings heated with gas, oil,
  direct electric, coal and LPG to multi-family buildings heated with heat pumps in
  square meter to fulfill the need for comfortable premises
unitOfMeasure: m2
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: multi_family_building_heating_with_gas
  - chain: multi_family_building_heating_with_oil
  - chain: multi_family_building_heating_with_propane
  - chain: multi_family_building_heating_with_direct_electric
  - chain: multi_family_building_heating_with_coal
  - chain: multi_family_building_heating_with_lpg
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: multi_family_building_heating_with_heatpump
cobenefits:
- air_quality
- indoor_climate_and_air_quality
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Heat pumps for domestic heating provide heat efficiently with zero emissions and a low lifecycle cost. They can also provide cooling. Switching to low carbon heating must be done alongside energy efficiency, so as to size the new heating system properly and guarantee high-performing, low-energy systems.




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
