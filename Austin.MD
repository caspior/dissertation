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
  - Land uses - [the official City of Austin open data portal](https://data.austintexas.gov/Locations-and-Maps/Land-Use-Inventory-Detailed/fj9m-h5qy).
  - Street network - [the official City of Austin open data portal](https://data.austintexas.gov/Locations-and-Maps/Street-Centerline/m5w3-uea6)
  - Bikesharing stations - [the official City of Austin open data portal](https://data.austintexas.gov/Transportation-and-Mobility/Austin-MetroBike-Kiosk-Locations/qd73-bsdg)
  - Bus stops - [the official City of Austin open data portal](https://data.texas.gov/Transportation/Capital-Metro-Shapefiles-JANUARY-2020/63b7-hxaj)
  - Employment - [US Census Bureau Center for Economic Studies](https://lehd.ces.census.gov/data/)
  - Bikways were retrieved from [Open Street Map](https://www.openstreetmap.org/) using the [QuickOSM](https://plugins.qgis.org/plugins/QuickOSM/) plugin for QGIS.

### GIS
For the purpose of advanced statistics and machine learning I aggregated the trips by polygons using this [PyQGIS script](Aus_trips.py). I created a 0.001x0.001 degrees grid over the city of Austin and aggregated trips starts and ends for the entire examined period (Aug 16th 2018 - Feb 28th 2019), only weekday morning trips, only weekday evening trips, and only weekend and holiday trips.

*More GIS analysis scripts to come

### Descriptive Statistics
Trips' descriptive statistical analysis performed using this [R script](Aus_Descriptive.R). This [R markdown output](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_descriptive.html) presents the code alongside the charts. This [chart](Aus_variablesX.MD) defines the independednt variables used in this research. This [chart](Aus_variablesY.MD) defines the independednt variables used in this research.

### Moran's I
The moran's I test examines whether a variable is sptially autocorrelated. Significnt results indictes a spatial autocorrelated - hence there is a spatial relationship between the study units and a spatial model is required for the analysis. I used this [R Markdown](Aus_MoransI.Rmd) and you can see the output [here](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_MoransI.html).

### Random Forest
I used random forest in my dissertation to be able to compare different types of shared micromobility with different distributions. I uaed the 'Increased MSE' parameter to evaluate the importance of each feature to the ridership. I used this [R Markdown](Aus_RF.Rmd) also available in [R script format](Aus_RF.R). You can see the output [here](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_RF.html).


### Spatial Lag, Spatial Error, and Spatial Durbin
I used three spatial regression models to evaluate the role of the features on e-scooter ridership:
- **Spatial Lag** - the spatial component derives from the weighted (W) y values of adjacent polygons multiply by the rho coefficient and appears as an additional feature in the model's equation: <img src="https://render.githubusercontent.com/render/math?math=y = \rho Wy %2B x\beta %2B \epsilon">
- **Spatial Error** - the spatial component derives from the weighted (W) error term multiply by the lambda coefficient: <img src="https://render.githubusercontent.com/render/math?math=y = x\beta %2B \epsilon"> where <img src="https://render.githubusercontent.com/render/math?math=\epsilon = x\lambda W\epsilon %2B u">
- **Sptial Durbin** - the spatial component derives from the the wieghted (W) y values of adjacent polygons multiply by the rho coefficient and the weighted (W) x vaules of adjacent polygons multiply by the theta coefficinets (different coefficient for each feature): <img src="https://render.githubusercontent.com/render/math?math=y = \rho Wy %2B Wx\theta %2B \epsilon">.

I used this [R Markdown](Aus_Spreg.Rmd) and you can see the output [here](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_Spreg.html).


### Geographically Weighted Regression (GWR)
GWR models estimate the effect of local rather than global independent variable coefficients by including only a limited region for estimating the variable coefficients for each study unit. I estimated models for two dependent variables in the city center area – all arrival trips and morning arrival trips. Since GWR is a linear regression I logged the ridership variables.

For the GWR analysis I used ArcGIS Desktop's GUI. The spatial distribution of the variables used in this analysis can be found [here](Aus_Spatial_variables.pdf). The GWR outputs can be found [here](Aus_GWR_all.pdf) for all the trips and [here](Aus_GWR_mornings.pdf) for the morning trips.


### Linear Regression
The final step in my analysis included a linear regression with the Median Annual Income coefficient from the GWR models as the depentend variable. I used this [R Markdown](Aus_LM.Rmd) and you can see the output [here](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_LM.html).

### Summary Table
| Description | Script | Input | Output |
| --- | --- | --- | --- |
| Cleaning the dockless trip log | [R](Aus_Cleaning.R) | [Austin's dockless trip log](https://drive.google.com/file/d/1uHDza25XWuaCml3jeToR6JMtOgbNwScx/view?usp=sharing) | |
| Cleaning the bikesharing trip log | [R](Aus_Cleaning_B.R) | [Austin's bikesharing trip log](https://data.austintexas.gov/Transportation-and-Mobility/Austin-MetroBike-Trips/tyfh-5r8s) | |
| Descriptive statistics | [R](Aus_Descriptive.R) | Outputs of trip log cleaning scripts, [Origin destination matrix](OD_matrix.csv) | [R Markdown](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_descriptive.html) |
| Moran's I | [R Markdown](Aus_MoransI.Rmd) | [Grid shapefile](Austin_grid.zip) | [R Markdown](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_MoransI.html) |
| Random Forest | [R](Aus_RF.R), [R Markdown](Aus_RF.Rmd) | [Grid shapefile](Austin_grid.zip) | [R Markdown](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_RF.html) |
| Spatial Regressions | [R Mardown](Aus_Spreg.Rmd) | [Grid shapefile](Austin_grid.zip) | [R Markdown](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_Spreg.html) |
| Geographically Weighted Regression | | [Grid shapefile](Austin_grid.zip) | [All trips](Aus_GWR_all.pdf), [Morning trips](Aus_GWR_mornings.pdf) |
| Linear Regression | [R Markdown](Aus_LM.Rmd) | GWR output | [R Markdown](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/Aus_LM.html) |

[Dependent variables](Aus_variablesY.MD)

[Independent variables](Aus_variablesX.MD)
