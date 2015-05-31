#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import sys
from rtree import index
from shapely.geometry import Point, Polygon

# TODO: read geo zones from geojson file

# create spatial index
idx = index.Index()
for it, zone in enumerate(geo_zones):
    idx.insert(it, geo_zones[it]["bounds"])

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    id, lat, lon, where = line.split(';')
    lat = float(lat)
    lon = float(lon)
    gps_point = Point(lon, lat)
    gps_point_buffer = gps_point.buffer(0.0002)
    for zId in list(idx.intersection(gps_point_buffer.bounds)):
        if geo_zones[zId]["polygon"].contains(gps_point_buffer):
            print('{}\t{}\t{}\t{}'.format(
                geo_zones[zId]["name"], id, str(lat), str(lon)))
            break
