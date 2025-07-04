---
title: T-5A2-TE-2 - Update imported district heat grid emission factor
id: imported_grid_district_heat_emission_factor
sector: energy
sustainability: amber
progress: 10
class: transition
version: 2.0.0
name: imported_grid_district_heat_emission_factor
type: supplyUpdate
longName: 'Alter the emission factor of imported district heat grid'
shortName: 'Imported district heat emission factor'
description: 'Alter the emission factor (grams of carbon dioxide equivalent per kilowatt-hour) for the district heat grid'
unitOfMeasure: g_co2e_kwh
cohort:
  expression: '1'
variableToUpdate: emission_factor_imported_grid_district_heating_kwh_to_co2e
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: imported_grid_district_heat

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

TBD




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
