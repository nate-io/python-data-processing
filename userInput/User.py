# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 06:04:16 2020

@author: nate
"""

def milesToKm(miles):
  CONVERSION_RATE = 1.60934
  km = miles * CONVERSION_RATE

  print(km, 'km')
  return km

m = input('Please enter miles: ')
m = float(m)

milesToKm(m)