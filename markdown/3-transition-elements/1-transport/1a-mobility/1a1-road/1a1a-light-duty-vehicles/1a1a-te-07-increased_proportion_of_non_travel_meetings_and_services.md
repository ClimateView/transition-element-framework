---
title: T-1A1a-TE-7 - Shift to online meetings and services
id: increased_proportion_of_non_travel_meetings_and_services
sector: transport
sustainability: green
progress: 50
class: transition
version: 2.0.1
ipccMitigationMethod: 1a-06-teleworking
name: increased_proportion_of_non_travel_meetings_and_services
type: shift
longName: 'Shift from Internal Combustion Engine (ICE) cars to online meetings and services.'
shortName: 'Online meetings'
description: 'Shift vehicle kilometer from petrol, diesel, LPG and gas vehicles to e-meetings in hours to fulfill the need of business trips'
unitOfMeasure: business_meetings
cohort:
  expression: ( %[0] * %[1] * %[2] * %[3] * %[4] * %[5] * atoc_lhs ) / ( %[6] + %[7] )
  variables:
  - population
  - proportion_working
  - proportion_office_workers
  - proportion_business_travellers
  - external_meetings
  - workingdays_per_year
  - stock_personal_vehicles_petrol
  - stock_personal_vehicles_diesel
shiftFrom:
  atoc:
    expression: '%[0]'
    variables:
    - mileage_external_meeting
  chains:
  - chain: petrol_vehicles
  - chain: diesel_vehicles
  - chain: lpg_vehicles
  - chain: gas_vehicles
shiftTo:
  atoc:
    expression: '%[0] * %[1]'
    variables:
    - meeting_length
    - bandwidth_usage_video_conference
  chains:
  - chain: e_meetings
cobenefits:
- air_quality
- reduced_noise
- reduced_accidents
- less_congestion

---


#  Background

IPCC WG3 definition: {{ ipcc_mitigation_link() }}.

Digital technologies are making it more viable for people to work from home. This has the potential to reduce the amount of daily office commutes by car - as well as longer-distance business trips by car or airplane.

Digital technologies are making it more viable for people to work from home. This has the potential to reduce the amount of daily office commutes by car - as well as longer-distance business trips by car or airplane.

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
