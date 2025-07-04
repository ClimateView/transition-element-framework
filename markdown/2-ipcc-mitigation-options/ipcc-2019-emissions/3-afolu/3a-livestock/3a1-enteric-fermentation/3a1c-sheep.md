---
title: E-3A1c - Sheep
---

# Categories

This page covers the following emission source categories and subcategories:

- Mature ewes
	- Breeding ewes for offspring and wool production
	- Milking ewes
- Other mature sheep
- Growing Lambs
	- Intact males
	- Castrates
	- Females

# Population
Section 10.2 of [@buendia2019Refinement20062019] outlines methods for calculating livestock population and feed characterisation. 

Emission calculations for sheep are based on the number of livestock ($N$) which can be calculated as:

$$N = Days\_alive \cdot \left[ \frac{NAPA}{365} \right] $$
Where:

$$
\begin{array}{rll}
N &=& \text{number of head of livestock} &\;  \\
NAPA &=& \text{number of animals produced annually} &\;
\end{array}
$$



# Emissions

Emissions from sheep livestock can be estimated using one of the following tiers

- Tier 1: emissions calculated per head of livestock
- Tier 1a: emissions calculated per head of livestock per productivity system
- Tier 2: emissions calculated based on gross energy intake of livestock
- Simplified Tier 2: emissions calculated based on Dry Matter Intake (DMI)

IPCC recommends tier 1 or 2 as the suggested inventory method for sheep [@buendia2019Refinement20062019].

> [!note]
> The distinction between "1" vs "1a" and "2" vs "2a" is the degree of complexity or simplification of method within the tier. In both cases the more advanced method is the often the recommended approach. 

## Tier 1a

Tier 1a is recommended where emissions are calculated per productivity system - either high or low - expressed as:

$$Emission = \sum_{p}EF_p \cdot \left[ \frac{N_p}{10^6} \right] $$
Where:

$$
\begin{array}{rll}
Emission &=& \text{Emissions of} \; CH_4 \; & (Gg \; CH_4 \; yr^-1) \\
EF_p &=& \text{emission factor} &\; (kg \; CH_4 \; head^-1 \; yr^-1 ) \\
N_p &=& \text{number of livestock} &\;  \\
p &=& \text{productivity system} &\; (high,low)
\end{array}
$$

Emission factors for Tier 1a for sheep:

| Productivity System | $CH_4$ Emission Factor |
| ------------------- | ---------------------- |
| High                | 9                      |
| Low                 | 5                      |


### High-productivity systems

>...  100 percent market oriented with high level of capital input requirements and high level of overall herd (flock) performance. Feed is purchased from local or international market or intensively produced on farm. Animals are improved through breeding practices for commercial production. [@buendia2019Refinement20062019]

### Low productivity systems

>...  mainly driven by local market or by self-consumption, with low capital input requirements and low level of overall herd (fowl) performance typically using large areas for production or backyards. Locally produced feed represents the major source of feed utilized or animals are kept-free range for major part or all of their production cycle, the yield of the activity being linked to the natural fertility of the land and the seasonal production of the pastures. [@buendia2019Refinement20062019]

## Tier 1

If the split of productivity system is excluded (not recommended by IPCC) then the approach is classified as Tier 1 and is thus simplified to:

$$Emission = EF \cdot \left[ \frac{N}{10^6} \right] $$
Where:

$$
\begin{array}{rll}
Emission &=& \text{Emissions of} \; CH_4 \; & (Gg \; CH_4 \; yr^-1) \\
EF &=& \text{emission factor} &\; (kg \; CH_4 \; head^-1 \; yr^-1 ) \\
N &=& \text{number of livestock} &\;  
\end{array}
$$


> [!note]
> Emission factors for Tier 1 are not given in [@buendia2019Refinement20062019]  as it is not the recommended approach for sheep.

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
The methane conversion factor is measured as a percent of gross energy in feed converted to methane. The factor $55.65 (MJ/kg CH_4)$ is the energy content of methane.

For sheep $Y_m$ is given as $6.7\% ± 0.9$ in table 10.13 of [@buendia2019Refinement20062019].

### Gross Energy Intake

Gross energy intake (GE) for sheep is defined in Equation 10.16 of [@buendia2019Refinement20062019] as:

$$GE = \left[ \frac{ \left( \frac{NE_m\,+\,NE_a\,+\,NE_l\,+\,NE_{work}\,+\,NE_p}{REM} \right) + \left( \frac{NE_g\,+\,NE_{wool}}{REG} \right) }{DE} \right] $$
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
NE_{wool} &=& \text{net energy for wool production} &\; (MJ \; day^-1) \\
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

Simplified Tier 2 uses estimates of Dry Matter Intake (DMI) to calculate the emission factor: 

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

> Dry matter is the amount of feed consumed (kg) after it has been corrected for the water content in the complete diet. For example, consumption of 10 kg of a diet that contains 70% dry matter would result in a dry matter intake of 7 kg. 

\- @egglestonh.s.2006IPCCGuidelines2006

Methods for calculating DMI for sheep are not explicitly provided in the IPCC reports [@egglestonh.s.2006IPCCGuidelines2006] and [@buendia2019Refinement20062019].  However approximate values are suggested for sheep when defining the methane conversion factor $Y_m$:

> The mean value [ of $Y_m$] of 6.7 percent is most appropriate for situations where average dry matter intake per day is between 0.6 and 0.8 kg day-1 with a value of 7.0 percent being more appropriate where average intake is <0.6 kg day-1, and a value of 6.5 percent being more appropriate where average intakes are >0.8kg day-1.

\- @buendia2019Refinement20062019


### Methane Yield

@buendia2019Refinement20062019  only provides explicite values for methane yield for cattle and buffalo - however the value for sheep could be extrapolated by combining the value of $Y_m$ for sheep ($6.7$) with the average conversion ratio between $MY$ and $Y_m$ for cattle of $3.333$. 

Thus we estimate methane yield for sheep as:

$$MY = 3.333 \cdot 6.7 = 22.3 $$

# Mitigation

## Demand-side methods

- [M-3C.2 - Shift to Sustainable Healthy Diets](/2-ipcc-mitigation-options/3-afolu/3c-other/3c-02-shift-sustainable-healthy-diets.md)


## Supply-side methods

- 

