---
title: T-5A3-TE-2 - CHP from oil
id: chp_oil
sector: energy
sustainability: red
progress: 10
class: transition
version: 2.1.0
name: chp_oil
type: supplyAlteration
longName: Alter the amount of electricity and heat produced by oil.
shortName: CHP oil
description: Alter the amount of district heat and electricity produced by CHP oil
unitOfMeasure: kwh
cohort:
  expression: '1'
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: chp_oil
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