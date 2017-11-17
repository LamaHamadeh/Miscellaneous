#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:46:26 2017

@author: lamahamadeh
"""



#difference in hours and minutes between two given times
import math

def TimeConvert(num):
    hours = int(math.floor(num/60)) # returns the largest integer value less 
    #than or equal to x.
    minutes = num % 60
    return str(hours) + ':' + str(minutes)

print(TimeConvert(350))