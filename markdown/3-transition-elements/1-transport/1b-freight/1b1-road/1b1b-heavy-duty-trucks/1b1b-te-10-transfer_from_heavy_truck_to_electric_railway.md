---
title: T-1B1b-TE-10 - Shift from heavy truck to electric railway
id: transfer_from_heavy_truck_to_electric_railway
sector: transport
sustainability: green
class: transition
version: 2.0.1
ipccMitigationMethod: 1a-12-electric-technologies
name: transfer_from_heavy_truck_to_electric_railway
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) heavy truck to electric rail freight transport.'
shortName: 'Heavy truck to electric rail'
description: 'Shift tonne kilometer from diesel heavy trucks to electric rail freight in tonne kilometer to fulfill the need of logistics'
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
  - chain: electric_rail_freight
cobenefits:
- air_quality
- reduced_noise
- reduced_accidents
- less_congestion

---



# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Railways are highly efficient in moving goods. Trains with electric propulsion cause the lowest amount of emissions, but diesel-powered trains are also significantly more efficient than diesel trucks.

Railways are highly efficient in moving goods. Trains with electric propulsion cause the lowest amount of emissions, but diesel-powered trains are also significantly more efficent than diesel trucks.

UK rail freight(excluding coal) has inreased over the past decade, to almost 70 million tonnes.

Source: Understanding the UK Freight Transport System, Government Office for Science


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
