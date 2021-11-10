# Equity Implications of Electric Bikesharing in Philadelphia

### Abstract
In this chapter, I examine the influence of the added e-bikes on Philadelphia's bikeshare on usage in disadvantaged neighborhoods in the city. Indego, Philadelphia's bikeshare, embraced the promotion of equity as part of its primary goals. While previous measures were not adequate for that cause, Indego decided to integrate e-bikes into its system to promote usage among current non-users. In my analysis, I combined official publicly available data using spatial analysis methods. Furthermore, I used random forest and spatial negative binomial regression to examine factors influencing shared bicycle and e-bike usage in Philadelphia. The findings show that e-bikes increase the overall usage of Indego, specifically in disadvantaged areas. In these regions, the users use shared e-bikes for both commute and other utilitarian purposes, while in the rest of the city, users use e-bikes mainly for commuting. While in the first few months, the ridership in disadvantaged areas was similar to the usage elsewhere, the usage in those areas later declined. I concluded that the integration of e-bikes was successful in increasing bikesharing usage in disadvantaged areas in the short term.

### Data
All the data in this research obtained from openly available online databases.
- Austin's dockless micromobility trip log retrieved from [the official City of Austin open data portal](https://data.austintexas.gov/Transportation-and-Mobility/Shared-Micromobility-Vehicle-Trips/7d8e-dm7r/data) on March 28th 2019. [The dataset I retrieved](https://drive.google.com/file/d/1uHDza25XWuaCml3jeToR6JMtOgbNwScx/view?usp=sharing) includes trip start and end coordinates which are masked in newer trip logs. I cleaned and prepared the dockless trip log with this [script](Aus_Cleaning.R).
- Austin's bikesharing trip log was also retrieved from [the official City of Austin open data portal](https://data.austintexas.gov/Transportation-and-Mobility/Austin-MetroBike-Trips/tyfh-5r8s). I cleaned and prepared the bikesharing trip log with this [script](Aus_Cleaning_B.R).
- From the [US Census Bureau](https://data.census.gov/), I retrieved the American Community Survey (ACS) 2014-2018 5-year estimates. I retrieved the total population (variable B01003), sex (B01001), race (B02001), median income by household (B19013), poverty status by household (B17017), school enrollment (B14007), and the aggregate number of total vehicles available in the Census Block Group (B25046).
- Shapefiles retrieved from various sources:
  - Census Block Groups - [TIGER US Census Bureau](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2019&layergroup=Block+Groups).
  - City boundaries - [TIGER US Census Bureau](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2019&layergroup=Places).
  - Land uses - [the official City of Austin open data portal](https://data.austintexas.gov/Locations-and-Maps/Land-Use-Inventory-Detailed/fj9m-h5qy).
  - Street network - [the official City of Austin open data portal](https://data.austintexas.gov/Locations-and-Maps/Street-Centerline/m5w3-uea6)
  - Bikesharing stations - [the official City of Austin open data portal](https://data.austintexas.gov/Transportation-and-Mobility/Austin-MetroBike-Kiosk-Locations/qd73-bsdg)
  - Bus stops - [the official City of Austin open data portal](https://data.texas.gov/Transportation/Capital-Metro-Shapefiles-JANUARY-2020/63b7-hxaj)
  - Employment - [US Census Bureau Center for Economic Studies](https://lehd.ces.census.gov/data/)
  - Bikways were retrieved from [Open Street Map](https://www.openstreetmap.org/) using the [QuickOSM](https://plugins.qgis.org/plugins/QuickOSM/) plugin for QGIS.

### GIS

### Descriptive Statistics

### Moran's I

### Random Forest

### Spatial Negative Binomial Regression
