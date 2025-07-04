---
title: T-4B1b-TE-7 - Retrofitting public buildings for efficient cooling
id: energy_efficient_non_residential_public_buildings_retrofitting_cooling
sector: buildings
sustainability: amber
progress: 25
class: transition
version: 2.0.1
name: energy_efficient_non_residential_public_buildings_retrofitting_cooling
type: update
longName: 'Retrofitting public buildings to reduce fuel use for cooling'
shortName: 'Retrofitting cooling public buildings'
description: 'Reduce the amount of energy required to cool public building with AC and disitrct cooling through retrofitting'
unitOfMeasure: m2
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_cooling_non_residential_public_ac
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public_cooling
- update: energy_intensity_cooling_non_residential_public_district_cooling
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - retrofitting_savings_factor_non_residential_public_cooling
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: public_building_cooling_with_ac
  - chain: public_building_cooling_with_district_cooling

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
