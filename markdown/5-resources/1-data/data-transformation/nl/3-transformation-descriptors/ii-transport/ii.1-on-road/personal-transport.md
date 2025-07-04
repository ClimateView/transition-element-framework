---
title: Personal transport 
progress: 50
region: nl
---

![Data Sourcing - TD](/images/data-sourcing-td.jpg){.cv-center .full-width-paragraph}


# Parameters
The methods below are for determining the parameter values for the following parameters:

- [Stock of personal vehicles (petrol) operation](/5-resources/1-data/definitions/parameters/stock_personal_vehicles_petrol.md)
- [Stock of personal vehicles (diesel) operation](/5-resources/1-data/definitions/parameters/stock_personal_vehicles_diesel.md)
- [Stock of personal vehicles (natural gas) operation](/5-resources/1-data/definitions/parameters/stock_personal_vehicles_natural_gas.md)
- [Stock personal vehicles (LPG) operation](/5-resources/1-data/definitions/parameters/stock_personal_vehicles_lpg.md)
- [Stock of personal vehicles (BEV) operation](/5-resources/1-data/definitions/parameters/stock_personal_vehicles_bev.md)
- [Stock of personal vehicles (hydrogen) operation](/5-resources/1-data/definitions/parameters/stock_personal_vehicles_hydrogen.md)
- [Stock petrol motorcycles](/5-resources/1-data/definitions/parameters/stock_motorcycles_petrol.md)
- [Stock electric motorcycles](/5-resources/1-data/definitions/parameters/stock_motorcycles_electric.md)
- [Stock diesel buses](/5-resources/1-data/definitions/parameters/stock_buses_diesel.md)
- [Stock petrol buses](/5-resources/1-data/definitions/parameters/stock_buses_petrol.md)
- [Stock gas buses](/5-resources/1-data/definitions/parameters/stock_buses_gas.md)
- [Stock LPG buses](/5-resources/1-data/definitions/parameters/stock_buses_lpg.md)
- [Stock hydrogen buses](/5-resources/1-data/definitions/parameters/stock_buses_hydrogen.md)
- [Stock of electric (BEV) bus operation](/5-resources/1-data/definitions/parameters/stock_mobility_bus_bev.md)
- [Stock of walking and biking](/5-resources/1-data/definitions/parameters/stock_mobility_walking_biking.md)
- [Stock electric bikes](/5-resources/1-data/definitions/parameters/stock_electric_bikes.md)



# Methods

## Personal vehicles: traffic performance of locally registered cars.

Per fuel type (petrol, diesel, lpg, ethanol, battery electric (BEV), hydrogen (FCEV)):

1. From **dataset [85405NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85405ned.md)**: Traffic performance of passenger cars, fuel extended, age, take the average number of km driven per car of a certain fuel type.
   - Let $X = \text{average number of km driven per car of the fuel type}$

2. From **dataset [85236NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85236ned.md)**: Motor vehicles active on January 1; vehicle type, region as of January 1, 2023 take the number of cars registered in your municipality.
   - Let $Y = \text{the number of cars registered in your municipality}$

3. From **dataset [85237NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85237ned.md)**: Passenger cars active; vehicle characteristics, regions, January 1 get the distribution of passenger cars per fuel type nationally.
   - Let $Z = \text{the share of passenger cars of your fuel type}$

4. Apply the national shares per fuel type to the number of cars registered in your municipality to get the number of cars per fuel type in your municipality.
   - Let $\text{numbercars}_{fueltype} = Y \times Z$

5. Multiply the number of cars per fuel type with the average yearly km for that fuel type.
   - Let $\text{operations}_{fueltype} = \text{numbercars}_{fueltype} \times X$

## Motorcycles

Per fuel type (petrol, electric (BEV)):

1. From **[SWOV - Instituut voor Wetenschappelijk Onderzoek Verkeersveiligheid](/5-resources/1-data/data-transformation/nl/2-data-descriptors/swov-instituut-voor-wetenschappelijk-onderzoek-verkeersveiligheid.md)** get the yearly average km driven by motorcycles.
   - Let $X$ = average number of km driven by motorcycle.

2. From **dataset [85236NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85236ned.md): Motor vehicles active on January 1; vehicle type, region as of January 1, 2023** take the number of motorcycles registered in your municipality.
   - Let $Y$ = number of motorcycles registered in your municipality.

3. From **dataset [85238NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85238ned.md): Motorcycles active;vehicle characteristics, regions, January1, 2023** get the distribution of motorcycles per fuel type nationally. Please note that there is no actual information on the fuel type, but as a proxy, the number of cylinders can be used where "unknown" is electric motorcycles and all the other petrol. Alternatively, make the assumption that 100% are petrol.
   - Let $Z$ = share of motorcycles of your fuel type.

4. Apply the national shares per fuel type to the number of motorcycles registered in your municipality to get the number of motorcycles per fuel type in your municipality.
   - Let $numbermcs_{fueltype} = Y \times Z$

5. Multiply the number of motorcycles per fuel type with the average yearly km for motorcycles.
   - Let $operations_{fueltype} = numbermcs_{fueltype} \times X$


## Buses

From **dataset [85237NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85237ned.md)**: Passenger cars active; vehicle characteristics, regions, January 1, get the total number of vehicle-km driven for the entire Netherlands with buses. Scale that number down for your municipality using population.

From the same **dataset** calculate the share of buses per fuel type nationally and apply that share to the number of vehicle-km calculated for your municipality to get the vehicle-km driven by buses per fuel type.

## Alternative approach: All private transport based on Google EIE data:
(Recommended)

Distances driven by personal vehicles: The **[Google EIE transport data](/5-resources/1-data/data-transformation/nl/2-data-descriptors/google-eie-transport-data.md) dataset** contains person-km per modality. It also contains distances for different travel bounds as well as GPC distance and total distance. To calculate the value for your city inventory, use the data from **ALL** travel bounds and we recommend using the **GPC distance**.

The modality **AUTOMOBILE** however also contains distances driven by light- and heavy goods vehicles. To get the distance for the personal vehicles, first determine the share of vehicle-kms:



From the **[85395NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85395ned.md): Motor vehicle traffic performance; kilometers, vehicle type, territory**, get the vehicle-kms for the types personal vehicles, heavy goods vehicles (the sum of HGVs excl. tractor trailer and tractor trailer), light goods vehicles.



For each vehicle type, multiply its vehicle-kms with the average load factor to convert them to person-km. Load factor for personal vehicles can be taken from the **[Verkeerskunde NL](/5-resources/1-data/data-transformation/nl/2-data-descriptors/verkeerskunde-nl.md) dataset**, for all other vehicle types, load factor 1 can be assumed.



From the person-kms for all these categories, determine each category's share of the total. Apply those shares to the person-kms of **AUTOMOBILE**.



Thereafter, convert them back to vehicle-kms by dividing that amount by its respective load factor again.



Please note: Depending on the dataset from **Google EIE**, motorcycles sometimes form their own category, sometimes not. In case motorcycles do not have their own category, include motorcycles in the calculations above to determine the shares.



For all the other categories, convert the person-kms to vehicle-kms where necessary for the activity value.



For buses, use local knowledge from the companies operating the bus lines, to divide the person-km between the different fuel types (diesel, petrol, gas, electric).




# Sources

- [85405NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85405ned.md)
- [85236NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85236ned.md)
- [85237NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85237ned.md)
- [85395NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85395ned.md)
- [85238NED](/5-resources/1-data/data-transformation/nl/2-data-descriptors/85238ned.md)
- [Google EIE transport data](/5-resources/1-data/data-transformation/nl/2-data-descriptors/google-eie-transport-data.md)
- [Verkeerskunde NL](/5-resources/1-data/data-transformation/nl/2-data-descriptors/verkeerskunde-nl.md)
- [Quickscan electric motorcycles](/5-resources/1-data/data-transformation/nl/2-data-descriptors/quickscan-electric-motorcycles.md)
- [SWOV - Instituut voor Wetenschappelijk Onderzoek Verkeersveiligheid](/5-resources/1-data/data-transformation/nl/2-data-descriptors/swov-instituut-voor-wetenschappelijk-onderzoek-verkeersveiligheid.md)



