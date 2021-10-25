# Creating grid over Austin (0.001x0.001 deg)

os.chdir("C:/Users/orcas/Documents/GitHub/dissertation/shapefiles")

from qgis.core import *
import processing

grid = processing.run("native:creategrid", {'TYPE': '2',
'EXTENT': '-97.9405,-97.5505,30.0905,30.5205',
'HSPACING': 0.001,
'VSPACING': 0.001,
'HOVERLAY': 0,
'VOVERLAY': 0,
'CRS': 'EPSG:4269',
'OUTPUT': 'grid.shp'})


# Refining grid by Austin's Boundaries

boundary_path = "https://opendata.arcgis.com/datasets/09cd5b6811c54857bd3856b5549e34f0_0.geojson"
boundaries = QgsVectorLayer(boundary_path, "boundaries", "ogr")

boundaries.selectByExpression(" \"CITY_NM\" = 'Austin' ")

_writer = QgsVectorFileWriter.writeAsVectorFormat(boundaries, "austin", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
selected_layer = iface.addVectorLayer("austin.shp", '', 'ogr')
del(_writer)

processing.run("qgis:clip", {'INPUT':"grid.shp", 'OVERLAY':"austin.shp", 'OUTPUT':"austin_grid.shp"})


# Change coordinate system to 'State Plane Texas Central'

austin_grid = QgsVectorLayer("austin_grid.shp", "austin", "ogr")
processing.run('native:reprojectlayer', {'INPUT':austin, 'TARGET_CRS':'EPSG:32139', 'OUTPUT':"austin_grid_sp.shp"})


# Geocode dockless trips

uri = "file:///C:/Users/orcas/Documents/GitHub/dissertation/dockless.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "Start.Longitude", "Start.Latitude","epsg:4269")
starts = QgsVectorLayer(uri,"Starts","delimitedtext")

uri = "file:///C:/Users/orcas/Documents/GitHub/dissertation/dockless.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "End.Longitude", "End.Latitude","epsg:4269")
ends = QgsVectorLayer(uri,"Ends","delimitedtext")
#QgsProject.instance().addMapLayer(ends)


# Aggregating trips


