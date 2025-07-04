---
title: T-4A1a-TE-8 - Energy efficient AC in multi-family buildings
id: energy_efficient_multi_family_residential_buildings_cooling
sector: buildings
sustainability: green
progress: 25
class: transition
version: 2.0.0
name: energy_efficient_multi_family_residential_buildings_cooling
type: update
longName: 'Upgrade AC in multi-family buildings to reduce electricity use'
shortName: 'Efficient multi-family AC'
description: 'Reduce the amount of energy required to cool multi family buildings with AC through more efficient AC units'
weightInversionExpression:
  expression: ((1 / ( unknown_x / %[0] )) - 1) / %[1]
  variables:
  - energy_intensity_cooling_residential_multi_family_buildings_ac
  - multi_family_ac_efficiency_improvement_factor
unitOfMeasure: m2
cohort:
  expression: '1'
variablesToUpdate:
- update: energy_intensity_cooling_residential_multi_family_buildings_ac
  type: EFFICIENCY_IMPROVEMENT
  by:
    expression: '%[0]'
    variables:
    - multi_family_ac_efficiency_improvement_factor
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: multi_family_building_cooling_with_ac

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Inverter air conditioners use a variable speed compressor instead of the fixed-speed compressor found in traditional models. A fixed-speed compressor operates at a constant speed, either running at full capacity or completely shutting off. On the other hand, an inverter compressor can adjust its speed and capacity based on the cooling load. This allows the inverter air conditioner to modulate its cooling output and match it precisely to the required cooling demand, resulting in better energy efficiency. Other advantages of this technology are: precise temperature control, quick cooling, and startup time, enhanced comfort, quieter operation and longer lifespan.




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
