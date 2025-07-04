---
title: T-4A1a-TE-6 - Retrofitting multi-family buildings for efficient heating
id: energy_efficient_multi_family_residential_buildings_retrofitting
sector: buildings
sustainability: amber
progress: 25
class: transition
version: 2.0.6
name: energy_efficient_multi_family_residential_buildings_retrofitting
type: update
longName: Retrofitting multi-family buildings to reduce fuel use for heating
shortName: Retrofitting heating multi-family buildings
description: Reduce the amount of energy required to heat district heating,  gas,
  oil, direct electric, heat pump, solid biofuels, coal, solar thermal and LPG multi
  family buildings through retrofitting
unitOfMeasure: m2
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_heating_residential_multi_family_buildings_biofuel
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
- update: energy_intensity_heating_residential_multi_family_buildings_direct_electricity
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
- update: energy_intensity_heating_residential_multi_family_buildings_district_heating
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
- update: energy_intensity_heating_residential_multi_family_buildings_heat_pumps
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
- update: energy_intensity_heating_residential_multi_family_buildings_oil
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
- update: energy_intensity_heating_residential_multi_family_buildings_natural_gas
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
- update: energy_intensity_heating_residential_multi_family_buildings_coal
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
- update: energy_intensity_heating_residential_multi_family_buildings_solar_thermal
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
- update: energy_intensity_heating_residential_multi_family_buildings_lpg
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
- update: energy_intensity_heating_residential_multi_family_buildings_hydrogen
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_multi_family
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: multi_family_building_heating_with_solid_biofuels
  - chain: multi_family_building_heating_with_direct_electric
  - chain: multi_family_building_heating_with_district_heating
  - chain: multi_family_building_heating_with_heatpump
  - chain: multi_family_building_heating_with_oil
  - chain: multi_family_building_heating_with_gas
  - chain: multi_family_building_heating_with_propane
  - chain: multi_family_building_heating_with_coal
  - chain: multi_family_building_heating_with_solar_thermal
  - chain: multi_family_building_heating_with_lpg
  - chain: multi_family_building_heating_with_hydrogen
cobenefits:
- air_quality
- indoor_climate_and_air_quality
- poverty_relief
- job_creation
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Improving the energy efficiency in existing buildings has a direct impact on emissions, either by reducing emissions from boilers or by reducing electricity consumption. This can be achieved by improving the fabric efficiency in walls and lofts as well as improved glazing. Insulating hot water tanks and pipes, installing hot water thermostats, low-energy lighting and highly efficient appliances also help reduce energy consumption.




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
