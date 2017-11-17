#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:57:22 2017

@author: lamahamadeh
"""


#prime number
def prime_number(number):
    for factor in range (2,number):
        if number % factor == 0:
            print(str(number) + ' ' + "is NOT a prime number")
            break
        else:
            print(str(number) + ' ' + "is a prime number")

print(prime_number(5))


