---
title: T-1A1C-TE-5 - Shift to electric busses
id: shift_to_electric_buses
sector: transport
sustainability: green
class: transition
type: shift
name: shift_to_electric_buses
version: 2.0.0
shift: shift_to_electric_buses
unitOfMeasure: vehicle_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_buses
  - chain: petrol_buses
  - chain: lpg_buses
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electric_bus
cobenefits:
- air_quality
- reduced_noise
---

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

TBD



# Transition Element

- **Type of shift**: `{{ get_te_shift_type() }}`
- **Activity**: TBD
- **Operation**: TBD
- **ATOC**: TBD


# Activities

{{ get_te_activities() }}


# Parameters

{{ generate_parameter_table() }}


# YAML Specification

```yaml
{{ json_to_yaml() }}
```
