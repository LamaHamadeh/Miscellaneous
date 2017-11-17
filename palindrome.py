#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:56:09 2017

@author: lamahamadeh
"""


#check if a string is palindrome or not
word = 'Nan'
word = word.casefold() #for caseless comparison
rev_word = reversed(word)
if list(word) == list(rev_word):
    print('This word is palindrome')
else:
    print('This word is NOT palindrome')

