---
title: T-4A1b-TE-7 - Energy efficient use of ACs in single-family buildings
id: efficient_use_single_family_residential_buildings_cooling
sector: buildings
sustainability: amber
progress: 25
class: transition
version: 2.0.0
name: efficient_use_single_family_residential_buildings_cooling
type: update
longName: 'Energy efficient use of ACs in single-family buildings to reduce electricity use'
shortName: 'Single-family AC efficient use'
description: 'Reduce the amount of energy required to cool single family buildings with AC through efficient use of AC units'
unitOfMeasure: m2
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_cooling_residential_single_family_buildings_ac
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - single_family_ac_efficient_use_savings_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: single_family_building_cooling_with_ac

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Efficient use of ACs through e.g. smart thermostats and raising the indoor temperature a few degrees and even more so during the time nobody is at home can save significant amounts of energy.




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
