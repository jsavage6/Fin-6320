# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:27:12 2017

@author: Joshua
"""
    
import random

total_heads = 0
total_tails = 0
count = 0

while count < 10000:
    
    coin = random.randint(1, 2)

    if coin == 1:
        #print("Heads!")
        total_heads += 1
        count += 1


    elif coin == 2:
        #print("Tails!")
        total_tails += 1
        count += 1

print("Okay, you flipped heads", total_heads, "times and tails", total_tails, "times")

