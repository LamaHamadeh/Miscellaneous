#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:54:11 2017

@author: lamahamadeh
"""


#check whether an integer is an Armstrong number or not
#An Armstrong number of three digits is an integer such that the sum of the 
#cubes of its digits is equal to the number itself. 

def Armstrong_Number(number):
    list_number = [int(d) for d in str(number)]    
    cube = [i**3 for i in list_number]    
    sum_digits = sum(cube)    
    if sum_digits == number:
        print('This is an Armstrong number')
    else:
        print('This is NOT an Armstrong number')

print(Armstrong_Number(412))