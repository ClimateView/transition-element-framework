---
title: T-2D4-TE-3 - Efficient use of mobile machinery
id: efficient_use_of_mobile_machinery
sector: industry
sustainability: amber
progress: 25
class: transition
version: 2.0.3
name: efficient_use_of_mobile_machinery
type: update
longName: Efficient use of mobile machinery to reduce fuel use.
shortName: Efficient machinery
weightInversionExpression:
  expression: ((1 / ( unknown_x / %[0] )) - 1) / %[1]
  variables:
  - energy_intensity_machinery_diesel
  - machinery_efficiency_improvement_factor
description: Reduce the amount of energy required to operate diesel, petrol, biofuel,
  LPG and electricity mobile machinery through more efficient use
unitOfMeasure: kwh
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_machinery_biofuel
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - machinery_efficiency_improvement_factor
- update: energy_intensity_machinery_electricity
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - machinery_efficiency_improvement_factor
- update: energy_intensity_machinery_diesel
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - machinery_efficiency_improvement_factor
- update: energy_intensity_machinery_petrol
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - machinery_efficiency_improvement_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: mobile_machinery_biofuel
  - chain: mobile_machinery_electricity
  - chain: mobile_machinery_diesel
  - chain: mobile_machinery_petrol
  - chain: mobile_machinery_lpg
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

By using existing mobile machinery more efficiently, for example by different actors sharing machines, the climate impact is reduced by the fact that fewer machines need to be produced.




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
