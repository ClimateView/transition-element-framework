---
title: E-1A3b - Road Transportation
---

This category can be further broken down for reporting purposes into emissions from:

- `1A3b.i` - Cars
	- `1A3b.i1` - Passenger cars with 3-way catalysts
	- `1A3b.i2` - Passenger cars without 3-way catalysts
- `1A3b.ii` - Light duty trucks
	- `1A3b.ii1` - Light duty trucks with 3-way catalysts
	- `1A3b.ii2` - Light duty trucks without 3-way catalysts
- `1A3b.iii` - Heavy duty trucks and buses
- `1A3b.iv` - Motorcycles (including mopeds, scooters, and three-wheelers)
- `1A3b.v` - Evaporative emissions from vehicles
- `1A3bv.i` - Urea-based catalysts



# Emissions

Emissions for road transportation are defined by the IPCC in section 3.2 of Volume 2 of [@egglestonh.s.2006IPCCGuidelines2006]. 

Emission reporting for road transport can be further broken down into:

- $\ce{CO2}$ emissions (from combustion)
- $\ce{CO2}$ emissions from urea-based catalysts
- $\ce{CH4}$ and $\ce{N2O}$ emissions

They can be estimated from either:

- Fuel consumption (tiers 1 and 2); or
- Vehicle kilometers travelled (tier 3)

## $\ce{CO2}$ emissions

### Tier 1

Emissions are calculated per fuel type ($a$) based on the parameter $Fuel_a$ = quantity of fuel sold, measured in $TJ$.

$$Emission = \sum_{a}[Fuel_a * EF_a] $$

Where:

$$
\begin{array}{rll}
Emission &=& \text{Emissions of} \; CO_2 \; &\; (kg) \\
Fuel_a &=& \text{fuel sold} &\; (TJ) \\
EF_a &=& \text{emission factor} &\; (kg/TJ) \\
a &=& \text{type of fuel}
\end{array}
$$


Emission factors calculated as the carbon content of the fuel multiplied by $44/12$ and are summarised in table 3.2.1 of [@egglestonh.s.2006IPCCGuidelines2006]:

| Fuel Type                 | $\ce{CO2}$ Emission Factors $(kg/TJ)$ |
| ------------------------- | ------------------------------------- |
| Motor Gasoline            | 69 300                                |
| Gas / Diesel Oil          | 74 100                                |
| Liquefied Petroleum Gases | 63 100                                |
| Kerosene                  | 71 900                                |
| Lubricants                | 73 300                                |
| Compressed Natural Gas    | 56 100                                |
| Liquefied Natural Gas     | 56 100                                |


### Tier 2
Tier 2 calculations use the same equation as for tier 1, however country-specific carbon content per fuel type are used to determine emission factors, instead of relying on the global average values as used in tier 1.


### Tier 3

The IPCC does not provide a tier 3 approach for estimating emissions of $\ce{CO2}$ for road transport. This is because, for reporting purposes, it is difficult to improve on the tier 2 equations that use direct fuel consumption data.

A tier 3 approach of estimating emissions from Vehicle Kilometers Travelled (VKT) would be less accurate than the tier 1 and 2 approaches. However, when considering mitigation options, then estimating VKT may be considered an improvement over tier 1 and 2.


## $\ce{CO2}$ emissions from urea-based catalysts

Emissions from the use of urea-based additives are not described with the tier approach, the IPCC present only the following consumption based equation:

$$Emission = Activity \cdot \frac{12}{60} \cdot Purity \cdot \frac{44}{12} $$

Where:

$$
\begin{array}{rll}
Emission &=& \text{emissions of} \; \ce{CO2} &\; (kg) \\
Activity &=& \text{amount of additive consumed} &\; (Gg) \\
Purity &=& \text{perctantage purity of additive} &\;  \\
\end{array}
$$



## $\ce{CH4}$ and $\ce{N2O}$ emissions

$\ce{CH4}$ and $\ce{N2O}$ emissions are harder to estimate and depend largely on factors such as the distribution of emission control technology in the fleet. For this reason, tier 2 and 3 methods address variations in the fleet as well as driving conditions.

Note: while $\ce{CO2}$ emissions from biofuels are not required by the IPCC for reporting national totals (as they are biogenic), $\ce{CH4}$ and $\ce{N2O}$ emissions from biofuels are considered anthropogenic and should be reported.


### Tier 1
This approach follows the tier 1 approach for  $\ce{CO2}$ emissions and is base on fuel consumption data, broken down by fuel type:

$$Emission = \sum_{a}[Fuel_a * EF_a] $$

Where:

$$
\begin{array}{rll}
Emission &=& \text{emissions}        &\; (kg) \\
Fuel_a   &=& \text{fuel sold}       &\; (TJ) \\
EF_a     &=& \text{emission factor} &\; (kg/TJ) \\
a        &=& \text{type of fuel}    &\; 
\end{array}
$$


### Tier 2
Tier 2 further breaks down fuel consumption by vehicle type and emission control technology:

$$Emission = \sum_{a,b,c}[Fuel_{a,b,c} * EF_{a,b,c}] $$

Where:

$$
\begin{array}{rll}
Emission &=& \text{emissions}   &\; (kg) \\
Fuel_a &=& \text{fuel sold} &\; (TJ) \\
EF_a &=& \text{emission factor} &\; (kg/TJ) \\
a &=& \text{type of fuel}\\
b &=& \text{type of vehicle}\\
c &=& \text{type of emission control technology}
\end{array}
$$


### Tier 3
Tier 3 improves on the lower tiers by using Vehicle Kilometers Travelled, as well as roughly accounting for the cold-start phase:


$$Emission = \sum_{a,b,c,d}[Distance_{a,b,c,d} \cdot EF_{a,b,c,d}] + \sum_{a,b,c,d}C$$

Where:

$$
\begin{array}{rll}
Emission &=& \text{emissions}   &\; (kg) \\
Distance_{a,b,c,d} &=& \text{distance travelled (VKT)} &\; (km) \\
EF_{a,b,c,d} &=& \text{emission factor} &\; (kg/km) \\
C_{a,b,c,d} &=& \text{cold start emissions} &\; (kg) \\
a &=& \text{type of fuel}\\
b &=& \text{type of vehicle}\\
c &=& \text{type of emission control technology}\\
d &=& \text{type of operating conditions}
\end{array}
$$


The cold-start phase is roughly estimated to the first 3km travelled per journey and takes into account the fact that catalysts only start to operate when engine temperatures reach 300 C.



# Mitigation

For mitigation strategies see [M-1A - Land-based Transport](/2-ipcc-mitigation-options/1-transport/1a-land-based-transport/index.md).








