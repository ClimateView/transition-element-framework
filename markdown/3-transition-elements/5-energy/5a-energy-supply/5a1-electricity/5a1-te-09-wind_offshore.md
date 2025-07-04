---
title: T-5A1-TE-9 - Electricity from wind offshore
id: wind_offshore
sector: energy
sustainability: green
progress: 10
class: transition
version: 2.0.0
name: wind_offshore
type: supplyAlteration
longName: 'Alter the amount of electricity produced by offshore wind.'
shortName: 'Wind offshore'
description: 'Alter the amount of electricity produced by wind offshore'
unitOfMeasure: kwh
cohort:
  expression: '1'
maximumPotential:
  expression: '%[0]'
  variables:
  - maximum_potential_wind_offshore
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: wind_offshore
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
