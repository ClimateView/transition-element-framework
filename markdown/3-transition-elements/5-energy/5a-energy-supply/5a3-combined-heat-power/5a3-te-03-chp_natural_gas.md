---
title: T-5A3-TE-3 - CHP from natural gas
id: chp_natural_gas
sector: energy
sustainability: amber
progress: 10
class: transition
version: 2.1.0
name: chp_natural_gas
type: supplyAlteration
longName: Alter the amount of electricity and heat produced by natural gas.
shortName: CHP natural gas
description: Alter the amount of district heat and electricity produced by CHP natural
  gas
unitOfMeasure: kwh
cohort:
  expression: '1'
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: chp_natural_gas
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
