---
title: T-4B1b-TE-6 - Retrofitting public buildings for efficient heating
id: energy_efficient_non_residential_public_buildings_retrofitting
sector: buildings
sustainability: amber
progress: 25
class: transition
version: 2.0.8
name: energy_efficient_non_residential_public_buildings_retrofitting
type: update
longName: Retrofitting public buildings to reduce fuel use for heating
shortName: Retrofitting heating public buildings
description: Reduce the amount of energy required to heat public building heating
  with district heating oil, gas, direct electric heaters, solid biofuels, heat pump,
  coal, solar thermal and  LPG through retrofitting
unitOfMeasure: m2
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_heating_non_residential_public_biofuel
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
- update: energy_intensity_heating_non_residential_public_direct_electricity
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
- update: energy_intensity_heating_non_residential_public_natural_gas
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
- update: energy_intensity_heating_non_residential_public_oil
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
- update: energy_intensity_heating_non_residential_public_heat_pumps
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
- update: energy_intensity_heating_non_residential_public_district_heating
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
- update: energy_intensity_heating_non_residential_public_coal
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
- update: energy_intensity_heating_non_residential_public_solar_thermal
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
- update: energy_intensity_heating_non_residential_public_lpg
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
- update: energy_intensity_heating_non_residential_public_hydrogen
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: public_building_heating_with_solid_biofuels
  - chain: public_building_heating_with_direct_electric_heaters
  - chain: public_building_heating_with_gas
  - chain: public_building_heating_with_propane
  - chain: public_building_heating_with_oil
  - chain: public_building_heating_with_heatpump
  - chain: public_building_heating_with_district_heating
  - chain: public_building_heating_with_coal
  - chain: public_building_heating_with_solar_thermal
  - chain: public_building_heating_with_lpg
  - chain: public_building_heating_with_hydrogen
  - chain: public_building_heating_with_gas_oil
cobenefits:
- air_quality
- indoor_climate_and_air_quality
- job_creation
- increased_productivity_school_attainment
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
