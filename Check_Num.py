#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:45:56 2017

@author: lamahamadeh
"""


#Check Nums
def CheckNums(num1,num2): 
    if num2 > num1:
        return True
    if num2 < num1:
        return False
    if num2 == num1:
        return '-1'

print(CheckNums(2,3))


#find the second highest number in an integer list
num_list = [1, 2, 8, 3, 12]
print(sorted(num_list, reverse=True)[1])


#find the largest and smallest number in an array
num_list = [1, 2, 8, 3, 12]
print(max(num_list))
print(min(num_list))
