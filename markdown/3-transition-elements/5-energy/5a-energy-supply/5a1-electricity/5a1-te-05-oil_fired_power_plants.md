---
title: T-5A1-TE-5 - Electricity from oil power plants
id: oil_fired_power_plants
sector: energy
sustainability: red
progress: 10
class: transition
version: 2.1.0
name: oil_fired_power_plants
type: supplyAlteration
longName: Alter the amount of electricity produced by oil.
shortName: Power plant oil
description: Alter the amount of electricity produced by oil fired power plants
unitOfMeasure: kwh
cohort:
  expression: '1'
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: oil_fired_power_plants
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