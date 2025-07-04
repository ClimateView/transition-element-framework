---
title: T-1A3-TE-1 - Biofuel for air passenger transport
id: biofuels_for_air_transport
sector: transport
sustainability: amber
progress: 25
class: transition
version: 2.0.0
ipccMitigationMethod: 1b-02-alternative-fuels-aircraft
name: biofuels_for_air_transport
type: resourceShift
longName: 'Alter the proportion of bio-turbine fuel in turbine fuel for air passenger transport.'
shortName: 'Biofuel air transport'
description: 'Increase the proportion of aviation biofuel in aviation turbine fuel'
unitOfMeasure: percent
cohort:
  expression: '1'
resourcesToUpdate:
  from: resource_proportion_aviation_turbine_fuel
  to: resource_proportion_aviation_biofuel
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: passenger_transportation_by_air
cobenefits:
- expand_stock_lifetime

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Sustainable biofuels are produced from biomass, such as arable crops, food waste or residues from the forest industry. Since biomass has accumulated carbon dioxide from the atmosphere during its growth, and release emissions during natural degradation in any case, emissions from biofuels are assumed to be zero. However, biofuel-powered aircraft still cause climate impact through the high-altitude effect on longer flights.

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
