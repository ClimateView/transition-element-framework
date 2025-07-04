---
title: T-4A1b-TE-9 - Retrofitting single-family buildings for efficient cooling
id: energy_efficient_single_family_residential_buildings_retrofitting_cooling
sector: buildings
sustainability: amber
progress: 25
class: transition
version: 2.0.1
name: energy_efficient_single_family_residential_buildings_retrofitting_cooling
type: update
longName: 'Retrofitting single-family buildings to reduce fuel use for cooling'
shortName: 'Retrofitting cooling single-family buildings'
description: 'Reduce the amount of energy required to cool single family building with AC and disitrct cooling through retrofitting'
unitOfMeasure: m2
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_cooling_residential_single_family_buildings_ac
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family_cooling
- update: energy_intensity_cooling_residential_single_family_buildings_district_cooling
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_residential_single_family_cooling
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: single_family_building_cooling_with_ac
  - chain: single_family_building_cooling_with_district_cooling

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Improving the energy efficiency in existing buildings has a direct impact on emissions, either by reducing emissions from ACs or district cooling. This can be achieved by improving the fabric efficiency in walls and lofts as well as improved glazing.




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
