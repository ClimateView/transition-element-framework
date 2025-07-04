---
title: E-3A1h - Swine
---


# Categories

This page covers the following emission source categories and subcategories:

- Mature swine
	- Sows in gestation
	- Farrowed sows nursing young
	- Boars for breeding
- Growing swine
	- Nursery
	- Finishing
	- Gilts for breeding
	- Growing boards for breeding


# Population
Section 10.2 of [@buendia2019Refinement20062019] outlines methods for calculating livestock population and feed characterisation. 

Emission calculations for swine are based on the number of livestock ($N$) which can be calculated as:

$$N = Days\_alive \cdot \left[ \frac{NAPA}{365} \right] $$
Where:

$$
\begin{array}{rll}
N &=& \text{number of head of livestock} &\;  \\
NAPA &=& \text{number of animals produced annually} &\;
\end{array}
$$



# Emissions

Emissions from swine livestock can be estimated using one of the following tiers

- Tier 1: emissions calculated per head of livestock
- Tier 1a: emissions calculated per head of livestock per productivity system
- Tier 2: emissions calculated based on Dry Matter Intake (DMI)
- Tier 2a: emissions calculated based on gross energy intake of livestock

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

Emission factors for Tier 1a for swine:

| Productivity System | $CH_4$ Emission Factor |
| ------------------- | ---------------------- |
| High                | 1.5                    |
| Low                 | 1                      |

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


>[!note]
>Emission factors for Tier 1 are not given in [@buendia2019Refinement20062019] presumably because it is not the recommended approach for swine.


## Tier 2
Tier 2 calculations are provided for livestock in a manner that would encompass swine, however emission factors are not presented in [@buendia2019Refinement20062019].


# Mitigation

## Demand-side methods

- [M-3C.2 - Shift to Sustainable Healthy Diets](/2-ipcc-mitigation-options/3-afolu/3c-other/3c-02-shift-sustainable-healthy-diets.md)

## Supply-side methods

- 

