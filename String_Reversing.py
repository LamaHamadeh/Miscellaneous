#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:42:14 2017

@author: lamahamadeh
"""



#code for reversing a string

def reverse_a_string(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1  # index = index - 1
        new_string += a_string[index] # new_string = new_string + character
    return new_string

print(reverse_a_string('My name is Lama')) 