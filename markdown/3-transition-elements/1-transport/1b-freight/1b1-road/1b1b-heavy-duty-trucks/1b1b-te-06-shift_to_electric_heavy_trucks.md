---
title: T-1B1b-TE-6 - Shift to electric heavy trucks
id: shift_to_electric_heavy_trucks
sector: transport
sustainability: green
class: transition
version: 2.0.1
ipccMitigationMethod: 1a-12-electric-technologies
name: shift_to_electric_heavy_trucks
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) heavy trucks to electric heavy trucks.'
shortName: 'Electric heavy trucks'
description: 'Shift tonne kilometer from diesel heavy trucks to battery electric heavy trucks in tonne kilometer to fulfill the need of logistics'
unitOfMeasure: tonne_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: diesel_heavy_trucks
  - chain: petrol_heavy_trucks
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: battery_electric_heavy_trucks
cobenefits:
- air_quality
- reduced_noise

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Electric vehicles have zero tailpipe emissions. They are also significantly more energy efficient and quiet than fossil-fueled vehicles. The shift to electric trucks reduces greenhouse gas emissions and helps create a better urban environment.




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
