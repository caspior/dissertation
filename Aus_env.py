# Creating grid over Austin (0.001x0.001 deg)

os.chdir("C:/Users/orcas/Documents/GitHub/dissertation/shapefiles")

from qgis.core import *
import processing


# Loading the grid with the aggregated trips

grid = QgsVectorLayer("grid_trips.shp", "grid", "ogr")


# Calculate polygons' area

pv = grid.dataProvider()
pv.addAttributes([QgsField('cell_area', QVariant.Double)])
grid.updateFields()
expression = QgsExpression('$area')
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(grid))
with edit(grid):
    for f in grid.getFeatures():
        context.setFeature(f)
        f['cell_area'] = expression.evaluate(context)
        grid.updateFeature(f)


# Land uses

## load land use
land_use = QgsVectorLayer("Land Use Inventory Detailed/geo_export_4be3cc52-d894-42aa-bff9-80a4462a1f52.shp", "land_use", "ogr")
#QgsProject.instance().addMapLayer(land_use)

def lu_prop(lu):

    ## divide by land use
    if lu == 'Residential':
        land_use.selectByExpression(" \"land_use\" >= 100 and  \"land_use\" < 300")
    elif lu == 'Commercial':
        land_use.selectByExpression(" \"land_use\" >= 300 and  \"land_use\" < 500")
    elif lu == 'Educational':
        land_use.selectByExpression(" \"land_use\" = 650")
    elif lu == 'Institutional':
        land_use.selectByExpression(" (\"land_use\" >= 600 and  \"land_use\" < 650) or \"land_use\" = 670 or \"land_use\" = 710")
    elif lu == 'Industrial':
        land_use.selectByExpression(" \"land_use\" >= 500 and  \"land_use\" < 600")
    elif lu == 'Recreational':
        land_use.selectByExpression(" \"land_use\" >= 720 and  \"land_use\" < 810")

    path = 'land_use/' + lu
    input = path + '.shp
    dissolve = path + '_dis.shp
    intersection = path + '_int.shp

    _writer = QgsVectorFileWriter.writeAsVectorFormat(land_use, path, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    del(_writer)
    
    from processing.tools import dataobjects
    context = dataobjects.createContext()
    context.setInvalidGeometryCheck(QgsFeatureRequest.GeometryNoCheck)

    ##intersect
    processing.run('qgis:intersection', {'INPUT': "grid_trips.shp", 'OVERLAY': input, 'OUTPUT': intersection})
    ##dissolve
    processing.run('native:dissolve',{'INPUT':intersection, 'FIELD':["id"], 'OUTPUT':dissolve},context=context)

    ##caculate areas and proportion
    lu_grid = QgsVectorLayer(dissolve, "lu_grid", "ogr")
    
    field = lu[:3] + '_prop'
    pv = lu_grid.dataProvider()
    pv.addAttributes([QgsField('lu_area', QVariant.Double), QgsField(field, QVariant.Double)])
    lu_grid.updateFields()
    expression1 = QgsExpression('$area')
    expression2 = QgsExpression('"lu_area"/"area"')
    context = QgsExpressionContext()
    context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(lu_grid))
    with edit(lu_grid):
        for f in lu_grid.getFeatures():
            context.setFeature(f)
            f['area'] = expression1.evaluate(context)
            f[field] = expression2.evaluate(context)
            lu_grid.updateFeature(f)

    