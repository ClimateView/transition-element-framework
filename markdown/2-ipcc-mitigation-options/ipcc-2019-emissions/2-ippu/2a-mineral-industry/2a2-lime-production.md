---
title: E-2A2 - Lime Production
---

This page covers emissions from calcium oxide ($\ce{CaO}$ or quicklime) production that stem from the heating of limestone ($\ce{CaCO3}$) to decompose the carbonates.  Specifically the following chemical reaction is estimated:

$$
\ce{CaCO3 + heat -> CaO + CO2}
$$

This emission source is modelled in the OTI as the activity: [T-2A2-A-1 - Calcination of limestone for lime production](/3-transition-elements/2-industry/2a-minerals/2a2-lime-production/2a2-a-01-calcination_of_limestone_for_lime_production.md).

# Lime types

- a) High calcium lime
- b) Dolomitic lime
- c) Hydraulic lime

# TODO: Activity
Volume 3, chapter 2 of @egglestonh.s.2006IPCCGuidelines2006 defines methods for calculating emissions from lime production ....


> [!note]
> No further amendments to cement emission modelling were made in @buendia2019Refinement20062019. 
# Emissions

Emissions from cement can be estimated using one of the following tiers

- Tier 1: emissions based on aggregated national level lime production data and default emission factors
- Tier 2: emissions based on direct estimates of lime production data and emission factors per type
- Tier 3: emissions based on weight and composition of all carbonate inputs from all raw materials using plant specific data

The IPCC states that if cement production is a *key category* then tier 1 should not be considered *good practice* for emission estimation because it does not account for imports and exports of clinker [@egglestonh.s.2006IPCCGuidelines2006]. Thus tier 2 or 3 are the recommended methods. If plant specific data is considered unreliable or uncertain then tier 2 should be used.

> [!note]
> Lime kiln dust (LKD) - a fine-grained solid by-product of the lime manufacturing process - is not included in the measurement of lime produced and thus should be measured and accounted for in tier 2 and tier 3 methods as a separate factor. 


## Tier 1

An equation for tier 1 emission calculation of lime production is not explicitly provided in @egglestonh.s.2006IPCCGuidelines2006 however one can be easily derived as a simplification of the tier 2 equation based on lime output:

$$E = M \cdot  EF_{lime} $$
Where:

$$
\begin{array}{rll}
E &=& \text{Emissions of} \; \ce{CO2} \; &  \\
M &=& \text{Lime production} &\; (tonnes) \\
EF_{lime} &=& \text{Emission factor for lime} &\; (tonnes \; \ce{CO2} \; / \; tonne \, lime) \\
\end{array}
$$

> [!note]
> It is unclear if $EF_{clc}$ should be measured per cement type $i$ - the subscript $i$ is missing from the parameter name however the textual description does state "emission factor for clinker in the particular cement"

### Emission Factor Lime
The tier 1 approach does not require country specific data for the emission factor. Instead @egglestonh.s.2006IPCCGuidelines2006 notes that the *good practice* is to assume 85% high calcium lime and 15% dolomitic lime. This division references @millerGeologicalSurveyMinerals1999 however this reference was found to be unclear - we have assumed that the 85 / 15 split is the rough split between high-calcium quicklime and dolomitic quicklime given in the 1999 production data for the United States in table 1. 

The $CaO$ content for clinker is roughly estimated to be 65% giving 0.65 tonnes of $CaO$ per tonne of $CaCO_3$. From this the following default emission factor can be derived:

$$EF_{lime} = 0.85 \cdot EF_{high calcium lime} + 0.15 \cdot EF_{dolomitic lime} $$


> [!note]
> LKD is not addressed in tier 1.


## Tier 2

The tier 2 approach estimates emissions based on total mass of lime produced:


$$E = \sum_i ( EF_{lime,i} \cdot  M_{l,i} \cdot  CF_{lkd,i} \cdot C_{h,i}) $$

Where:

$$
\begin{array}{rll}
E &=& \text{Emissions of} \; \ce{CO2} \; &  \\
EF_{lime,i} &=& \text{Emission factor for lime of type i} &\; (tonnes \; \ce{CO2} \; / \; tonne \, lime) \\
M_{l,i} &=& \text{Lime of type i produced} &\; (tonnes) \\
CF_{lkd,i} &=& \text{Correction factor for LKD for lime of type i} &\; \\
C_{h,i} &=& \text{Correction factor for hydrated lime of type i} &\; \\
\end{array}
$$


### Emission Factor Lime
Tier 2 emission factor calculation for lime is broken down into the three primary types of lime:


$$
\begin{array}{rl}
EF_{lime,a} &=& SR_{\ce{CaO}} \bullet \ce{CaO} \, \text{content} \\
EF_{lime,b} &=& SR_{\ce{CaO}\cdot\ce{MgO}} \bullet \ce{CaO}\cdot\ce{MgO} \, \text{content} \\
EF_{lime,c} &=& SR_{\ce{CaO}} \bullet \ce{CaO} \, \text{content} \\
\end{array}
$$

Where:

$$
\begin{array}{rll}
EF_{lime,a} &=& \text{Emission factor for quicklime} &\; (\text{tonnes} \; \ce{CO2} \; / \; \text{tonne} \, \text{lime}) \\
EF_{lime,b} &=& \text{Emission factor for dolomitic lime} &\; (\text{tonnes} \; \ce{CO2} \; / \; \text{tonne} \, \text{lime}) \\
EF_{lime,c} &=& \text{Emission factor for hydraulic lime} &\; (\text{tonnes} \; \ce{CO2} \; / \; \text{tonne} \, \text{lime}) \\
SR_{\ce{CaO}} &=& \text{Stoichiometric ratio of } \ce{CO2} \text{ and } \ce{CaO} &\;  (\text{tonnes} \; \ce{CO2} \; / \; \text{tonne} \,\ce{CaO} ) \\
SR_{\ce{CaO}\cdot\ce{MgO}} &=& \text{Stoichiometric ratio of } \ce{CO2} \text{ and } \ce{CaO}\cdot\ce{MgO} &\;  (\text{tonnes} \; \ce{CO2} \; / \; \text{tonne} \,\ce{CaO}\cdot\ce{MgO} ) \\
\ce{CaO} \text{ content} &=& \ce{CaO} \text{ content } &\; (\text{tonnes} \; \ce{CaO} \; / \; \text{tonne lime} ) \\
\ce{CaO}\cdot\ce{MgO} \text{ content} &=& \ce{CaO}\cdot\ce{MgO} \text{ content } &\; (\text{tonnes} \; \ce{CaO}\cdot\ce{MgO} \; / \; \text{tonne lime} ) \\
\end{array}
$$

@egglestonh.s.2006IPCCGuidelines2006 Volume 3, Table 2.4 provides the stoichiometric ratios and content factors as:

| Lime type         | SR    | Content | Default EF |
| ----------------- | ----- | ------- | ---------- |
| High-calcium lime | 0.785 | 0.95    | 0.75       |
| Dolomitic lime    | 0.913 | 0.95    | 0.86       |
| Hydraulic lime    | 0.785 | 0.75    | 0.59       |


### Emission Correction Factor for CKD

Lime kiln dust (CKD) can occur at many stages during the lime manufacturing process. Some LKD is captured and can be returned to the kiln. Since the LKD is partially calcinated and not all LKD is returned to the kiln, the tier 2 method recommends using a factor of $1.02$ to correct for LKD.



## TODO: Tier 3


# Mitigation

## Demand-side methods


## Supply-side methods

 

