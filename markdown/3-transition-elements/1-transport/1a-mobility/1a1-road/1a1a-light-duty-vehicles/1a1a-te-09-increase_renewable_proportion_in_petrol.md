---
title: T-1A1a-TE-9 - Biofuel for petrol cars
id: increase_renewable_proportion_in_petrol
sector: transport
sustainability: amber
progress: 50
class: transition
version: 2.0.0
ipccMitigationMethod: 1a-11-alternative-fuels-vehicles
name: increase_renewable_proportion_in_petrol
type: resourceShift
longName: 'Alter the proportion of ethanol in petrol for cars.'
shortName: 'Biofuel petrol cars'
description: 'Increase the proportion of ethanol in petrol'
unitOfMeasure: percent
cohort:
  expression: '1'
resourcesToUpdate:
  from: resource_proportion_petrol
  to: resource_proportion_ethanol
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: petrol_vehicles

---


#  Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Sustainable biofuels such as ethanol are produced from biomass, such as arable crops, food waste or residues from the forest industry. Since biomass has accumulated carbon dioxide from the atmosphere during its growth, and release emissions during natural degradation in any case, emissions from biofuels are assumed to be zero. However, biofuel vehicles still cause particulate emissions.

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
