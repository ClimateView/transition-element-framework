---
title: T-5A3-TE-1 - CHP from coal
id: chp_coal
sector: energy
sustainability: red
progress: 10
class: transition
version: 2.0.0
name: chp_coal
type: supplyAlteration
longName: 'Alter the amount of electricity and heat produced by coal.'
shortName: 'CHP coal'
description: 'Alter the amount of district heat and electricity produced by CHP coal'
unitOfMeasure: kwh
cohort:
  expression: '1'
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: chp_coal

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
