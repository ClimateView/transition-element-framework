---
title: T-5A3-TE-4 - CHP from waste incineration
id: chp_waste_incineration
sector: energy
sustainability: amber
progress: 10
class: transition
version: 2.0.4
name: chp_waste_incineration
type: supplyAlteration
longName: 'Alter the amount of electricity and heat produced by waste.'
shortName: 'CHP waste incineration'
description: 'Alter the amount of district heat and electricity produced by CHP waste incineration'
unitOfMeasure: kwh
cohort:
  expression: '1'
maximumPotential:
  expression: '%[0]'
  variables:
  - maximum_potential_heat_chp_waste_incineration
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: chp_waste_incineration
cobenefits:
- reduced_quantity_of_waste
- production_of_heat_and_power

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
