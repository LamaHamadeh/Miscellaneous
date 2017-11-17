#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:47:57 2017

@author: lamahamadeh
"""



#find the longest word in a string
def longest_word(string):
    words = string.split()
    longest_word = ' '
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(longest_word('today is Thursday'))
