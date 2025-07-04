---
title: T-5A1-TE-6 - Electricity from hydro reservoir
id: hydro_reservoir
sector: energy
sustainability: green
progress: 10
class: transition
version: 2.0.4
name: hydro_reservoir
type: supplyAlteration
longName: 'Alter the amount of electricity produced by hydro reservoir.'
shortName: 'Hydro reservoir'
description: 'Alter the amount of electricity produced by hydro reservoir'
unitOfMeasure: kwh
cohort:
  expression: '1'
maximumPotential:
  expression: '%[0]'
  variables:
  - maximum_potential_hydro_reservoir
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: hydro_reservoir
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
