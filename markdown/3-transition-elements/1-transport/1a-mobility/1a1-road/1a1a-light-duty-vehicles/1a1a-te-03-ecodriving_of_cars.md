---
title: T-1A1a-TE-3 - Ecodriving of cars
id: ecodriving_of_cars
sector: transport
sustainability: amber
progress: 50
class: transition
version: 2.0.2
ipccMitigationMethod: 1a-16-eco-driving
name: ecodriving_of_cars
type: update
longName: 'Ecodrive cars to reduce fuel use.'
shortName: 'Ecodriving'
description: 'Reduce the amount of energy required to drive petrol, diesel, LPG and natural gas vehicles through ecodriving'
unitOfMeasure: vehicle_km
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_personal_vehicles_petrol
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - personal_vehicle_eco_driving_savings_factor
- update: energy_intensity_personal_vehicles_diesel
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - personal_vehicle_eco_driving_savings_factor
- update: energy_intensity_personal_vehicles_lpg
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - personal_vehicle_eco_driving_savings_factor
- update: energy_intensity_personal_vehicles_natural_gas
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - personal_vehicle_eco_driving_savings_factor
- update: energy_intensity_personal_vehicles_hydrogen
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - personal_vehicle_eco_driving_savings_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: petrol_vehicles
  - chain: diesel_vehicles
  - chain: lpg_vehicles
  - chain: gas_vehicles
  - chain: hydrogen_vehicles
cobenefits:
- air_quality
- reduced_noise
- reduced_accidents
- increased_longevity_of_stock

---


#  Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

The speed of a car has a major impact on its fuel consumption and emissions. The effect becomes more pronounced at higher speeds. Increasing the speed from 70 mph to 75 mph increases emissions by around 15 percent. In urban areas, reduced speed not only helps reduce emissions but also dramatically improves road safety.

The speed of a car has a major impact on its fuel consumption and emissions.

The effect becomes more pronounced at higher speeds. Increasing the speed from 70 mph to 75 mph increases emissions by around 15 percent.

In urban areas, reduced speed does not only help reduce emissions but also dramatically improves road safety.

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
