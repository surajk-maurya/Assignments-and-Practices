# -*- coding: utf-8 -*-
"""
Spyder Editor

This assignment was to find total sum of ints in a text file.
"""
import re
x = open('actual-data.txt')
intlist = []
for i in x:
    y = []
    y = re.findall('[0-9]+',i)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    for n in y: 
        intlist.append(n)
intlist = list(map(int, intlist))
print(sum(intlist))