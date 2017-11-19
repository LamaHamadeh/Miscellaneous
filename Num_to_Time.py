#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:46:26 2017

@author: lamahamadeh
"""



#the following code converts a number to a time: hours:minutes
import math

def TimeConvert(num):
    hours = int(math.floor(num/60)) # returns the largest integer value less 
    #than or equal to x.
    minutes = num % 60
    return str(hours) + ':' + str(minutes)

print(TimeConvert(350))
#-----------------------------------

#this code converts the time to words



