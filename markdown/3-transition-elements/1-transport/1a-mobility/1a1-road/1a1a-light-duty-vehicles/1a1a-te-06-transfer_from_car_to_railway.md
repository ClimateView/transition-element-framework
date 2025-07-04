---
title: T-1A1a-TE-6 - Shift from car to railway
id: transfer_from_car_to_railway
sector: transport
sustainability: green
progress: 50
class: transition
version: 2.0.2
ipccMitigationMethod: 1a-03-public-transit
name: transfer_from_car_to_railway
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) cars to electric rail passenger transport.'
shortName: 'Car to railway'
description: 'Shift vehicle kilometer from petrol, diesel, LPG and gas vehicles to electric rail in person kilometer to fulfill the need of mobility'
unitOfMeasure: person_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: 1 / %[0]
    variables:
    - load_factor_car_average
  chains:
  - chain: petrol_vehicles
  - chain: diesel_vehicles
  - chain: lpg_vehicles
  - chain: gas_vehicles
shiftTo:
  atoc:
    expression: 1 + %[0]
    variables:
    - distance_increase_car_to_train_long_journey
  chains:
  - chain: electric_rail
cobenefits:
- air_quality
- reduced_noise
- reduced_accidents
- less_congestion

---


#  Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Railways are a highly efficient mode of transport. Regardless of fuel source, railways generate significantly less emissions than passenger transport by car.

Railways are a highly efficient mode of transport. Regardless of fuel source, railways generate significantly less emissions emissions than passenger transport by car.
Replacing longer - distance car trips with railways will not only reduce greenhouse gas emissions but also air and noise pollution.

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
