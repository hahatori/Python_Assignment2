#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import csv
import operator
import matplotlib
import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
import tkinter
import re
import collections
import os
from tkinter import *
from tkinter import messagebox


matplotlib.use('TkAgg') # Backend.


# Make the frame of plots and set properties.
fig = plt.figure(figsize=(9.5, 5))
ax = fig.add_axes([0, 0, 1, 1])


# To open death.parishes.txt file.
p = []             # Creat an empty list.
with open("death.parishes.txt") as f1:
    data1 = f1.read().splitlines()   # Read the file by line.
    for row in data1:
        rowlist = []
        for value in row.split(','): # Change data from text into standard data. 
            rowlist.append(float(value))
        p.append(rowlist) # Read the csv into the p list.
#print(p) # Test output.


# Same way to load death.rats.txt file.
r = []  
with open("death.rats.txt") as f2:
    data2 = f2.read().splitlines() 

    for row in data2:
        rowlist = []
        for value in row.split(','):  
            rowlist.append(float(value))
        r.append(rowlist) 
#print(r)


# Display 2x(400m x 400m) raster maps.
plt.subplot(1,3,1)   # p raster map is in the first row, first column.
plt.title("Population Density Plot")
plt.imshow(p)
plt.subplot(1,3,2) #The page has 1 row, 3 columns, r is in the second position.
plt.title("Rats Caught Plot")
plt.imshow(r)

# p_weight = 0.8 x r
p_weight = []
p_weight =np.multiply(np.array(p),0.8) # Lists cannot be multiplied directly.
print(p_weight)

# r_weight = 1.3 x p
r_weight = []
r_weight =np.multiply(np.array(r),1.3)
print(r_weight)

#d = p_weight x r_weight 
d=np.multiply(np.array(p_weight),np.array(r_weight))
print(d)
   
# Show d plot.
plt.subplot(1,3,3)   # d is in the third position. 
plt.title("Deaths Plot")
plt.imshow(d)

# Save text file
np.savetxt('death.deaths.txt',d,fmt='%0.2f')
print("Save successful") # A prompt will appear when d is saved successfully.


# Find the number of average deaths in every pixel.
fh1 = open(r'd.txt',"r")
j=0
allsum1=0
allsum2=0
allsum3=0
allsum4=0
allsum5=0
allsum6=0
allsum7=0
allsum8=0
allsum9=0
allsum10=0
allsum11=0
allsum12=0
allsum13=0
allsum14=0
allsum15=0
allsum16=0

sum1=0
sum2=0
sum3=0
sum4=0


for i in range(0,400):
    data1 = fh1.readline()
    j=j+1
    line1=data1.split(",")
 #   line1=list(map(int,line1))
    line1=list(map(float,line1))   
    
    sum1=sum(line1[0:100]) 
    sum2=sum(line1[100:200])
    sum3=sum(line1[200:300])
    sum4=sum(line1[300:400])

    if j>=31:
      allsum13=allsum13+sum1;
      allsum14=allsum14+sum2;
      allsum15=allsum15+sum3;
      allsum16=allsum16+sum4; 
    elif j>=21:
      allsum9=allsum9+sum1;
      allsum10=allsum10+sum2;
      allsum11=allsum11+sum3;
      allsum12=allsum12+sum4;
    elif j>=11:
      allsum5=allsum5+sum1;
      allsum6=allsum6+sum2;
      allsum7=allsum7+sum3;
      allsum8=allsum8+sum4;
    else:
      allsum1=allsum1+sum1;
      allsum2=allsum2+sum2;
      allsum3=allsum3+sum3;
      allsum4=allsum4+sum4
 
    sum1=0
    sum2=0
    sum3=0
    sum4=0

#print(allsum1,allsum2,allsum3,allsum4,allsum5,allsum6,allsum7,allsum8,allsum9,allsum10,allsum11,allsum12,allsum13,allsum14,allsum15,allsum16)

# Calculate the average deaths per week in 100m x 100m square.
allsum1=allsum1/10000
allsum2=allsum2/10000
allsum3=allsum3/10000
allsum4=allsum4/10000
allsum5=allsum5/10000
allsum6=allsum6/10000
allsum7=allsum7/10000
allsum8=allsum8/10000
allsum9=allsum9/10000
allsum10=allsum10/10000
allsum11=allsum11/10000
allsum12=allsum12/10000
allsum13=allsum13/10000
allsum14=allsum14/10000
allsum15=allsum15/10000
allsum16=allsum16/10000


# Calculate the total deaths per week in 400m x 400m square.
allsum=allsum1+allsum2+allsum3+allsum4+allsum5+allsum6+allsum7+allsum8+allsum9+allsum10+allsum11+allsum12+allsum13+allsum14+allsum15+allsum16
#allsum=allsum/160000
total = ("%d" % allsum)
print(total)

fh1.close()

'''
#i_d=[]
#count_d=[]
with open('death.deaths.txt','r') as f:
    number = f.read()
    number = number.replace('    ',',')
    number = number.split()
    print(number)
    setnum=set(number)
    for i in setnum:
        count=number.count(i)
        print(i, 'occurs', count)
       #i_d.append(i)
       #count_d.append(count)        
#print(i_d) 
#print(count_d)
       
       
# Same as steps above. 
# Steps: 1. Number of count_d.
t = sum(count_d)
print(t)

# 2. Multiply two lists.
multi = list(map(lambda x,y:x*y, i_d,count_d))
print(multi)

# 3. Add all the elements in the list.
add= list(map(lambda x:x+x, multi))
print(add)

# 4. Calatuate the total deaths.  
total = list(map(lambda x,y:x/y, add, t))  
print(total)
'''  
      
# Users can change weight by themselves.
pop = [[x0 * 1.3 for x0 in y0] for y0 in p]
rat = [[x1 * 0.8 for x1 in y1] for y1 in r]

# Free to input 2 weights.
def update():
    fig.clear()
    global pop
    global rat
    w1 = float(input("Weight of Population Density:"))
    pop = [[x0 * w1 for x0 in y0] for y0 in p]
    w2 = float(input("Weight of Rats Caught:"))
    rat = [[x1 * w2 for x1 in y1] for y1 in r]
    return pop, rat

'''
def multiply(pop, rat):
    #return pop*rat

ww=multiply(pop, rat)
print(ww)   
'''

def output():
    var = e.get()
    # t.insert('end', var)
    t.insert(2.2, var)
    #var = plt.title("Deaths Plot")
    var = plt.imshow(d)
   
def run():
    global ani
    ani = matplotlib.animation.FuncAnimation(fig, update, frames=3, repeat=False) 
    canvas.draw()

# A pop-up window to show the total deaths per week.
def hit_me():
   messagebox.showinfo("Message", "Total deaths per week = %s" % total)


# Creat a window.
root = tkinter.Tk()     # Capital object name. 
root.title("my window") # Name of the window.
#root.geometry("200x100")   


# Creat a "hit me" button.   
b = tkinter.Button(root, text = 'hit me', width = 15, height= 2,
               command = hit_me) #Just click it, it will run hit_me defined above.
b.pack()
b.bind('<Button-1>',hit_me) # Bind button.

# The input a number will show it after click on "insert_end" button.
e = tkinter.Entry(root)
e.pack()

# Set "insert number" button to execute 'update' command..
b1 = tkinter.Button(root,text="input",command=update)
b1.pack()

# Set "insert end" button to execute 'insert_end' command.
b2 = tkinter.Button(root,text="output",command=output)
b2.pack()

# Execute ‘run’ command.
b3 = tkinter.Button(root,text="change weight",command=run)
b3.pack()

t = tkinter.Text(root)
t.pack()


canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.pack(side = tkinter.TOP, fill = tkinter.BOTH, expand=1)

# Set menu of window.
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label = "Model", menu = model_menu)
#model_menu.add_command(label = "Run model", command = run)

# mainloop is a large while loop.
root.mainloop() #The window is constantly refreshing.
 
   

    
  
    
    
    
    
    

