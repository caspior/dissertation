# Creating grid over Austin (0.001x0.001 deg)

os.chdir("C:/Users/orcas/Documents/GitHub/dissertation/shapefiles")

from qgis.core import *
import processing

grid = processing.run("native:creategrid", {'TYPE': '2',
'EXTENT': '-97.9405,-97.5205,30.0705,30.5205',
'HSPACING': 0.001,
'VSPACING': 0.001,
'HOVERLAY': 0,
'VOVERLAY': 0,
'CRS': 'EPSG:4269',
'OUTPUT': 'grid.shp'})


# Refining grid by Austin's Boundaries

boundaries = QgsVectorLayer("tl_2019_48_place/tl_2019_48_place.shp", "boundaries", "ogr")

boundaries.selectByExpression(" \"NAME\" = 'Austin' ")

_writer = QgsVectorFileWriter.writeAsVectorFormat(boundaries, "austin", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
selected_layer = iface.addVectorLayer("austin.shp", '', 'ogr')
del(_writer)

processing.run("qgis:clip", {'INPUT':"grid.shp", 'OVERLAY':"austin.shp", 'OUTPUT':"austin_grid.shp"})


# Change coordinate system to 'State Plane Texas Central'

austin_grid = QgsVectorLayer("austin_grid.shp", "austin", "ogr")
processing.run('native:reprojectlayer', {'INPUT':austin_grid, 'TARGET_CRS':'EPSG:32139', 'OUTPUT':"austin_grid_sp.shp"})