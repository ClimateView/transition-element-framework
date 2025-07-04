---
title: T-1B1b-TE-5 - Ecodriving of heavy trucks
id: ecodriving_of_heavy_trucks
sector: transport
sustainability: amber
class: transition
version: 2.0.2
ipccMitigationMethod: 1a-08-supply-chain-management
name: ecodriving_of_heavy_trucks
type: update
longName: 'Ecodrive heavy trucks to reduce fuel use.'
shortName: 'Ecodriving HGV'
description: 'Reduce the amount of energy required to drive diesel, hydrogen and battery electric heavy trucks through ecodriving'
unitOfMeasure: tonne_km
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_freight_heavy_trucks_diesel
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_eco_driving_savings_factor
- update: energy_intensity_freight_heavy_trucks_bev
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_eco_driving_savings_factor
- update: energy_intensity_freight_heavy_trucks_hydrogen
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_eco_driving_savings_factor
- update: energy_intensity_freight_heavy_trucks_gas
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_eco_driving_savings_factor
- update: energy_intensity_freight_heavy_trucks_petrol
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - heavy_truck_eco_driving_savings_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_heavy_trucks
  - chain: battery_electric_heavy_trucks
  - chain: hydrogen_heavy_trucks
  - chain: gas_heavy_trucks
  - chain: petrol_heavy_trucks
cobenefits:
- air_quality
- reduced_noise
- reduced_accidents
- increased_longevity_of_stock

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

A truck's speed has a major impact on its fuel consumption and emissions - both at lower and higher speeds.The effect becomes more pronounced at higher speeds. Reducing a truck's cruising speed from 55 to 50 mph can reduce carbon dioxide emissions by up to 15 percent.Reduced speed not only helps reduce emissions but also improves road safety.




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
