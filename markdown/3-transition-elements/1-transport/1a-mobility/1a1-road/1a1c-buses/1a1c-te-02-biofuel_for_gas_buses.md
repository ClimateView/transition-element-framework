---
title: T-1A1c-TE-2 - Biofuel for gas buses
id: biofuel_for_gas_buses
sector: transport
sustainability: amber
progress: 50
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: biofuel_for_gas_buses
type: resourceShift
longName: 'Alter the proportion of compressed biogas (CBG) in compressed natural gas (CNG) for buses.'
shortName: 'Biofuel CNG buses'
description: 'Increase the proportion of biogas in gas mix'
unitOfMeasure: percent
cohort:
  expression: '1'
resourcesToUpdate:
  from: resource_proportion_natural_gas_gasbus
  to: resource_proportion_biogas_gasbus
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: gas_buses
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
