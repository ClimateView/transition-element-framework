---
title: T-1B1a-TE-6 - Shift to electric light trucks
id: electric_light_trucks
sector: transport
sustainability: green
class: transition
version: 2.0.1
name: electric_light_trucks
ipccMitigationMethod: 1a-12-electric-technologies
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) light trucks to electric light trucks.'
shortName: 'Electric light trucks'
description: 'Shift vehicle kilometer from diesel light trucks to battery electric light trucks in vehicle kilometer to fulfill the need of logistics'
unitOfMeasure: vehicle_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_light_trucks
  - chain: petrol_light_trucks
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: battery_electric_light_trucks
cobenefits:
- air_quality
- reduced_noise

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Electric trucks cause no tailpipe emissions, thereby directly reducing both greenhouse gas emissions and particulate emissions. Electric trucks also produce less noise, helping to improve the general urban environment.Electric trucks cause more emissions in the production phase than internal combustion engine cars, but cause fewer emissions over the lifetime of the car.

Electric trucks cause no tailpipe emissions, thereby directly reducing both greenhouse gas emissions and particulate emissions. Electric trucks also produce less noise, helping to improve the general urban environment.

Electric trucks cause more emissions in the production phase than internal combustion engine cars, but cause less emissions over the lifetime of the car.


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
