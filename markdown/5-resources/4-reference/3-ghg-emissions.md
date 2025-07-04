---
title: GHG Emissions
---

References to GHG emission statistics throughout this site come from [Climate Watch](https://www.climatewatchdata.org/ghg-emissions). 

Climate Watch provides raw data for "GHG Emissions from Fuel Combustion" that is adapted from IEA data. Climate Watch have chosen not to reallocate fuel combustion data into end-use sectors - as a consequence the energy sector accounts for approximately 75% of emissions.

The Transition Element Framework has opted to reallocate fuel combustion to the relevant sectors using data available from [World Greenhouse Gas Emissions in 2020](https://www.wri.org/data/world-greenhouse-gas-emissions-2020), a Sankey diagram created by World Resources Institute. This data source visualises the allocation of fuel combustion to end-use sectors and sub-sectors that closely match the TEF hierarchy.


# Method
The total GHG emission estimate used by this website has been taken directly from Climate Watch data using the following filter:

- Data Source: "Climate Watch"
- Location: "WORLD"
- Year: 2020
- Sector: "Total including LUCF" 

This gave total emissions as 47,463 MtCO₂-eq. 

2020 was chosen as the year in order to align with the Sankey diagram data. We were unable to find source data or a method description for the diagram and instead elected to use the raw percentage data used for rendering the diagram. Method descriptions for both Climate Watch Data [@geClimateWatchCountry2024] and the first version of World Resources Institutes sankey allocation [@herzogNavigatingNumbers2005]. 

The Sankey diagram sub-sectors were mapped to our TEF hierarchy as follows:

- Transport:
	- Air
	- Rail
	- Road
	- Ship
	- Other Transportation
	-  Pipeline
- Industry:
	- Cement
	- Chemical and petrochemical
	- Electric Power Systems
	- Electronics
	- Food and tobacco
	- Iron and steel
	- Machinery
	- Mining and quarrying
	- Non-ferrous metals
	- Non-metallic minerals
	- Other Industry
	- Paper, pulp and printing
	- Textile and leather
	- Transport equipment
- AFOLU
	- Agriculture & Fishing Energy Use"
    - Agriculture Soils
	- Burning
    - Drained organic soils
    - Fires in organic soils
    - Forest Land
    - Forest fires
    - Livestock & Manure
    - Rice Cultivation
    - Wood and wood products
- Buildings:
	- Commercial Buildings
	- Construction
	- Residential Buildings
- Energy:
	- Flared
	- Production
	- Transmission and distribution
	- Unallocated Fuel Combustion
	- Vented
- Waste:
	- Landfills
	- Other Waste
	- Wastewater


# Emission estimates

Combining the total emission figure with percentage data gives total emissions for each TEF sector:

| Sector    | MtCO₂-eq      | Proportion |
| --------- | ------------- | ---------- |
| Transport | 7,499.18      | 15.80%     |
| Industry  | 14,860.24     | 31.31%     |
| AFOLU     | 8,220.15      | 17.32%     |
| Buildings | 8,870.39      | 18.69%     |
| Energy    | 6,362.91      | 13.41%     |
| Waste     | 1,651.72      | 3.48%      |
| **Total** | **47,463.17** |            |

In addition to GHG emissions measured in CO₂-eq the Sankey data provides a mapping to specific gasses also measured in MtCO₂-eq:




| Sector    | CO₂           | CH₄         | N₂O          | F-Gases      | Total         |
| --------- | ------------- | ------------ | ------------ | ------------ | ------------- |
| Transport | 7,309.8       | 43.19        | 146.19       | 0            | 7,499.18      |
| Industry  | 13,324.33     | 21.36        | 292.37       | 1,222.18     | 14,860.24     |
| AFOLU     | 2,106.89      | 3,667.00     | 2,446.25     | 0            | 8,220.15      |
| Buildings | 8,599.38      | 259.15       | 11.86        | 0            | 8,870.39      |
| Energy    | 3,262.14      | 3,041.44     | 59.33        | 0            | 6,362.91      |
| Waste     | 0             | 1506.48      | 145.24       | 0            | 1,651.72      |
| **Total** | **34,602.55** | **8,538.62** | **3,101.24** | **1,222.18** | **47,463.17** |


