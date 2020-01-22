#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:29:48 2020

@author: toriliang
"""
#import matplotlib.pyplot
import csv
import operator
import matplotlib.pyplot as plt
import numpy as np

p = []             # Creat agents list.
with open("death.parishes.txt") as f1:
    data1 = f1.read().splitlines() 
    for row in data1:
        rowlist = []
        for value in row.split(','): # Change data from in.txt into standard data. 
            rowlist.append(float(value))
            
        p.append(rowlist) # Read the csv into the p list.

print(p)


r = []  
with open("death.rats.txt") as f2:
    data2 = f2.read().splitlines() 

    for row in data2:
        rowlist = []
        for value in row.split(','): # Change data from in.txt into standard data. 
            rowlist.append(float(value))
        r.append(rowlist) # Read the csv into the p list.

print(r)



plt.xlim(0, 99)            # Set the x-axis range from 0 to 99
plt.ylim(0, 99)            # Set the y-axis range from 0 to 99

plt.subplot(2,2,1)
plt.imshow(p)
plt.subplot(2,2,2)
plt.imshow(r)

# p_weight = 0.8 x r
p_weight = []
p_weight =np.multiply(np.array(p),0.8)
print(p_weight)

# r_weight = 1.3 x p
r_weight = []
r_weight =np.multiply(np.array(r),1.3)
print(r_weight)

#d = p_weight x r_weight 
d=np.multiply(np.array(p_weight),np.array(r_weight))
print(d)

# Show d plot
plt.subplot(2,2,3)
plt.imshow(d)

# Save text file

np.savetxt('in.txt',d,fmt='%.2f')

print("Save successful") 






