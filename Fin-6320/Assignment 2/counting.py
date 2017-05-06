# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:48:29 2017

@author: Joshua
"""

x = int(input("Please input number"))
y = int(input("Please input a higher number"))
z = int(input("what number would you like to count by?"))

count = int(x)

while count < y:
    if count < y:
        count+=z
        print(count)
    elif count > y:
        break