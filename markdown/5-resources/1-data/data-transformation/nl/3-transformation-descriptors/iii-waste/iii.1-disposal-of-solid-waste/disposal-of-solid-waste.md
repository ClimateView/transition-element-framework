---
title: Disposal of solid waste 
progress: 50
region: nl
---

![Data Sourcing - TD](/images/data-sourcing-td.jpg){.cv-center .full-width-paragraph}


# Parameters
The methods below are for determining the parameter values for the following parameters:

- [Stock of waste to landfills](/5-resources/1-data/definitions/parameters/stock_waste_landfill.md)
- [Stock waste exported for landfill](/5-resources/1-data/definitions/parameters/stock_exported_waste_landfill.md)
- [Stock of recycled waste](/5-resources/1-data/definitions/parameters/stock_waste_recycling.md)



# Methods

## Household waste

From **[83452NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/83452ned.md)**: Household waste per municipality per inhabitant, filter for your municipality and year. Aggregate the different waste types by treatment type (landfill, incineration, composting, AD, etc.) and whether the activity is taking place in the municipality or exported (or which fraction is being handled in vs. outside of the municipality). Then multiply the aggregated amount with the population number to get the total amount.

Alternative source: **[83558NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/83558ned.md)**: Municipal waste; quantities, household waste per different collection ways and regions.




# Sources

- [83452NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/83452ned.md)
- [83558NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/83558ned.md)



