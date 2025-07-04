---
title: T-4B1a-TE-6 - Retrofitting commerical buildings for efficient heating
id: energy_efficient_non_residential_commercial_buildings_retrofitting
sector: buildings
sustainability: amber
progress: 25
class: transition
version: 2.0.6
name: energy_efficient_non_residential_commercial_buildings_retrofitting
type: update
longName: Retrofitting commerical buildings to reduce fuel use for heating
shortName: Retrofitting heating commercial buildings
description: Reduce the amount of energy required to heat commercial building with
  gas, oil, direct electric heaters, district heating, heat pump, coal, solar thermal,
  solid biofuels and LPG through retrofitting
unitOfMeasure: m2
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_heating_non_residential_commercial_natural_gas
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
- update: energy_intensity_heating_non_residential_commercial_oil
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
- update: energy_intensity_heating_non_residential_commercial_direct_electricity
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
- update: energy_intensity_heating_non_residential_commercial_district_heating
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
- update: energy_intensity_heating_non_residential_commercial_heat_pumps
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
- update: energy_intensity_heating_non_residential_commercial_coal
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
- update: energy_intensity_heating_non_residential_commercial_solar_thermal
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
- update: energy_intensity_heating_non_residential_commercial_biofuel
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
- update: energy_intensity_heating_non_residential_commercial_lpg
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
- update: energy_intensity_heating_non_residential_commercial_hydrogen
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_commercial
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: commercial_building_heating_with_gas
  - chain: commercial_building_heating_with_propane
  - chain: commercial_building_heating_with_oil
  - chain: commercial_building_heating_with_direct_electric_heaters
  - chain: commercial_building_heating_with_district_heating
  - chain: commercial_building_heating_with_heatpump
  - chain: commercial_building_heating_with_coal
  - chain: commercial_building_heating_with_solar_thermal
  - chain: commercial_building_heating_with_solid_biofuels
  - chain: commercial_building_heating_with_lpg
  - chain: commercial_building_heating_with_hydrogen
  - chain: commercial_building_heating_with_gas_oil
cobenefits:
- air_quality
- indoor_climate_and_air_quality
- job_creation
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Improving the energy efficiency in existing buildings has a direct impact on emissions, either by reducing emissions from boilers or by reducing electricity consumption. This can be achieved by improving the fabric efficiency in walls and lofts as well as improved glazing. Insulating hot water tanks and pipes, installing hot water thermostats, low-energy lighting and highly efficient appliances also help reduce energy consumption.

Improving the energy efficiency in the existing housing stock has a direct impact on emissions, either by reducing emissions from exiting oil and gas boilers, or by reducing electricy consumption.

Fabric efficiency(walls, lofts) and other measures such as glazing will reduce space heating demand. Other areas to address are hot water and appliances, by insulating hot water tanks and pipes, installing hot water thermostats, low - energy lighting and highly efficient appliances.

Measures such as batteries and smart appliances also allow households to use energy more flexibly, helping to shift consumption away from peak and towards periods when renewable energy is available.


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
