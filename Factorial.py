#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:40:45 2017

@author: lamahamadeh
"""

# code a factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n=int(input("Input a number to compute the factiorial : "))

print(factorial(n))