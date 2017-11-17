#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:48:24 2017

@author: lamahamadeh
"""


#Vowel count in astring/word
sentence = 'This is my name: Lama'

counts = {i:0 for i in 'aeiouAEIOU'}

for char in sentence:
    if char in counts:
        counts[char] += 1

for k,v in counts.items():
    print(k,v)

#------------------------
    
#word count in a string
def count_words(sentence):
    sentence = sentence.casefold()
    count_words = {}
    words = sentence.split()
    for word in words:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1
    return count_words

print(count_words('My daughter and I are having a good time'))

#------------------------

#Vowel count in astring/word
sentence = 'This is my name: Lama'

counts = {i:0 for i in 'aeiouAEIOU'}

for char in sentence:
    if char in counts:
        counts[char] += 1

for k,v in counts.items():
    print(k,v)
    
#------------------------
    
#letter count in a string
def count_letters(sentence):
    count_letters = {}
    for letter in sentence:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1
    return count_letters

print(count_letters("Hello My name is Lama"))

#------------------------

#count the number of palindromes in a given string
def palindrome(string):
    string = string.casefold()
    words = string.split()
    palindrome_counts = {}    
    for word in words:
        rev_word = reversed(word)
        if list(word) == list(rev_word):
            if word in palindrome_counts:
                palindrome_counts[word] += 1
            else:
                palindrome_counts[word] = 1
    return palindrome_counts

print(palindrome('Nan Bread is a must when going to an indian restaurant'))    

#------------------------


#specific letter count
def count_specific_letter(word, to_find):
    count = 0
    for char in word:
        if char == to_find:
            count += 1
    return count

print(count_specific_letter('Lama','a'))

#------------------------

#to get the most common character in the string
from collections import Counter
most_common_letter = Counter("Hello My name is Lama").most_common(1)          
print(most_common_letter)

#------------------------
