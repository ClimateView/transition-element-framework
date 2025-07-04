---
title: Residential cooling 
progress: 50
region: nl
---

![Data Sourcing - TD](/images/data-sourcing-td.jpg){.cv-center .full-width-paragraph}



# Parameters
The methods below are for determining the parameter values for the following parameters:

- [Stock multi-family houses cooled with AC](/5-resources/1-data/definitions/parameters/stock_cooling_residential_multi_family_ac.md)
- [Stock multi-family houses cooled with district cooling](/5-resources/1-data/definitions/parameters/stock_cooling_residential_multi_family_building_district_cooling.md)
- [Stock single-family houses cooled with AC](/5-resources/1-data/definitions/parameters/stock_cooling_residential_single_family_ac.md)
- [Stock single-family houses cooled with district cooling](/5-resources/1-data/definitions/parameters/stock_cooling_residential_single_family_building_district_cooling.md)



# Methods

## Heating all residential builings

For your municipality, download the zip file containing all the building and energy files. Open the file **"GMxxxx_bebouwing"**. You will find the number of buildings for each building category.


Split between small houses (domestic houses) and blocks of flats (residential blocks):

- Count the following as small houses:
  - Vrijstaande_woning, 2_onder_1_kap, Rijwoning_hoek and Rijwoning_tussen


- Count the following types as blocks of flats:
  - Appartementen


Use local knowledge about the average size per house type to determine the total amount of square meters for the two categories.


Further, split between the different heating energy sources:

For each Strategy file (**GMxxxx_BUyyyyyyyy_strategie**), sum up the total demand and demand per usage multiplied by the total WEQ for the buurt (from the file **GMxxxx_bebouwing**):

- $H01\_Vraag\_totaal$ for the total usage,
- $H02\_Vraag\_RV$ and $H03\_Vraag\_TW$ for space heating,
- $H04\_Vraag\_Vent$ and $H05\_Vraag\_Koude$ for cooling and
- $H06\_Vraag\_App$ for other appliances


In the same way, sum up the total supply per energy type multiplied by the total WEQ for the buurt:

- $H08\_Input\_totaal$
- $H09\_Input\_Aardgas$
- $H10\_Input\_duurzaamgas$
- $H11\_Input\_elektriciteit$
- $H12\_Input\_MTwarmtebronnen$
- $H13\_Input\_LTwarmtebronnen$
- $H14\_Input\_omgevingswarmte$


Please note that the energy usage is including the non-residential buildings' energy use. To get the shares of each energy source for residential, either make the simplified assumption that the shares are the same across sectors or apply local knowledge to correct that.

Calculate the shares for heating:

- From the usage sums ("Vraag..."), look at which usages are exclusively electricity, (possibly appliances, cooling and ventilation) and subtract their total from the total supply of electricity. 
- In case there are other usages (e.g. gas for cooking or other non-heating related usages for other energy types), subtract the corresponding amount from those energy types.
- From the remaining amounts of energy used (which can be assumed to be for heating), calculate the share of each energy source.
- Apply those shares to the m2 of the respective building types to get the activity in m2 to enter into the upload sheet.

## Cooling and other energy use

The energy amounts calculated above not used for heating, can be entered into cooling and "other energy use" for the respective energy sources.

Apply the share that goes to residential.

Convert from GJ to kWh.




# Sources

- [Startanalyse aardgasvrije buurten](/5-resources/1-data/data-transformation/nl/2-data-descriptors/startanalyse-aardgasvrije-buurten.md)



