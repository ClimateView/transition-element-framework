---
title: T-3A1-A-1 - Enteric Fermentation from Cattle
id: enteric_fermentation_cattle
sector: afolu
sustainability: red
progress: 80
ipccEmissionSource: 3a1a-cattle
name: enteric_fermentation_cattle
class: activity
version: 1.0.0
operation:
  growthType: YES
  variable: activity_cattle
  growthFactor:
    unitOfMeasure: per_capita
    expression: "%[0]"
    variables:
      - activity_growth_cattle
  primaryStock:
    name: average_other_livestock_population
work:
  - name: enteric_fermentation
    unitOfMeasure: joule
    operationToWork:
      unitOfMeasure: kj/kg
      expression: "%[0]"
      variables:
        - enteric_fermentation_efficiency_cattle
    input:
      - resource: cattle_feed
        unitOfMeasure: kg
        resourceToWork:
          unitOfMeasure: kg/kj
          expression: "%[0]"
          variables:
            - kg_feed_per_kj_enteric_fermentation_other_livestock
        emissionFactor:
          unitOfMeasure: g_co2e/kg
          expression: "%[0]"
          variables:
            - emission_factor_enteric_fermentation_cattle_feed
---

# Definition
This emission source is defined by the IPCC in {{ ipcc_emission_link() }} 


{{ activity_sustainability() }}

# Transition Elements

This activity has the following mitigation options modelled as transition elements:

{{ transition_element_list() }}

# Activity Model
This emission source is modelled with [Enteric Fermentation](/5-resources/5-about/work-types.md#enteric-fermentation) as:

*TBD*.

## Parameters

{{ generate_parameter_table() }}

# YAML Specification

```yaml
{{ json_to_yaml() }}
```
