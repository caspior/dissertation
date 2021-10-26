# Shared Micromobility Usage Patterns in Austin, Texas

### Abstract
In this chapter, I examine dockless e-scooter and e-bike sharing usage patterns in Austin, Texas, and compare them with the city's bikeshare. I spatially analyzed micromobility trip logs with respect to the built environment and sociodemographics. I used various spatial regression models and random forest models to examine the influence of different factors on micromobility trips. Results show that micromobility usage in Austin increased due to the introduction of dockless micromobility sharing services, while bikesharing usage did not decrease. Shared e-scooters and e-bikes are mainly used in regions served by bikesharing and increase micromobility usage outside these regions. E-bikes are apparently mainly used for commuting, while e-scooters and bicycles are used for short utilitarian trips. My findings suggest that micromobility modes cover all trip purposes, serving residents’ various activity needs.

### Data
All the data in this research obtained from openly available online databases.
- Austin's dockless micromobility trip log retrieved from [the official City of Austin open data portal](https://data.austintexas.gov/Transportation-and-Mobility/Shared-Micromobility-Vehicle-Trips/7d8e-dm7r/data) on March 28th 2019. [The dataset I retrieved](https://drive.google.com/file/d/1uHDza25XWuaCml3jeToR6JMtOgbNwScx/view?usp=sharing) includes trip start and end coordinates which are masked in newer trip logs. I cleaned and prepared the dockless trip log with this [script](Aus_Cleaning.R).
- Austin's bikesharing trip log was also retrieved from [the official City of Austin open data portal](https://data.austintexas.gov/Transportation-and-Mobility/Austin-MetroBike-Trips/tyfh-5r8s). I cleaned and prepared the bikesharing trip log with this [script](Aus_Cleaning_B.R).
- From the [US Census Bureau](https://data.census.gov/), I retrieved the American Community Survey (ACS) 2014-2018 5-year estimates. I retrieved the total population (variable B01003), sex (B01001), race (B02001), median income by household (B19013), poverty status by household (B17017), school enrollment (B14007), and the aggregate number of total vehicles available in the Census Block Group (B25046).
- Shapefiles retrieved from various sources:
  - Census Block Groups - [TIGER US Census Bureau](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2019&layergroup=Block+Groups).
  - City boundaries - [TIGER US Census Bureau](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2019&layergroup=Places).
  - Land uses - [the official City of Austin open data portal](https://data.austintexas.gov/Locations-and-Maps/Land-Use-Inventory-Detailed/fj9m-h5qy)

### GIS
