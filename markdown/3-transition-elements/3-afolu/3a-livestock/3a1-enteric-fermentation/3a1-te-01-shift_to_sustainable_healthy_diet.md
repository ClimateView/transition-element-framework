---
title: T-3A1-TE-1 - Shift to Sustainable Healthy Diets
id: shift_to_sustainable_healthy_diet
sector: afolu
sustainability: amber
ipccMitigationMethod: 3c-02-shift-sustainable-healthy-diets
class: transition
progress: 25
elements:
  - upshift: shift_to_sustainable_healthy_diet
    version: 1.0.0
    unitOfMeasure: meat_consumed
    cohort:
      expression: "1"
    variablesToUpdate:
      - update: meat_proportion_in_diet
        type: SAVINGS
        by:
          expression: "%[0]"
          variables:
            - reduction_meat_proportion
    carbonCausalChains:
      atoc:
        expression: "%[0]"
        variables:
          - meat_proportion_in_diet
      chains:
        - chain: enteric_fermentation_cattle
        - chain: enteric_fermentation_sheep
        - chain: enteric_fermentation_swine
        - chain: enteric_fermentation_other_livestock
---

This Transition Element is the shift from animal based diets to plant based diets.

# Background

This transition element models the mitigation options and potentials outlined in {{ ipcc_mitigation_link() }}.


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
