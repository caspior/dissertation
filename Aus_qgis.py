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

boundaries = QgsVectorLayer("tl_2021_48_place/tl_2021_48_place.shp", "boundaries", "ogr")

boundaries.selectByExpression(" \"NAME\" = 'Austin' ")

_writer = QgsVectorFileWriter.writeAsVectorFormat(boundaries, "austin", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
selected_layer = iface.addVectorLayer("austin.shp", '', 'ogr')
del(_writer)

processing.run("qgis:clip", {'INPUT':"grid.shp", 'OVERLAY':"austin.shp", 'OUTPUT':"austin_grid.shp"})


# Change coordinate system to 'State Plane Texas Central'

austin_grid = QgsVectorLayer("austin_grid.shp", "austin", "ogr")
processing.run('native:reprojectlayer', {'INPUT':austin_grid, 'TARGET_CRS':'EPSG:32139', 'OUTPUT':"austin_grid_sp.shp"})


# Geocode dockless trips

uri = "file:///C:/Users/orcas/Documents/GitHub/dissertation/dockless.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "Start.Longitude", "Start.Latitude","epsg:4269")
starts = QgsVectorLayer(uri,"Starts","delimitedtext")

uri = "file:///C:/Users/orcas/Documents/GitHub/dissertation/dockless.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "End.Longitude", "End.Latitude","epsg:4269")
ends = QgsVectorLayer(uri,"Ends","delimitedtext")
#QgsProject.instance().addMapLayer(ends)

 
# Aggregating trips

def agg_field(agg):
    path = 'counts/' + agg + '.shp'
    layer = QgsVectorLayer(path, agg, "ogr")
    pv = layer.dataProvider()
    pv.addAttributes([QgsField(agg, QVariant.Int)])
    layer.updateFields()
    expression = QgsExpression('"ID_count"')
    context = QgsExpressionContext()
    context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))
    with edit(layer):
        for f in layer.getFeatures():
            context.setFeature(f)
            f[agg] = expression.evaluate(context)
            layer.updateFeature(f)

def agg_trips(grid,direction,time):
    agg = direction + '_' + time
    path = 'counts/' + agg + '.shp'
    if direction=='ends':
        direction_points = ends
    elif direction=='strats':
        direction_points = starts
    else:
        print("Direction is wrong")
    #processing.run("qgis:joinbylocationsummary", {'INPUT':grid, 'JOIN':direction_points, 'OUTPUT':path})
    
    #agg_field(agg)

    #fields = ['left', 'top', 'right', 'bottom', 'field_1_co', 'ID_count', 'Device.ID_', 'Vehicle.Ty', 'Trip.Durat', 'Trip.Dista', 'Start.Time', 'End.Time_c', 'Modified.D', 'Month_coun', 'Hour_count', 'Day.of.Wee', 'Council.Di', 'Council._1', 'Origin.Cel', 'Destinatio', 'Year_count', 'Start.Lati', 'Start.Long', 'End.Latitu', 'End.Longit', 'date_count', 'dayname_co', 'time_start', 'numeric_st', 'time_end_c', 'holiday_co', 'weekend_co', 'speed_coun']
    #path2 = path + '2'
    #processing.run('native:deletecolumn', {'INPUT':path, 'COLUMN':fields, 'OUTPUT':path2})


## All starts
agg_trips("austin_grid_sp.shp","starts","all")