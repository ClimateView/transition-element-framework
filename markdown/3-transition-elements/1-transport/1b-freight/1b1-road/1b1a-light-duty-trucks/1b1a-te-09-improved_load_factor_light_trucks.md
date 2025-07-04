---
title: T-1B1a-TE-9 - Improved load factor for light trucks
id: improved_load_factor_light_trucks
sector: transport
sustainability: amber
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-08-supply-chain-management
name: improved_load_factor_light_trucks
type: upshift
longName: 'Improved load factor for light trucks.'
shortName: 'Load factor LGV'
weightInversionExpression:
  expression: ((( 1 / unknown_x ) / %[0] ) - 1 ) / %[1]
  variables:
  - load_factor_light_trucks
  - load_factor_increase_light_trucks
description: 'Reduce the amount of vehicle kilometer from diesel light trucks to fulfill the need of logistics through improving the load factor'
unitOfMeasure: ideal_vehicle_km
cohort:
  expression: '1'
variablesToUpdate:
- update: load_factor_light_trucks
  type: INCREASE
  by:
    expression: '%[0]'
    variables:
    - load_factor_increase_light_trucks
carbonCausalChains:
  atoc:
    expression: 1 / %[0]
    variables:
    - load_factor_light_trucks
  chains:
  - chain: diesel_light_trucks
  - chain: hydrogen_light_trucks
  - chain: battery_electric_light_trucks
  - chain: petrol_light_trucks
  - chain: gas_light_trucks
cobenefits:
- air_quality
- reduced_noise
- reduced_accidents
- less_congestion

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Emissions from freight transport are directly impacted by how well the trucks are filled - the load factor. The UK average load factor is around 68 percent.

Emissions from freight transport (per unit of weight) are directly related to the load factor - which means how well the trucks are filled.

The UK average load factor is around 68 percent, referring to the volume of goods moved as a proportion of the total volume of goods that could have been carried.Around 30 percent of the time trucks run completely empty.

Higher load factors will not only reduce emissions but be economically benefical.

Source: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/777781/fom_understanding_freight_transport_system.pdf


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
