---
title: E-2A1 - Cement Production
---


This page covers emissions from cement production that stem from the clinker production phase.  During this phase, limestone (primarily $\ce{CaCO3}$) is heated to produce lime ($\ce{CaO}$) with $\ce{CO2}$ being emitted as a by-product.
 
This emission source is modelled in the OTI as the activity: [T-2A1-A-1 - Calcination of limestone for clinker production](/3-transition-elements/2-industry/2a-minerals/2a1-cement/2a1-a-01-calcination_of_limestone_for_clinker_production.md).

# Activity
Volume 3, chapter 2 of @egglestonh.s.2006IPCCGuidelines2006 defines methods for calculating emissions from clinker production based primarily on measurements of the activity of net cement production.

Tier 1 recommendations are to use activity data collected per type of cement produced as well as the estimated clinker fraction in each type of cement. The following table from @egglestonh.s.2006IPCCGuidelines2006 gives suggested example types and values based on U.S. standards ASTM C-150 and C-595:

| Cement Type                | Fraction clinker |
| -------------------------- | ---------------- |
| Portland                   | 95-97%           |
| Masonry                    | 64%              |
| Slag-modified portland     | > 70-93%         |
| Portland BF Slag           | 28-70%           |
| Portland pozzolan          | 28-79%           |
| Pozzolan-modified portland | 28-93%           |
| Slag cement                | < 28%            |


> [!note]
> No further amendments to cement emission modelling were made in @buendia2019Refinement20062019. 

# Emissions

Emissions from cement can be estimated using one of the following tiers

- Tier 1: emissions based on clinker production estimates inferred from cement production data
- Tier 2: emissions based on direct estimates of clinker production data
- Tier 3: emissions based on weight and composition of all carbonate inputs from all raw materials using plant specific data

The IPCC states that if cement production is a *key category* then tier 1 should not be considered *good practice* for emission estimation because it does not account for imports and exports of clinker [@egglestonh.s.2006IPCCGuidelines2006]. Thus tier 2 or 3 are the recommended methods. If plant specific data is considered unreliable or uncertain then tier 2 should be used.

> [!note]
> Cement kiln dust (CKD) - a fine-grained solid by-product of the cement manufacturing process - is not included in the measurement of cement or clinker produced and thus should be measured and accounted for in tier 2 and tier 3 methods as a separate factor. 


## Tier 1

Tier 1 emissions are based on total mass of cement produced and summed per type of cement - the exact amount of clinker used in cement production is not adressed, however imports and exports of clinker are compensated for.

Emissions are calculated as:

$$E = \left[ \sum_i (M_{ci} \cdot C_{cli}) - Im + Ex \right] \cdot  EF_{clc} $$
Where:

$$
\begin{array}{rll}
E &=& \text{Emissions of} \; \ce{CO2} \; &  \\
M_{ci} &=& \text{Cement of type $i$ produced} &\; (tonnes) \\
C_{cli} &=& \text{Clinker fraction for cement of type $i$} &\;  \\
Im &=& \text{Clinker imports} &\; (tonnes) \\
Ex &=& \text{Clinker exports} &\; (tonnes) \\
EF_{clc} &=& \text{Emission factor for clinker} &\; (tonnes \; \ce{CO2} \; / \; tonne \, clinker) \\
\end{array}
$$

> [!note]
> It is unclear if $EF_{clc}$ should be measured per cement type $i$ - the subscript $i$ is missing from the parameter name however the textual description does state "emission factor for clinker in the particular cement"


### Emission Factor Clinker

The $\ce{CaO}$ content for clinker is roughly estimated to be 65% giving 0.65 tonnes of $\ce{CaO}$ per tonne of $\ce{CaCO3}$. From this the following default emission factor can be derived:

$$EF_{clc} = 0.51 \cdot 1.02 = 0.52 \; (tonnes \,\ce{CO2} \; / \; tonne \, clinker) $$


> [!note]
> CKD is factored into $EF_{clc}$ using the correction factor $1.02$.


## Tier 2

The tier 2 approach estimates emissions based on total mass of clinker produced:


$$E = M_{cl} \cdot  EF_{cl} \cdot  CF_{ckd} $$
Where:

$$
\begin{array}{rll}
E &=& \text{Emissions of} \; \ce{CO2} \; &  \\
M_{cl} &=& \text{Clinker produced} &\; (tonnes) \\
EF_{cl} &=& \text{Emission factor for clinker} &\; (tonnes \; \ce{CO2} \; / \; tonne \, clinker) \\
CF_{ckd} &=& \text{Emissions correction factor for CKD} &\; \\
\end{array}
$$


> [!note]
> The tier 2 approach assumes that the majority of cement manufactured is portland cement or similar.


### Emission Factor Clinker

Country-specific data should be used for the $\ce{CaO}$ content of clinker, giving a country-specific $EF_{cl}$.

### Emission Correction Factor for CKD

Cement kiln dust (CKD) can occur at many stages during the clinker manufacturing process. Some CKD is captured and can be returned to the kiln. Since the CKD is partially calcinated and not all CKD is returned to the kiln, the following factor corrects for this in the tier 2 method:

$$CF_{ckd} = 1 + (M_d / M_{cl}) \cdot  C_{d} \cdot F_d \cdot (EF_c/EF_{cl}) $$
Where:

$$
\begin{array}{rll}
CF_{ckd} &=& \text{Emission correction factor for CKD} \; \ce{CO2} \; &  \\
M_{d} &=& \text{CKD not recycled into kiln} &\; (tonnes) \\
M_{cl} &=& \text{Clinker produced} &\; (tonnes) \\
C_{d} &=& \text{Fraction carbonate in CKD} &\; (fraction) \\
EF_{c} &=& \text{Emission factor for carbonate} &\; (tonnes \; \ce{CO2} \; / \; tonne \, carbonate) \\
EF_{cl} &=& \text{Emission factor for clinker uncorrected for CKD} &\; (tonnes \; \ce{CO2} \; / \; tonne \, clinker) \\
\end{array}
$$


##  Tier 3

The tier 2 approach measures emissions based on plant specific carbonate input data using the following equation:

$$E = \sum_i (EF_i \cdot M_i \cdot F_i) -  M_d \cdot  C_{d} \cdot (1-F_d) \cdot EF_{d} + \sum_k (M_k \cdot X_k \cdot EF_k) $$

Where:

$$
\begin{array}{rll}
E &=& \text{Emissions of} \; \ce{CO2} \; &\; (tonnes) \\
EF_{i} &=& \text{Emission factor for carbonate $i$} &\; (tonnes \; \ce{CO2} \; / \; tonne \, carbonate) \\
M_{i} &=& \text{Carbonate consumed in kiln} &\; (tonnes) \\
F_{i} &=& \text{Fraction calcination achieved in kiln} &\; (fraction) \\
M_{d} &=& \text{CKD not recycled to kiln} &\; (tonnes) \\
C_{d} &=& \text{Fraction carbonate in CKD} &\; (fraction) \\
F_{d} &=& \text{Fraction calcination achieved for CKD} &\; (fraction) \\
EF_{d} &=& \text{Emission factor for CKD} &\; (tonnes \; \ce{CO2} \; / \; tonne \, carbonate) \\
M_{k} &=& \text{Mass of carbon-bearing resource of type $k$} &\; (tonnes) \\
X_{k} &=& \text{Fraction of carbon content in resource of type $k$} &\; (tonnes) \\
EF_{k} &=& \text{Emission factor for $k$} &\; (tonnes) \\
\end{array}
$$


> [!note]
> If the kerogen content is high (e.g. more than 5% of total heat) then it is recommended as *good practice* to include these emissions.

### Emission Factors
Using tier 3 then $EF_i$, $EF_d$ and $EF_k$ are plant specific estimates.

# Mitigation

## TODO: Demand-side methods


## TODO: Supply-side methods


