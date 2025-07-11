---
title: T-5A2-TE-3 - District heating by residual heat
id: district_heating_residual_heat
sector: energy
sustainability: green
progress: 10
class: transition
version: 2.1.0
name: district_heating_residual_heat
type: supplyAlteration
longName: Alter the amount of heat produced by residual heat.
shortName: Residual heat district heating
description: Alter the amount of district heat produced by residual heat
unitOfMeasure: kwh
cohort:
  expression: '1'
maximumPotential:
  expression: '%[0]'
  variables:
  - maximum_potential_district_heating_residual_heat
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: district_heating_residual_heat
cobenefits:
- air_quality
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

TBD




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
