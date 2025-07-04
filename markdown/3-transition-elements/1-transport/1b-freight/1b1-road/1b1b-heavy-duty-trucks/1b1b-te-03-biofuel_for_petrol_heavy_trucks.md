---
title: T-1B1b-TE-3 - Biofuel for petrol heavy trucks
id: biofuel_for_petrol_heavy_trucks
sector: transport
sustainability: amber
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: biofuel_for_petrol_heavy_trucks
type: resourceShift
longName: 'Alter the proportion of ethanol in petrol for heavy trucks.'
shortName: 'Biofuel petrol heavy trucks'
description: 'Increase the proportion of ethanol in petrol'
unitOfMeasure: percent
cohort:
  expression: '1'
resourcesToUpdate:
  from: resource_proportion_petrol_heavy_trucks
  to: resource_proportion_ethanol_heavy_trucks
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: petrol_heavy_trucks
cobenefits:
- air_quality

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Sustainable biofuels are produced from biomass, such as arable crops, food waste or residues from the forest industry. Since biomass has accumulated carbon dioxide from the atmosphere during its growth, and release emissions during natural degradation in any case, emissions from biofuels are assumed to be zero. However, biofuel vehicles still cause particulate emissions.




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
