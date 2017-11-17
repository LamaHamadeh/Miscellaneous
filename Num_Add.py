#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:44:08 2017

@author: lamahamadeh
"""


#add up all the numbers from 1 to num.

def SimpleAdding(num):
    for i in range (num):
        num = i + num
    return num
    
print(SimpleAdding(5))