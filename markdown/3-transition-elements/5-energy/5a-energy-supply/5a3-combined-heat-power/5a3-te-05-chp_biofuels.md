---
title: T-5A3-TE-5 - CHP from biomass
id: chp_biofuels
sector: energy
sustainability: green
progress: 10
class: transition
version: 2.1.0
name: chp_biofuels
type: supplyAlteration
longName: Alter the amount of electricity and heat produced by biofuel.
shortName: CHP biomass
description: Alter the amount of district heat and electricity produced by CHP biofuels
unitOfMeasure: kwh
cohort:
  expression: '1'
maximumPotential:
  expression: '%[0]'
  variables:
  - maximum_potential_heat_chp_biofuels
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: chp_biofuels
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
