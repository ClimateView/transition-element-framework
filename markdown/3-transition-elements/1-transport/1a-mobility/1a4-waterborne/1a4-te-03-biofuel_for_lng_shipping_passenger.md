---
title: T-1A4-TE-3 - Biofuel for LNG marine passenger transport
id: biofuel_for_lng_shipping_passenger
sector: transport
sustainability: amber
progress: 30
class: transition
version: 2.0.0
ipccMitigationMethod: 1c-01-alternative-fuels-shipping
name: biofuel_for_lng_shipping_passenger
type: resourceShift
longName: 'Alter the proportion of LBG in LNG for marine passenger transport.'
shortName: 'Biofuel LNG marine passenger transport'
description: 'Increase the proportion of liquefied biogas in liquefied gas mix'
unitOfMeasure: percent
cohort:
  expression: '1'
resourcesToUpdate:
  from: resource_proportion_liquefied_natural_gas_shipping_passenger
  to: resource_proportion_liquefied_bio_gas_shipping_passenger
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: lng_shipping_passenger
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
