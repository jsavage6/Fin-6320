# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:00:01 2017

@author: Joshua
"""

import random

lowbound = 0
highbound = 100
randomnumber = random.randint(lowbound,highbound)

print('Hi, please think of a number between 0 and 100')

print('is your number ', randomnumber, '?')
response = input()

while response != 'yes':
    if response == 'higher':
        lowbound = randomnumber + 1
        randomnumber = random.randint(lowbound,highbound)
        print('is it ', randomnumber, '?')
        response = input()
        
    elif response == 'lower':
        highbound = randomnumber - 1
        randomnumber = random.randint(lowbound, highbound)
        print('is it ',randomnumber, '?')
        response = input()
        
    if response == 'yes':
        print('Im smarter than you bitch')
        break