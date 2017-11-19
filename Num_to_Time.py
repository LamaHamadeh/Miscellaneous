#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:46:26 2017

@author: lamahamadeh
"""



#the following code converts a number to a time: hours:minutes
import math

def TimeConvert(num):
    hours = int(math.floor(num/60)) # returns the largest integer value less 
    #than or equal to x.
    minutes = num % 60
    return str(hours) + ':' + str(minutes)

print(TimeConvert(350))
#-----------------------------------

#this code converts time into words

#Hours dictionary
hour_dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
             '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', 
             '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', 
              '15':'fifteen', '16':'sixteen', '17':'seventeen', 
              '18':'eighteen', '19':'nineteen', '20':'twenty', 
              '21':'twenty one', '22':'twenty two', '23':'twenty three',
              '24':'twenty four'}
#minutes ones dictionary
minute_dict_ones = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
                    '6':'six', '7':'seven', '8':'eight', '9':'nine', 
                    '11':'eleven', '12':'twelve', '13':'thirteen', 
                    '14':'fourteen', '15':'fifteen', '16':'sixteen', 
                    '17':'seventeen', '18':'eighteen', '19':'nineteen'}
#minutes tens dictionary
minute_dict_tens = {'1':'ten', '2':'twenty', '3':'thirty', '4':'fourty', 
                    '5':'fifty'}

def Time2wordConverter(time):
    """This function converts digital time, i.e., (hour:minutes) into words"""
    #splitting the time into hours and minutes
    hour, minute = time.split(':')[0], time.split(':')[1]
    #hours
    if int(hour) == 0:
        suffix = 'a.m.'
        hour = hour_dict['12']
    if int(hour) == 12:
        suffix = 'p.m.'
        hour = hour_dict['12']
    if (int(hour) > 0) and (int(hour) < 12):
        suffix = 'a.m.'
        hour = hour_dict[str(int(hour))]
    else:
        suffix = 'p.m'
        hour = hour_dict[str(int(hour) - 12)]
         
    #minutes    
    if (str(int(minute)) in minute_dict_ones) and (int(minute) < 10):
         minute = "oh " + minute_dict_ones[str(int(minute))] + ' '
    if (list(str(minute))[0] == '0') and (list(str(minute))[1] == '0'):
        minute = ' '
    if list(str(minute))[1] == '0':
        minute = minute_dict_tens[list(str(minute))[0]] 
    else:
        minute = minute_dict_tens[list(str(minute))[0]] + ' ' + minute_dict_ones[list(str(minute))[1]] 
    
    #output    
    return ('it is '+ hour + ' ' + minute + ' ' + suffix)


print(Time2wordConverter('23:10'))

#-----------------------------------


