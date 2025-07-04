---
title: T-4A1-TE-1 - Energy efficient new Housing
id: energy_efficient_new_housing
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.2
name: energy_efficient_new_housing
type: update
unitOfMeasure: m2
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_heating_residential_single_family_new_buildings
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - residential_heating_energy_intensity_savings_factor
- update: energy_intensity_heating_residential_multi_family_new_buildings
  type: SAVINGS
  by:
    expression: '%[0]'
    variables:
    - residential_heating_energy_intensity_savings_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: heating_of_new_residential_single_family_buildings
  - chain: heating_of_new_residential_multi_family_buildings
cobenefits:
- air_quality
- indoor_climate_and_air_quality
- job_creation

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Newly constructed buildings can be constructed using the latest energy-saving technologies, aiming to achieve zero emissions or even negative emissions.




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
