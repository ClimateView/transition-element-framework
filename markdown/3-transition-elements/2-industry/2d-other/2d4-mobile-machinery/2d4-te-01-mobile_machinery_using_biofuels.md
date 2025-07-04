---
title: T-2D4-TE-1 - Shift to biofuel for mobile machinery
id: mobile_machinery_using_biofuels
sector: industry
sustainability: green
progress: 25
class: transition
version: 2.0.1
name: mobile_machinery_using_biofuels
type: shift
longName: 'Shift from diesel mobile machinery to biofuel mobile machinery.'
shortName: 'Biofuel machinery'
description: 'Shift kilowatt-hours from mobile machinery diesel to mobile machinery biofuel in kilowatt-hour to fulfill the need of productivity'
unitOfMeasure: kwh
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: mobile_machinery_diesel
  - chain: mobile_machinery_petrol
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: mobile_machinery_biofuel
cobenefits:
- air_quality
- increased_longevity_of_stock

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Fossil fuels used for mobile machinery are being replaced by sustainably produced biofuels. The potential for this is great, as there are biodiesel that can be used in diesel engines without any modifications being necessary. Biodiesel is also blended into regular diesel to reduce its climate impact.




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
