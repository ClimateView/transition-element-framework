---
title: T-4A1b-TE-6 - Retrofitting single-family buildings for efficient heating
id: energy_efficient_single_family_residential_buildings_retrofitting
sector: buildings
sustainability: amber
progress: 25
class: transition
version: 2.0.4
name: energy_efficient_single_family_residential_buildings_retrofitting
type: update
longName: Retrofitting single-family buildings to reduce fuel use for heating
shortName: Retrofitting heating single-family buildings
description: Reduce the amount of energy required to heat single family building with
  gas, oil, direct electric heaters, district heating, heat pump, coal, solar thermal,
  solid biofuels and LPG through retrofitting
unitOfMeasure: m2
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_heating_residential_single_family_buildings_natural_gas
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
- update: energy_intensity_heating_residential_single_family_buildings_oil
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
- update: energy_intensity_heating_residential_single_family_buildings_direct_electricity
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
- update: energy_intensity_heating_residential_single_family_buildings_district_heating
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
- update: energy_intensity_heating_residential_single_family_buildings_heat_pumps
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
- update: energy_intensity_heating_residential_single_family_buildings_coal
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
- update: energy_intensity_heating_residential_single_family_buildings_solar_thermal
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
- update: energy_intensity_heating_residential_single_family_buildings_biofuel
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
- update: energy_intensity_heating_residential_single_family_buildings_lpg
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
- update: energy_intensity_heating_residential_single_family_buildings_hydrogen
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: single_family_building_heating_with_gas
  - chain: single_family_building_heating_with_propane
  - chain: single_family_building_heating_with_oil
  - chain: single_family_building_heating_with_direct_electric_heaters
  - chain: single_family_building_heating_with_district_heating
  - chain: single_family_building_heating_with_heatpump
  - chain: single_family_building_heating_with_coal
  - chain: single_family_building_heating_with_solar_thermal
  - chain: single_family_building_heating_with_solid_biofuels
  - chain: single_family_building_heating_with_lpg
  - chain: single_family_building_heating_with_hydrogen
cobenefits:
- air_quality
- indoor_climate_and_air_quality
- job_creation
- poverty_relief
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Improving the energy efficiency in the housing stock has a direct impact on emissions, either by reducing emissions from boilers or by reducing electricity consumption. This can be achieved by improving the fabric efficiency in walls and lofts as well as improved glazing. Insulating hot water tanks and pipes, installing hot water thermostats, low-energy lighting and highly efficient appliances also help reduce energy consumption.

Improving the energy efficiency in the housing stock has a direct impact on emissions, either by reducing emissions from boilers or by reducing electricity consumption. This can be achieved by improving the fabric efficiency in walls and lofts as well as improved glazing. Insulating hot water tanks and pipes, installing hot water thermostats, low-energy lighting and highly efficient appliances also help reduce energy consumption.


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
