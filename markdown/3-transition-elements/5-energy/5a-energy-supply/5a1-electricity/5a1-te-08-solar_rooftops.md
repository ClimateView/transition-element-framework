---
title: T-5A1-TE-8 - Electricity from solar rooftops
id: solar_rooftops
sector: energy
sustainability: green
progress: 10
class: transition
version: 2.1.0
name: solar_rooftops
type: supplyAlteration
longName: Alter the amount of electricity produced by solar rooftops.
shortName: Solar rooftops
description: Alter the amount of electricity produced by solar rooftops
unitOfMeasure: kwh
cohort:
  expression: '1'
maximumPotential:
  expression: '%[0]'
  variables:
  - maximum_potential_solar_rooftops
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: solar_rooftops
cobenefits:
- air_quality
- job_creation
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
