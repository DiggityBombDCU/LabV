# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:19:32 2026

@author: Aaron Dignam
"""

import numpy as np
import matplotlib.pyplot as plt

# Variables
h = [0.05, 0.005, 0.0005] # List of steps to run through
tmax = 10 * np.pi # enough time for 5 oscillations

# Defining Functions
def dx_func(x,y,t):
    dx = y
    return dx

def dy_func(x, y, t):
    dy = -x
    return dy

# Creates one figure for each run
fig, ax = plt.subplots() # Define graph for euler and actual values
fig2, ax2 = plt.subplots() # Define graph for calculated difference between euler and actual

for i in h:
    # h-value for run
    h_new = i
    # Initial Conditions
    t = 0 # Start time
    x = 0 # Initial x value
    y = 1 # Initial y value (since dx/dt = y) // represnets velocity
    diff = 0 # Initial difference value between actual and calculated
    # Arrays
    xval = np.array([x]) # Array of x values
    yval = np.array([y]) # Array of y values
    sinval = np.array([t])
    time = np.array([t]) # Time array
    diffval = np.array([diff])
    # Loop which calculates new values
    while True:
        
        x_old, y_old = x, y

        xinit = x_old + h_new * dx_func(x_old, y_old, t)
        yinit = y_old - h_new * dy_func(x_old, y_old, t)
        # Actual Sine value
        s = np.sin(t)
        # Calculating x-value
        x = x_old + 0.5 * h_new * (y_old + yinit)
        # Calculating y-value
        y = y_old - 0.5 * h_new * (x_old + xinit)
        # Calculate next time
        t = t + h_new
        # Calculating the difference
        diff = x - s
        # Append values to arrays
        xval = np.append(xval, [x]) # Append to xval array
        yval = np.append(yval, [y]) # Append to yval array
        time = np.append(time, [t]) # Append to time array
        sinval = np.append(sinval, [s]) # Append to true value
        diffval = np.append(diffval, [diff]) # Append to difference in values array
        
        #sleep(2)
        # Loop ending condition
        if abs(t - tmax) < h_new/2:
            #print(f"xval: {xval} // Size: {xval.size}")
            #print()
            #print(f"time: {time} // Size: {time.size}")
            break
        #print(f"Difference array = {diffval} // Size = {diffval.size}")
    ax.plot(time, xval, label=f"Euler values for h = {h_new}") # Plotting euler on the graoh
    ax2.plot(time, diffval, label=f"Difference values for h = {h_new}") # plotting difference values



# print(f"xvalues = {xval} // Size = {xval.size}")
# print(f"yvalues = {yval} // Size = {yval.size}")
# print(f"Time-value array: {time} // Size: {time.size}")


# Plotting the results of the function

#ax.plot(time, yval, label='y-values')
ax.plot(time, sinval, label='Actual Values')
#ax.plot(time, xyval, label='xy-values')

ax.set(xlabel = 'Time (s)', ylabel = 'x')
ax2.set(xlabel='Time (s)', ylabel='Difference Value')
ax.grid()
ax.legend()
ax2.grid()
ax2.legend()
plt.show()

# Plotting just h = 0.0005 to see the difference values

fig3, ax3 = plt.subplots()
ax3.plot(time, diffval, label=f"Focused values for exclusively h = {h_new}")
ax3.plot(xlabel='Time (s)', ylabel='Difference')
ax3.legend()
ax3.grid()
plt.show()