# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 06:35:16 2020

@author: nate
"""

import simplekml

OUTPUT_FILE = "D:\\python-course-files\\exercises-output\\user.kml"

def generateKmlPoint(lon, lat):
  # sanitize
  cleanLon = float(lon)
  cleanLat = float(lat)

  # init   
  kml = simplekml.Kml()
  kml.newpoint(name="User Point", coords=[(cleanLon, cleanLat)])

  kml.save(OUTPUT_FILE)


lon = input('Please enter a longitude: ')
lat = input('Please enter a latitude: ')

generateKmlPoint(lon, lat)