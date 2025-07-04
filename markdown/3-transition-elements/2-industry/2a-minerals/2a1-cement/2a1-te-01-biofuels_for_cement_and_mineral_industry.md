---
title: T-2A1-TE-1 - Shift to use biofuel in cement and mineral industry
id: biofuels_for_cement_and_mineral_industry
sector: industry
sustainability: amber
progress: 25
class: transition
version: 2.0.0
name: biofuels_for_cement_and_mineral_industry
type: shift
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
  - chain: cement_mineral_industries_biomass_usage
cobenefits:
- air_quality

---


# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

The second greatest source of emissions from cement production comes from the heating of the kiln. This is often done using coal. Replacing coal with biological waste material can reduce emissions, as biological materials would have caused emissions through natural degradation anyway.




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
