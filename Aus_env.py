# Creating grid over Austin (0.001x0.001 deg)

os.chdir("C:/Users/orcas/Documents/GitHub/dissertation/shapefiles")

from qgis.core import *
import processing


# Loading the grid with the aggregated trips

grid = QgsVectorLayer("grid_trips.shp", "grid", "ogr")


# Calculate polygons' area

pv = grid.dataProvider()
pv.addAttributes([QgsField('area', QVariant.Double)])
grid.updateFields()
expression = QgsExpression('$area')
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(grid))
with edit(grid):
    for f in grid.getFeatures():
        context.setFeature(f)
        f['area'] = expression.evaluate(context)
        grid.updateFeature(f)


# Land uses

land_use = QgsVectorLayer("Land Use Inventory Detailed/geo_export_4be3cc52-d894-42aa-bff9-80a4462a1f52.shp", "land_use", "ogr")
#QgsProject.instance().addMapLayer(land_use)

land_use.selectByExpression(" \"land_use\" >= 100 and  \"land_use\" < 300")
_writer = QgsVectorFileWriter.writeAsVectorFormat(land_use, "land_use/Residential", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)

land_use.selectByExpression(" \"land_use\" >= 300 and  \"land_use\" < 500")
_writer = QgsVectorFileWriter.writeAsVectorFormat(land_use, "land_use/Commercial", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)

land_use.selectByExpression(" \"land_use\" = 650")
_writer = QgsVectorFileWriter.writeAsVectorFormat(land_use, "land_use/Educational", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)

land_use.selectByExpression(" (\"land_use\" >= 600 and  \"land_use\" < 650) or \"land_use\" = 670 or \"land_use\" = 710")
_writer = QgsVectorFileWriter.writeAsVectorFormat(land_use, "land_use/Institutional", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)

land_use.selectByExpression(" \"land_use\" >= 500 and  \"land_use\" < 600")
_writer = QgsVectorFileWriter.writeAsVectorFormat(land_use, "land_use/Industrial", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)

land_use.selectByExpression(" \"land_use\" >= 720 and  \"land_use\" < 810")
_writer = QgsVectorFileWriter.writeAsVectorFormat(land_use, "land_use/Recreational", 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
del(_writer)