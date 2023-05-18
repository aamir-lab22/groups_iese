# -*- coding: utf-8 -*-
"""
Created on Thu May 18 09:52:54 2023

@author: Aamir Alaud Din
"""

import random as random

groups = []
lg = 0

while lg < 6:
    n = random.randint(1, 6)
    if n not in groups:
        groups.append(n)
        lg = len(groups)
        
print(groups)