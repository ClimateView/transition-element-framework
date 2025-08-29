---
title: T-1A4-TE-5 - Shift to electric marine passenger transportion
id: electrification_of_domestic_sea_passenger_transport
sector: transport
sustainability: green
progress: 25
class: transition
version: 2.0.1
ipccMitigationMethod: 1c-02-electric-technologies-shipping
name: electrification_of_domestic_sea_passenger_transport
type: shift
longName: Shift from conventional fueled to electric marine passenger transport.
shortName: Electric marine passenger transport
description: Shift person kilometer from ship passenger to electric shipping passenger in person kilometer to fulfill the need of mobility
unitOfMeasure: person_km
cohort:
  expression: '1'
shiftFrom:
  atoc:
    expression: '1'
  chains:
  - chain: ship_passenger
  - chain: gas_oil_shipping_passenger
shiftTo:
  atoc:
    expression: '1'
  chains:
  - chain: electric_shipping_passenger
cobenefits:
- air_quality
- reduced_noise
---
TBD

{{ te_sustainability() }}

# Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

TBD



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
