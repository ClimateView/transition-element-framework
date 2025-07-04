---
title: T-2D4-TE-2 - Shift to electric mobile machinery
id: electrification_of_mobile_machinery
sector: industry
sustainability: green
progress: 25
class: transition
version: 2.0.2
name: electrification_of_mobile_machinery
type: shift
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: mobile_machinery_diesel
  - chain: mobile_machinery_petrol
  - chain: mobile_machinery_lpg
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: mobile_machinery_electricity
cobenefits:
- air_quality
- reduced_noise
---
# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Fuel-powered mobile machinery are being replaced by electric ones that are more efficient and do not contribute to any direct emissions of greenhouse gases.




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
