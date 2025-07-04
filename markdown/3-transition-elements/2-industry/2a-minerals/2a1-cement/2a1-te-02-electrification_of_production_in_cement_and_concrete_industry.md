---
title: T-2A1-TE-2 - Shift to electricity in cement and mineral industry
id: electrification_of_production_in_cement_and_concrete_industry
sector: industry
sustainability: green
progress: 25
class: transition
version: 2.0.0
name: electrification_of_production_in_cement_and_concrete_industry
type: shift
longName: 'Shift from using coal to electricity energy in cement and mineral industry.'
shortName: 'Electricity in cement and mineral'
description: 'Shift kilowatt-hours from cement and mineral processes that uses coal to cement and mineral processes that uses electricity'
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: cement_mineral_industries_coal_usage
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: cement_mineral_industries_electricity_usage
cobenefits:
- air_quality

---


# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

The second greatest source of emissions from cement production comes from the heating of the kiln. This is often done using coal. Replacing the energy from coal combustion with electrical processes, where applicable, can reduce emissions.




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
