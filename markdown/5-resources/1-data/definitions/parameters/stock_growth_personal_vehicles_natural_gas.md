---
id: stock_growth_personal_vehicles_natural_gas
title: Growth of personal vehicles (CNG) operation
type: parameter
parameter_type: GROWTH_FACTOR
unit: vehicle_km_percapita
tags:
  - operations_growth
values:
  - value: 0
    global: True
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Per capita based on UK national statistics
    reference: https://climateview.slab.com/public/ranizl8z
  - value: 0
    country: CA
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Model description ClimateView - Canada -  Personal Transportation
    reference: https://climateview.slab.com/public/ird2eslu
  - value: 0
    country: CH
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Für Schätzungen basierend auf deutschen Daten, siehe Dokumentation.
    reference: https://climateview.slab.com/public/piy3mcng
  - value: 0
    country: DE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Für geschätzte Werte, siehe Dokumentation
    reference: https://climateview.slab.com/public/piy3mcng
  - value: 26.6181
    country: ES
    scalingType: CONSTANT
    validFrom: 2020-01-01
    comment: |
        Calculations based on national Spanish data.
    reference: https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#h5v39-cars
  - value: 30.6589
    country: FR
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Valeur basée sur les statistiques nationales
    reference: https://climateview.slab.com/posts/road-transport-france-eoxjg43o#h28f9-tableau-2-vehicules-personnels
  - value: 0
    country: GB
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        For estimates based on national statistics, see documentation.
    reference: https://climateview.slab.com/public/ranizl8z
  - value: 0
    country: SE
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        För värden baserade på nationell statistik (TRAFA), se dokumentation.
    reference: https://climateview.slab.com/public/81gb14xu
  - value: 0
    country: US
    scalingType: CONSTANT
    validFrom: 2019-01-01
    comment: |
        Value based on US national statistics.
    reference: https://climateview.slab.com/posts/personal-transportation-wtgg2hlu#hu3m2-table-2-distances-travelled-by-cars
---


Unit of measure: `{{unit}}`


# Values


| Value | Region | Scaling | Period | Comment | Reference |
|-------|--------|---------|--------|---------|-----------|
| 0 | Global | CONSTANT | 2019-01-01 | Per capita based on UK national statistics | https://climateview.slab.com/public/ranizl8z |
| 0 | CA | CONSTANT | 2019-01-01 | Model description ClimateView - Canada -  Personal Transportation | https://climateview.slab.com/public/ird2eslu |
| 0 | CH | CONSTANT | 2019-01-01 | Für Schätzungen basierend auf deutschen Daten, siehe Dokumentation. | https://climateview.slab.com/public/piy3mcng |
| 0 | DE | CONSTANT | 2019-01-01 | Für geschätzte Werte, siehe Dokumentation | https://climateview.slab.com/public/piy3mcng |
| 26.6181 | ES | CONSTANT | 2020-01-01 | Calculations based on national Spanish data. | https://climateview.slab.com/posts/transporte-por-carretera-road-transport-esqm8w27#h5v39-cars |
| 30.6589 | FR | CONSTANT | 2019-01-01 | Valeur basée sur les statistiques nationales | https://climateview.slab.com/posts/road-transport-france-eoxjg43o#h28f9-tableau-2-vehicules-personnels |
| 0 | GB | CONSTANT | 2019-01-01 | For estimates based on national statistics, see documentation. | https://climateview.slab.com/public/ranizl8z |
| 0 | SE | CONSTANT | 2019-01-01 | För värden baserade på nationell statistik (TRAFA), se dokumentation. | https://climateview.slab.com/public/81gb14xu |
| 0 | US | CONSTANT | 2019-01-01 | Value based on US national statistics. | https://climateview.slab.com/posts/personal-transportation-wtgg2hlu#hu3m2-table-2-distances-travelled-by-cars |


