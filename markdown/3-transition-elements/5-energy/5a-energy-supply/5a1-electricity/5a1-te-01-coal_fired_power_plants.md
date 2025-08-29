---
title: T-5A1-TE-1 - Electricity from coal power plants
id: coal_fired_power_plants
sector: energy
sustainability: red
progress: 10
class: transition
version: 2.0.0
name: coal_fired_power_plants
type: supplyAlteration
longName: Alter the amount of electricity produced by coal.
shortName: Power plant coal
description: Alter the amount of electricity produced by coal fired power plants
unitOfMeasure: kwh
cohort:
  expression: '1'
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: coal_fired_power_plants
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