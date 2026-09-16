# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:19:32 2026

@author: Aaron Dignam
"""

import numpy as np

# Variables
h = 0.05 # Step
tmax = 2.6 # Maximum time


# Initial Conditions
t = 0 # Start time
x = -0.75 # Initial quantity
xo = x
#x = [3,1,0,-0.5,0.75] # Initial quantity list

# Arrays
xval = np.array([x]) # Array of x values
time = np.array([t]) # Time array

# Function for calculation
def f(x,t):
    output = t - (x**2)
    return output

# Loop which calculates new values for calculated
while True:
    # Calculating each step
    x = x + h * f(x,t)
    # Calculate next time
    t = t + h
    #print(N, t)
    # Append N and t to arrays
    xval = np.append(xval, [x]) # Append to xval array
    time = np.append(time, [t]) # Append to time array
    print(f"x-value at {t}s is {x}")
    # Loop ending condition
    if abs(t - tmax) < h/2:
        break

print(f"x-value array: {xval} // Size: {xval.size}")
print()
print(f"Time-value array: {time} // Size: {time.size}")

# Plotting the results of the function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(time, xval, label=f"x_o = {xo}")
ax.set(xlabel = 'Time (s)', ylabel = 'X value')
ax.grid()
ax.legend()
plt.show()

