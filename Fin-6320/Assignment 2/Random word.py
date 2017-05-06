# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:56:35 2017

@author: Joshua
"""

import random

words = ['poop', 'arbitrage','peanut butter','graduate','ridiculous']

for i in range (len(words)):
    random_index = random.randrange(len(words))
    print(words[random_index])
    del words[random_index]