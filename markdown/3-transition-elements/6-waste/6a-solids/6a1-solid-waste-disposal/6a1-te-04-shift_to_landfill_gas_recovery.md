---
title: T-6A1-TE-4 - Shift to landfill gas recovery
id: shift_to_landfill_gas_recovery
sector: waste
sustainability: amber
class: transition
type: shift
longName: 'Shift from landfilling to landfill gas recovery'
shortName: 'Landfill gas recovery'
description: 'Shift tonne from solid waste disposal in landfills without gas recovery to solid waste disposal in landfills with landfill gas recovery in tonne to fulfill the need of waste handling'
name: shift_to_landfill_gas_recovery                
version: 2.0.0
shift: shift_to_landfill_gas_recovery
unitOfMeasure: tonne
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: solid_waste_disposal_in_landfills_and_open_dumps_etc
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: solid_waste_disposal_landfill_with_gas_recovery
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
