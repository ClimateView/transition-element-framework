---
title: E-3A1a - Cattle
---

# Categories

This page covers the following emission source categories and subcategories:

- Cattle and Buffalo
	- Mature dairy cows or buffalo
		- High-producing cows
		- Low-producing cows
	- Other mature cattle or non-dairy buffalo
		- Females
			- Cows used to produce offspring for meat
			- Cows used for more than one production purpose
		- Males
			- Bulls used for breeding purposes
			- Bullocks used for draft power
	- Growing cattle or buffalo
		- Calves pre-weaning
		- Replacement dairy heifers
		- Growing / fattening cattle
		- Feedlot-fed cattle

# Population
Section 10.2 of [@buendia2019Refinement20062019] outlines methods for calculating livestock population and feed characterisation. 

All emission calculations for cattle are based on the number of livestock ($N$) which can be calculated as:


$$N = Days\_alive \cdot \left[ \frac{NAPA}{365} \right] $$


Where:

$$
\begin{array}{rll}
N &=& \text{number of head of livestock} &\;  \\
NAPA &=& \text{number of animals produced annually} &\;
\end{array}
$$

A "tier 2" method for calculating population can be considered if information is available for population for individual source subcategories.

# Emissions

Emissions from livestock can be estimated using one of the following tiers

- Tier 1: emissions calculated per head of livestock
- Tier 1a: emissions calculated per head of livestock per productivity system
- Tier 2: emissions calculated based on gross energy intake of livestock
- Simplified Tier 2: emissions calculated based on Dry Matter Intake (DMI)
- Tier 3: for countries where cattle livestock is particularly important, sophisticated models that consider diet composition in detail

IPCC *suggests* tier 2 or 3 as the inventory method for cattle [@buendia2019Refinement20062019]. Our interpretation is that tier 1 may be sufficient for countries where cattle livestock activity is low. For tier 3 exact calculation methods are not provided by the IPCC.

> [!note]
> The distinction between "1" vs "1a" and "2" vs "2a" is the degree of complexity or simplification of method within the tier. In both cases the more advanced method is the often the recommended approach. 

## Tier 1a

Tier 1a emissions are calculated per livestock type and productivity system, expressed as:

$$E_T = \sum_{P}EF_{(T,P)} \cdot \left[ \frac{N_{(T,P)}}{10^6} \right] $$

Where:


$$
\begin{array}{rll}
E_T &=& \text{Emissions of} \; CH_4 \; & (Gg \; CH_4 \; yr^-1) \\
EF_{(T,P)} &=& \text{emission factor} &\; (kg \; CH_4 \; head^-1 \; yr^-1 ) \\
N_{(T,P)} &=& \text{number of livestock} &\;  \\
T &=& \text{livestock species / category} &\; \\
P &=& \text{productivity system} &\; (high,low)
\end{array}
$$


Livestock categories and productivity systems:

- Dairy Cattle
	- High productivity
	- Low productivity
- Other cattle
	- High productivity
	- Low productivity
- Buffalo


### Emission Factors

Emission factors for Tier 1a for cattle are provided in @buendia2019Refinement20062019 per region in Table 10.11.


## Tier 1

Tier 1 emissions are a simplification of tier 1a and are calculated per livestock type and do not differentiate productivity systems, expressed as:



$$E_T = EF_{T} \cdot \left[ \frac{N_{T}}{10^6} \right] $$

Where:


$$
\begin{array}{rll}
E_T &=& \text{Emissions of} \; CH_4 \; & (Gg \; CH_4 \; yr^-1) \\
EF_{T} &=& \text{emission factor} &\; (kg \; CH_4 \; head^-1 \; yr^-1 ) \\
N_{T} &=& \text{number of livestock} &\;  \\
T &=& \text{livestock species / category} &\; \\
\end{array}
$$


Livestock categories:

- Dairy Cattle
- Other cattle
- Buffalo


## Tier 2

The Tier 2 approach builds upon Tier 1 by using  gross energy intake in order to determine a more accurate emission factor using:



$$EF = \frac{GE \cdot \left( \frac{Y_m}{100} \right) \cdot 365 }{55.65} $$

Where:


$$
\begin{array}{rll}
EF &=& \text{emission factor} &\; (kg \; CH_4 \; head^-1 \; yr^-1 ) \\
GE &=& \text{gross energy intake} &\; (MJ \; head^-1 \; day^-1) \\
Y_m &=& \text{methane conversion factor} &\;  
\end{array}
$$

The methane conversion factor is measured as a percent of gross energy in feed converted to methane. The factor $55.65 (MJ/kg \; CH_4)$ is the energy content of methane.

For cattle $Y_m$ is given in table 10.12 of [@buendia2019Refinement20062019] and ranges from 3.0 to 5.7.

### Gross Energy Intake

Gross energy intake (GE) for cattle is defined in Equation 10.16 of [@buendia2019Refinement20062019] as:


$$GE = \left[ \frac{ \left( \frac{NE_m\,+\,NE_a\,+\,NE_l\,+\,NE_{work}\,+\,NE_p}{REM} \right) + \left( \frac{NE_g}{REG} \right) }{DE} \right] $$

Where:


$$
\begin{array}{rll}
GE &=& \text{gross energy} &\; (MJ \; day^-1) \\
NE_m &=& \text{net energy for animal maintenance} &\; (MJ \; day^-1) \\
NE_a &=& \text{net energy for animal activity} &\; (MJ \; day^-1) \\
NE_l &=& \text{net energy for lactation} &\; (MJ \; day^-1) \\
NE_{work} &=& \text{net energy for work} &\; (MJ \; day^-1) \\
NE_p &=& \text{net energy for pregnancy} &\; (MJ \; day^-1) \\
REM &=& \text{ratio energy for maintenance to digestible energy} &\; \\
NE_g &=& \text{net energy for growth} &\; (MJ \; day^-1) \\
REG &=& \text{ratio energy for growth to digestible energy} &\; \\
DE &=& \text{digestibility of feed} &\; (\text{digestible energy / gross energy})\\
\end{array}
$$


#### TODO: net energy required by the animal for maintenance
#### TODO: net energy for animal activity
#### TODO: net energy for lactation
#### TODO: net energy for work
#### TODO: net energy required for pregnancy
#### TODO: ratio of net energy available in a diet for maintenance to digestible energy
#### TODO:  net energy needed for growth
#### TODO: ratio of net energy available for growth in a diet to digestible energy consumed
#### TODO: net energy required to produce a year of wool
#### TODO: digestibility of feed expressed as a fraction of gross energy


## Simplified Tier 2

Simplified Tier 2 uses estimates of Dry Matter Intake (DMI) for cattle to calculate the emission factor per type.



$$EF = DMI \cdot \left( \frac{MY}{1000} \right) \cdot 365 $$

Where:


$$
\begin{array}{rll}
EF &=& \text{emission factor} &\; (kg \; CH_4 \; head^-1 \; yr^-1 ) \\
DMI &=& \text{dry matter intake} &\; (kg \; DMI \; day^-1) \\
MY &=& \text{methane yield} &\; (g \, CH_4 \; kg \, DMI^-1)
\end{array}
$$

The factor 1000 is the conversion from $g\;CH_4$ to $kg\;CH_4$. 


### Dry Matter Intake

Dry Matter Intake (DMI) for cattle is calculated using equations 10.17 and 10.8 as defined below.


TODO: Update to 2019 - calves, growing cattle, etc


#### Calves



$$DMI = BW^{0.75} \cdot \left[ \frac{ ( 0.0582 \cdot NE_{mf} -0.00266 \cdot {NE_{mf}}^2 - 0.1128) }{0.239 \cdot NE_{mf}} \right]  $$


Where:


$$
\begin{array}{rll}
DMI &=& \text{dry matter intake} &\; (kg \; DMI \; day^-1) \\
BW &=& \text{live body weight} &\; (kg)\\
NE_{mf} &=& \text{dietary net energy} &\; (MJ \; kg^-1)\\
\end{array}
$$


#### Growing  Cattle



$$DMI = BW^{0.75} \cdot \left[ \frac{ ( 0.0582 \cdot NE_{mf} -0.00266 \cdot {NE_{mf}}^2 - 0.0869) }{0.239 \cdot NE_{mf}} \right]  $$


Where:

$$
\begin{array}{rll}
DMI &=& \text{dry matter intake} &\; (kg \; DMI \; day^-1) \\
BW &=& \text{live body weight} &\; (kg)\\
NE_{mf} &=& \text{dietary net energy} &\; (MJ \; kg^-1)\\
\end{array}
$$


#### Feedlot Cattle

For steers and bulls:


$$DMI = 3.83 + 0.0143 \cdot BW \cdot 0.96  $$


For heifers:


$$DMI = 3.184 + 0.01536 \cdot BW \cdot 0.96  $$


Where:


$$
\begin{array}{rll}
DMI &=& \text{dry matter intake} &\; (kg \; DMI \; day^-1) \\
BW &=& \text{live body weight} &\; (kg)\\
\end{array}
$$


For mature beef cows the following table can be used directly:


| Forage type     | Digestibility (DE,%) | DMI non-lactating | DMI lactating |
| --------------- | -------------------- | ----------------- | ------------- |
| Low quality     | < 52                 | 18.               | 2.2           |
| Average quality | 52-59                | 2.2               | 2.5           |
| High quality    | > 59                 | 2.5               | 2.7           |


#### Lactating Dairy Cows


$$DMI = 0.0185 \cdot BW + 0.305 \cdot FCM  $$


Where:


$$
\begin{array}{rll}
DMI &=& \text{dry matter intake} &\; (kg \; DMI \; day^-1) \\
BW &=& \text{live body weight} &\; (kg)\\
FCM &=& \text{fat corrected milk} &\; (kg \; day^-1)\\
\end{array}
$$


Further:


$$FCM = 3.5\% \cdot \left[ (0.4324 \cdot m) + (16.216 \cdot f) \right]$$


Where:


$$
\begin{array}{rll}
m &=& \text{milk produced} &\; (kg) \\
f &=& \text{fat produced} &\; (kg)\\
\end{array}
$$



### Dietary Net Energy

See Table 10.8a of @buendia2019Refinement20062019 

# Mitigation

## Demand-side methods

- [M-3C.2 - Shift to Sustainable Healthy Diets](/2-ipcc-mitigation-options/3-afolu/3c-other/3c-02-shift-sustainable-healthy-diets.md)


## Supply-side methods

- 

