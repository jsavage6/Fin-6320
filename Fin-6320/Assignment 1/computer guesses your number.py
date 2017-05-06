# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:00:46 2017

@author: Joshua
"""

import random

lowbound = 0
highbound = 100
randomnumber = random.randint(lowbound,highbound)
print('think of a random number, i am going to guess it')

print('is it', randomnumber,"?")
response = input()

while response != "yes":
    if response == "higher":
        lowbound = randomnumber + 1
        randomnumber = random.randint(lowbound,highbound)
        print('is it ',randomnumber, "?")
        response = input()
        
    elif response == "lower":
        highbound = randomnumber - 1
        randomnumber = random.randint(lowbound,highbound)
        print('is it ',randomnumber, "?")
        response = input()
        
    if response == "yes":
        print("nailed it")
        break