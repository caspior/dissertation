# Geocode dockless trips

from qgis.core import *

uri = "file:///C:/Users/orcas/Documents/GitHub/dissertation/dockless.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "Start.Longitude", "Start.Latitude","epsg:4269")
starts = QgsVectorLayer(uri,"Starts","delimitedtext")
QgsProject.instance().addMapLayer(starts)

uri = "file:///C:/Users/orcas/Documents/GitHub/dissertation/dockless.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "End.Longitude", "End.Latitude","epsg:4269")
ends = QgsVectorLayer(uri,"Ends","delimitedtext")
QgsProject.instance().addMapLayer(ends)


# Creating grid over Austin (0.001x0.001 deg)

os.chdir("C:/Users/orcas/Documents/GitHub/dissertation/shapefiles")

import processing

grid = processing.run("native:creategrid", {'TYPE': '2',
'EXTENT': '-97.9405,-97.5505,30.0905,30.5205',
'HSPACING': 0.001,
'VSPACING': 0.001,
'HOVERLAY': 0,
'VOVERLAY': 0,
'CRS': 'EPSG:4269',
'OUTPUT': 'grid.shp'})

selected_layer = iface.addVectorLayer("grid.shp", '', 'ogr')


# Refining grid by Austin's Boundaries

boundary_path = "BOUNDARIES_jurisdictions/geo_export_498cd848-1828-48cf-a5c5-bdc10f628774.shp" #geometry problems!!
boundaries = QgsVectorLayer(boundary_path, "boundaries", "ogr")
QgsProject.instance().addMapLayer(boundaries)

boundaries.selectByExpression(" \"globalid\" = '6a4e125f-2404-48fb-8c88-8697bfa0a306' ")

_writer = QgsVectorFileWriter.writeAsVectorFormat(boundaries, "austin", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
selected_layer = iface.addVectorLayer("austin.shp", '', 'ogr')
del(_writer)

processing.run("qgis:clip", {'INPUT':"grid.shp", 'OVERLAY':"austin.shp", 'OUTPUT':"austin_grid.shp"})