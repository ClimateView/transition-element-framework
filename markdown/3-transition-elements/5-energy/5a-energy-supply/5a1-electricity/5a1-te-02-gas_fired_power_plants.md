---
title: T-5A1-TE-2 - Electricity from gas power plants
id: gas_fired_power_plants
sector: energy
sustainability: amber
progress: 10
class: transition
version: 2.1.0
name: gas_fired_power_plants
type: supplyAlteration
longName: Alter the amount of electricity produced by gas.
shortName: Power plant gas
description: Alter the amount of electricity produced by gas fired power plants
unitOfMeasure: kwh
cohort:
  expression: '1'
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: gas_fired_power_plants
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
