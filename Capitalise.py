#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:43:08 2017

@author: lamahamadeh
"""



#capatilise the first letter in a sentence

string = 'the brown fox'

string = string[0].upper() + string[1:]
print(string)


#capatalise each first letter in each word in a sentence

input = "they're bill's friends from the uk"

words = input.split(' ')
capatalised_words = []
for word in words:
    first_letter = word[0].upper() + word[1:]
    capatalised_words.append(first_letter)
output = ' '.join(capatalised_words)

print(input)
print(output)


#capatalise the nth letter in a string
def capitalize_nth(string, n):
    return string[:n].lower() + string[n:].capitalize()