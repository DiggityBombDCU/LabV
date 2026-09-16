# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:19:32 2026

@author: Aaron Dignam
"""

import numpy as np
import matplotlib.pyplot as plt

# Variables
h = 0.05 # Step
tmax =  1 # Maximum time


# Initial Conditions
t = 0 # Start time
x = [3,1,0,-0.5, -0.75] # Initial quantity list




# Function for calculation
def f(x,t):
    output = t - (x**2)
    return output

# Creates one figure for each run
fig, ax = plt.subplots()
# Loop which calculates new values for calculated
for i in x:
    xo = i
    t = 0
    print(i)
    # Arrays
    xval = np.array([int(i)]) # Array of x values
    time = np.array([t]) # Time array
    while True:
        # Calculating each step
        xo = xo + h * f(xo,t)
        # Calculate next time
        t = t + h
        #print(N, t)
        # Append N and t to arrays
        xval = np.append(xval, [xo]) # Append to xval array
        time = np.append(time, [t]) # Append to time array
        print(f"x-value at {t}s is {xo}")
        # Loop ending condition
        if abs(t - tmax) < h/2:
            print(f"xval: {xval} // Size: {xval.size}")
            print()
            print(f"time: {time} // Size: {time.size}")
            break

# print(f"x-value array: {xval} // Size: {xval.size}")
# print()
# print(f"Time-value array: {time} // Size: {time.size}")

# Plotting the results of the function
    ax.plot(time, xval, label=f"x_o = {i}")


ax.set(xlabel = 'Time (s)', ylabel = 'X value')
ax.grid()
ax.legend()
plt.show()


