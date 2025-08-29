---
title: T-5A1-TE-7 - Electricity from solar parks
id: solar_parks
sector: energy
sustainability: green
progress: 10
class: transition
version: 2.0.4
name: solar_parks
type: supplyAlteration
longName: Alter the amount of electricity produced by solar parks.
shortName: Solar parks
description: Alter the amount of electricity produced by solar parks
unitOfMeasure: kwh
cohort:
  expression: '1'
maximumPotential:
  expression: '%[0]'
  variables:
  - maximum_potential_solar_parks
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: solar_parks
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