---
title: T-1B4b-TE-4 - Biofuel for marine freight transport
id: biofuels_for_sea_freight_transport
sector: transport
sustainability: amber
class: transition
version: 2.0.1
name: biofuels_for_sea_freight_transport
type: resourceShift
longName: Alter the proportion of biomarine diesel in marine diesel for marine freight transport.
shortName: Biofuel marine freight transport
description: Increase the proportion of marine biodiesel in marine diesel
unitOfMeasure: percent
cohort:
  expression: '1'
resourcesToUpdate:
  from: resource_proportion_marine_diesel
  to: resource_proportion_marine_biodiesel
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: ship_freight
cobenefits:
- air_quality
---
TBD

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Sustainable biofuels are produced from biomass, such as arable crops, food waste or residues from the forest industry. Since biomass has accumulated carbon dioxide from the atmosphere during its growth, and release emissions during natural degradation in any case, emissions from biofuels are assumed to be zero.




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
