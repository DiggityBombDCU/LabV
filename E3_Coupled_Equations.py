# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:19:32 2026

@author: Aaron Dignam
"""

import numpy as np
import matplotlib.pyplot as plt

# Variables
h = 0.05 # Step
tmax = 37.7 # Maximum time


# Initial Conditions
t = 0 # Start time
x = 0.7 # Initial x value
y = 0.7 # Initial y value (since dx/dt = y)


# Arrays
xval = np.array([x]) # Array of x values
yval = np.array([y]) # Array of y values
sinval = np.array([t])
xyval = np.array([t])
time = np.array([t]) # Time array


# Defining Functions
def dx_func(x,y,t):
    dx = y
    return dx

def dy_func(x, y, t):
    dy = -x
    return dy


# Loop which calculates new values
while True:
    # Calculate next time
    t = t + h
    # Actual Sine value
    s = np.sin(t)
    # Calculating x-value
    x = x + dx_func(x,y,t) * h
    print(x)
    # Calculating y-value
    y = y + dy_func(x,y,t) * h
    print(y)
    # Append values to arrays
    xval = np.append(xval, [x]) # Append to xval array
    yval = np.append(yval, [y]) # Append to yval array
    time = np.append(time, [t]) # Append to time array
    sinval = np.append(sinval, s) # Append to true value
    sums = x + y # Adds x and y array together
    xyval = np.append(xyval, sums) # Appends sum of x and y to array
    #sleep(2)
    # Loop ending condition
    if abs(t - tmax) < h/2:
        print(f"xval: {xval} // Size: {xval.size}")
        print()
        print(f"time: {time} // Size: {time.size}")
        break
    

# print(f"xvalues = {xval} // Size = {xval.size}")
# print(f"yvalues = {yval} // Size = {yval.size}")
# print(f"Time-value array: {time} // Size: {time.size}")

# Creates one figure for each run
fig, ax = plt.subplots()
# Plotting the results of the function
ax.plot(time, xval, label='x-values')
ax.plot(time, yval, label='y-values')
ax.plot(time, sinval, label='Sine Values')
#ax.plot(time, xyval, label='xy-values')

ax.set(xlabel = 'Time (s)', ylabel = 'X & Y values')
ax.grid()
ax.legend()
plt.show()


