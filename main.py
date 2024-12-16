from shapely.geometry import Polygon, Point
import geopandas as gpd
import json

def mean(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)


# Address
data = json.load(open('addresses.json', 'r'))

print(len(data.keys()))

points = []

for address in data.keys():
    long = data[address][1]
    lat = data[address][0]
    address_point = Point(long, lat)
    address_point_gs = gpd.GeoSeries([address_point], crs='EPSG:4326')
    address_point_gs = address_point_gs.to_crs(epsg=32611)
    points.append(address_point_gs)


# Define a polygon using longitude and latitude
polygon_1 = Polygon([(-118.07136, 34.01885), (-118.24921, 34.05641), (-118.25127, 34.10361), (-118.02879, 34.1667), (-118.07136, 34.01885)])
polygon_2 = Polygon([(-117.80701, 34.06437), (-117.86262, 34.0143), (-117.89352, 34.02739), (-117.8846, 34.07063), (-117.80701, 34.06437)])
polygon_3 = Polygon([(-117.83928, 33.99893), (-117.86262, 33.95452), (-118.00133, 33.98812), (-117.98416, 34.01487), (-117.83928, 33.99893)])
polygon_4 = Polygon([(-118.02947, 33.8447), (-118.06518, 33.8447), (-118.0638, 33.89316), (-118.03496, 33.8886), (-118.02947, 33.8447)])
polygon_5 = Polygon([(-118.37897, 33.75112), (-118.41262, 33.7477), (-118.4188, 33.76311), (-118.39271, 33.76368), (-118.39202, 33.77738), (-118.38035, 33.77795), (-118.37897, 33.75112)])
polygon_6 = Polygon([(-118.43589, 34.05431), (-118.44963, 34.05431), (-118.44963, 34.06768), (-118.43521, 34.06853), (-118.43589, 34.05431)])


# Convert the polygon into a GeoSeries

polygon_gs1 = gpd.GeoSeries([polygon_1], crs='EPSG:4326')
polygon_gs2 = gpd.GeoSeries([polygon_2], crs='EPSG:4326')
polygon_gs3 = gpd.GeoSeries([polygon_3], crs='EPSG:4326')
polygon_gs4 = gpd.GeoSeries([polygon_4], crs='EPSG:4326')
polygon_gs5 = gpd.GeoSeries([polygon_5], crs='EPSG:4326')
polygon_gs6 = gpd.GeoSeries([polygon_6], crs='EPSG:4326')

# Reproject the polygon to a CRS that uses meters (e.g., EPSG:3395 or EPSG:3857)
polygon_projected1 = polygon_gs1.to_crs(epsg=32611)  # EPSG:3395 is a global projection in meters
polygon_projected2 = polygon_gs2.to_crs(epsg=32611)
polygon_projected3 = polygon_gs3.to_crs(epsg=32611)
polygon_projected4 = polygon_gs4.to_crs(epsg=32611)
polygon_projected5 = polygon_gs5.to_crs(epsg=32611)
polygon_projected6 = polygon_gs6.to_crs(epsg=32611)

projected_polygons = [polygon_projected1, polygon_projected2, polygon_projected3, polygon_projected4, polygon_projected5, polygon_projected6]

min_distances = []

for point in points:
    distances = []
    for polygon in projected_polygons:
        dist = point.distance(polygon[0])[0] / 1609.344
        distances.append(dist)
    min_distances.append(min(distances))

print(f"The average minimum distances is: {mean(min_distances)} miles")
print(f"The average minimum distances is: {sum(min_distances) / (len(min_distances)-5)} miles")

# for p in projected_polygons:
#     d = address_point_gs.distance(p[0])[0] / 1609.344
#     distances.append(d)

# for d in distances:
#     print(d)
