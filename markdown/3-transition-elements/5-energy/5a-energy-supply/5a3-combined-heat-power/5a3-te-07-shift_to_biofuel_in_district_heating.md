---
title: T-5A3-TE-7 - Shift to biofuel in district heating
id: shift_to_biofuel_in_district_heating
sector: energy
sustainability: green
class: transition
type: shift
name: shift_to_biofuel_in_district_heating                
version: 2.0.0
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: chp_coal
  - chain: chp_natural_gas
  - chain: chp_oil
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: chp_biofuels
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
