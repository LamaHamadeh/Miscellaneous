#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:56:58 2017

@author: lamahamadeh
"""



#calculate the distance between two points
import math

def distance(point1, point2):
    dist = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return dist

print(distance((1,2),(4,5)))
