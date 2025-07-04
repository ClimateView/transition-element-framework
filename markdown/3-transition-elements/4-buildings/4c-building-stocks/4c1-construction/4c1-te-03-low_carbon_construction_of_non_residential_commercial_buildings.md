---
title: T-4C1-TE-3 - Low carbon construction of commercial buildings
id: low_carbon_construction_of_non_residential_commercial_buildings
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.0
name: low_carbon_construction_of_non_residential_commercial_buildings
type: shift
longName: 'Shift from standard construction to low carbon construction in commercial buildings.'
shortName: 'Low carbon construction commercial'
description: 'Shift square meter from non residential commercial standard construction to non residential commercial low carbon construction in square meter to fulfill the need of housing'
unitOfMeasure: m2
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: non_residential_commercial_standard_construction
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: non_residential_commercial_low_carbon_construction

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

No other commonly used building material requires as little energy to produce as wood. Wood products also act as carbon sinks, and the average life of wood as structural material is 75 years. Every cubic metre of wood used as a substitute for other building materials reduces CO₂ emissions to the atmosphere by an average of 1 to 2.5 tonnes of CO₂.



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
