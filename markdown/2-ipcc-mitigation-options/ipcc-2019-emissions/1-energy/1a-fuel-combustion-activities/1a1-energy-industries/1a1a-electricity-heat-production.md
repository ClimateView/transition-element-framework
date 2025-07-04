---
title: E-1A1a - Main Activity Electricity and Heat Production
id: 1a1a-electricity-heat-production
---

This category can be further broken down for reporting purposes into emissions from:

- `1A1a.i` - Electricity Generation
- `1A1a.ii` - Combined Heat and Power Generation (CHP)
- `1A1a.iii` - Heat Plants


# Emissions

## Tier 1

The tier 1 approach for stationary combustion is to estimate the entire fuel consumption for each type of fuel. This estimate is then combined with a default emission factor for each fuel type.


Emissions for _public electricity and heat production_ are estimated as:

$$Emissions_{GHG,fuel} = Fuel \, Consumption_{fuel} \cdot  Emission \, Factor_{GHG,fuel}$$

Where:

$$
\begin{array}{rll}
\text{Emissions}_{GHG,fuel} &=& \text{emissions of a GHG by fuel type} & (\text{kg GHG}) \\
\text{Fuel Consumption}_{fuel} &=& \text{quantity of fuel combusted} & (\text{TJ}) \\
\text{Emission Factor}_{GHG,fuel} &=& \text{default emission factor for GHG and fuel type}  & (\text{kg} \, \ce{CO2} \, / \, \text{KJ})
\end{array}
$$

Total emissions for _public electricity and heat production_ can then be calculate as:

$$
Emissions_{GHG} = \sum_{fuels} Emissions_{GHG,fuel}
$$


## Tier 2

The tier 2 approach expands upon tier 1 by using country-specific emission factor(s) for each fuel type.



## Tier 3




Emissions for _public electricity and heat production_ are estimated as:

$$Emissions_{GHG,fuel,technology} = Fuel \, Consumption_{fuel,technology} \cdot  Emission \, Factor_{GHG,fuel,technology}$$

Where:

$$
\begin{array}{rll}
\text{Emissions}_{GHG,fuel,technology} &=& \text{emissions of a GHG by fuel and technology} & (\text{kg GHG}) \\
\text{Fuel Consumption}_{fuel,technology} &=& \text{quantity of fuel combusted} & (\text{TJ}) \\
\text{Emission Factor}_{GHG,fuel,technology} &=& \text{default emission factor for GHG and fuel type}  & (\text{kg} \, \ce{CO2} \, / \, \text{KJ})
\end{array}
$$

Total emissions for _public electricity and heat production_ can then be calculate as:

$$
Emissions_{GHG} = \sum_{fuels} Emissions_{GHG,fuel}
$$








