---
title: T-1A1c-TE-1 - Biofuel for diesel buses
id: biofuel_for_diesel_buses
sector: transport
sustainability: amber
progress: 50
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: biofuel_for_diesel_buses
type: resourceShift
longName: 'Alter the proportion of HVO biodiesel in diesel for buses.'
shortName: 'Biofuel diesel buses'
description: 'Increase the proportion of biodiesel in diesel'
unitOfMeasure: percent
cohort:
  expression: '1'
resourcesToUpdate:
  from: resource_proportion_diesel_buses
  to: resource_proportion_biodiesel_buses
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_buses
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
