#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:47:14 2017

@author: lamahamadeh
"""


#Alphabet Order for the letters in a certain word
def AlphabetOrder(string):
    string = string.casefold() #caseless situation
    chars = list(string)
    new_string = sorted(chars)
    return ' '.join(new_string)

print(AlphabetOrder('Hello'))