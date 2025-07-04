---
title: Railways 
progress: 50
region: nl
---

![Data Sourcing - TD](/images/data-sourcing-td.jpg){.cv-center .full-width-paragraph}


# Parameters
The methods below are for determining the parameter values for the following parameters:

- [Stock passenger rail diesel](/5-resources/1-data/definitions/parameters/stock_passenger_diesel_rail.md)
- [Stock of electric railway operation](/5-resources/1-data/definitions/parameters/stock_mobility_rail_electric.md)
- [Stock of tram and light rail operaton](/5-resources/1-data/definitions/parameters/stock_mobility_tram_light_rail.md)
- [Stock of freight rail operation](/5-resources/1-data/definitions/parameters/stock_freight_rail.md)
- [Stock of freight electric rail operations](/5-resources/1-data/definitions/parameters/stock_freight_electric_rail.md)



# Methods

## Electrified freight rail and diesel freight rail.

From either **[80429NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/80429ned.md)**: Rail transport; cargo weight, cargo tonne-kilometre, train kilometres or **[82512NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/82512ned.md)**: Rail transport; freight transport on Dutch rail, freight type, take the total goods moved (tonne-km). The total number is the same in both datasets, one contains numbers sliced per import, export or transit, the other one contains numbers sliced per goods type. If you only want the total, take either, if any of the splits is of interest, select that one.

Downscale the number to your province. Since both datasets mentioned above contain only total numbers, the downscaling can be done either by population or by "rail density", see next point.

To downscale the total number of tonne-km to your province, calculate the total number of rail-km per province using dataset **[71024NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/71024ned.md)**: Length of railway routes; railway route characteristics, province. To do that, multiply the kms of rail tracks with the number of tracks per province and the entire country and work out the shares. Now apply the share of your province to the total amount of goods moved (tonne-km) for the Netherlands. Please note, that for this type of downscaling, we assume that the movement of freight trains is evenly distributed across all the rail tracks.

Work out the share of tracks that are electrified in your province from the dataset **[71024NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/71024ned.md)**: Length of railway routes; railway route characteristics, province. For your province (or other geographic entity), multiply the total km of tracks by the respective number of tracks for those with overhead lines and those without overhead lines respectively. Calculate the share of electrified vs. non electrified.

Now split the amount of tonne-km for your province between electric and diesel rail according to the proportions of electrified vs. non-electrified tracks. Alternatively, apply local knowledge to make that split.




# Sources

- [80429NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/80429ned.md)
- [82512NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/82512ned.md)
- [71024NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/71024ned.md)



