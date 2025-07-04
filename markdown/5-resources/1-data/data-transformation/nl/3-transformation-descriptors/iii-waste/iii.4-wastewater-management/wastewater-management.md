---
title: Wastewater management 
progress: 50
region: nl
---

![Data Sourcing - TD](/images/data-sourcing-td.jpg){.cv-center .full-width-paragraph}


# Parameters
The methods below are for determining the parameter values for the following parameters:

- [Stock domestic waste water treatment](/5-resources/1-data/definitions/parameters/stock_m3_domestic_wastewater_treated.md)
- [Stock waste exported for treatment](/5-resources/1-data/definitions/parameters/stock_exported_wastewater_for_treatment.md)



# Methods

## Waste water treated

From the dataset **7477**: Purification of waste water; regional, find the region (entire NL, province or other) most suitable for your municipality. Get the number from column **VolumeAfvalwater_{43}**. Scale it to your municipality by population to estimate the amount of waste water produced by your municipality. Apply local knowledge to determine whether all, none or parts of the waste water is treated locally or if it is being exported.

Alternative source: **[71476NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/71476ned.md)**: Purification of urban waste water; per regional water quality manager, if you know what water quality manager your municipality belongs to and what share of the population your municipality corresponds. The column to look for here is also **VolumeAfvalwater_{43}**.




# Sources

- [7477NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/7477ned.md)
- [71476NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/71476ned.md)



