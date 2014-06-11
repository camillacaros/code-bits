import shapefile
import shapely

#Load a shapefile of polygons and convert it to shapely polygon objects
census_tract = shapefile.Reader("/Users/buzz/Documents/Mapbox/process/Arc-to-Mapbox/SD-data/CENSUS_TRACTS_2010.shp")
tract = census_tract.shapes()
tract_pts = [q.points for q in tract ]
from shapely.geometry import Polygon
tract_poly = [Polygon(q) for q in tract_pts]

#Load a shapefile of points and convert it to shapely point objects
tour_attr = shapefile.Reader("/Users/buzz/Documents/Mapbox/process/Arc-to-Mapbox/SD-data/majattrs.shp")
attr = tour_attr.shapes()
from shapely.geometry import Point
attr_coords = [q.points[0] for q in attr ]
attr_pts = [Point(q.points[0]) for q in attr ]

#Build a spatial index based on the bounding boxes of the polygons
from rtree import index
idx = index.Index()
count = -1
for q in tract:
	count +=1
	idx.insert(count, q.bbox)

#Assign one or more matching polygons to each point
matches = []
for i in range(len(attr_pts)): #Iterate through each point
    temp=None
    print "Point ", i
    #Iterate only through the bounding boxes which contain the point
    for j in idx.intersection(attr_coords[i]):
        #Verify that point is within the polygon itself not just the bounding box
        if attr_pts[i].within(tract_poly[j]):
            temp=j
            print "Match found! ",j
            break
    matches.append(temp) #Either the first match found, or None for no matches

print matches
records = tract_poly.records()
print records
