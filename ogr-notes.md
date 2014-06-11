echo "Open a point based shapefile in iPython with OGR"
#cd to folder where data lives


ipython
import osgeo.ogr

shapeData = osgeo.ogr.Open('filename.shp')

#shapeData. *tab* will give you all options

#get the first layer
layer = shapeData.GetLayer()

#get the spatial reference of the layer
spatialReference = layer.GetSpatialRef() 
spatialReference.ExportToProj4()

#examine the first point
feature = layer.GetFeature(0)
geometry = feature.GetGeometryRef()
geometry.GetX()
geometry.GetY()

#collect points in a list
shapeData = osgeo.ogr.Open('filename.shp')
layer = shapeData.GetLayer()
points = []
for index in xrange(layer.GetFeatureCount()):
	feature = layer.GetFeature(index)
	geometry = feature.GetGeometryRef()
	points.append((geometry.GetX(), geometry.GetY()))

#display points
points
#returns a list of coordinates