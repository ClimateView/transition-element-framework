---
title: T-5A3-TE-6 - Increased energy recovery from waste
id: increased_energy_recovery_from_waste
sector: energy
sustainability: amber
class: transition
type: shift
longName: 'Shift from incineration and open burning to CHP waste incineration.'
shortName: 'Energy from waste'
description: 'Shift tonne from solid waste disposal in landfills and open dumps, incineration and open burning of waste to CHP waste incineration in tonne to fulfill the need of warm premisses'
name: increased_energy_recovery_from_waste                
version: 2.0.0
unitOfMeasure: tonne
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: incineration_and_open_burning_of_waste
shiftTo:
  atoc:
    expression: 1 / %[0]
    variables:
    - energy_from_waste_conversion
  chains:
  - chain: chp_waste_incineration
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
