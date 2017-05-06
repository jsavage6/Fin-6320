# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:59:23 2017

@author: Joshua
"""
import random

count = 0

print("You have decided to open a fortune cookie, your fortune is")

while count < 1:
    fortune = random.randint(1,5)
    
    if fortune == 1:
        print("you will get killed tonight")
        count+=1
    elif fortune == 2:
        print("you will win $1 tomorrow")
        count+=1
    elif fortune == 3:
        print("Tyler will stop giving homework")
        count+=1
    elif fortune == 4:
        print("you will get a job")
        count+=1
    elif fortune == 5:
        print("you will never get a job")
        count+=1
    
    