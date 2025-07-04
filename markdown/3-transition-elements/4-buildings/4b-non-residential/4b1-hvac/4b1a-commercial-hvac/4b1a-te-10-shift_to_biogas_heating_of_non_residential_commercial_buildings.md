---
title: T-4B1a-TE-10 - Shift to biogas in commercial buildings
id: shift_to_biogas_heating_of_non_residential_commercial_buildings
sector: buildings
sustainability: green
class: transition
type: shift
longName: 'Shift from natural gas to biogas in commercial buildings.'
shortName: 'Biogas in commercial buildings'
name: shift_to_biogas_heating_of_non_residential_commercial_buildings                
version: 2.0.0
description: 'Shift square meter from commercial building heating with gas to commercial building heating with biogas in square meter to fulfill the need of comfortable premises'
unitOfMeasure: m2
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: commercial_building_heating_with_gas
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: commercial_building_heating_with_biogas
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
