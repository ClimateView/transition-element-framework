---
title: T-2B1-TE-1 - Biogas in methane reforming for ammonia production
id: biogas_in_methane_reforming_for_ammonia_production
sector: industry
sustainability: amber
class: transition
type: resourceShift
longName: 'Alter the proportion of biogas in methane reforming for ammonia production'
shortName: 'Biogas in ammonia'
name: biogas_in_methane_reforming_for_ammonia_production                
version: 2.0.0
unitOfMeasure: percent
cohort:
  expression: '1'
resourcesToUpdate:
  from: resource_proportion_natural_gas_reforming_for_ammonia_production
  to: resource_proportion_biogas_reforming_for_ammonia_production
carbonCausalChains:
  atoc:
    expression: '1'
  chains:
  - chain: reforming_of_methane_for_ammonia_production
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
