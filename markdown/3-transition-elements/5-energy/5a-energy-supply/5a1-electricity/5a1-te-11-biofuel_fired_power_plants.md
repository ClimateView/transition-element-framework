---
title: T-5A1-TE-11 - Electricity from biomass power plants
id: biofuel_fired_power_plants
sector: energy
sustainability: green
class: transition
type: supplyAlteration
longName: 'Alter the amount of electricity produced by biofuel.'
shortName: 'Power plant biomass'
name: biofuel_fired_power_plants                
version: 1.0.0
description: 'Alter the amount of electricity produced by biofuel fired power plants'
unitOfMeasure: kwh
cohort:
  expression: '1'
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: biofuel_fired_powerplants
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
