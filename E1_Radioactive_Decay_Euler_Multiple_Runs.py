# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:19:32 2026

@author: Aaron Dignam
"""

import numpy as np

# Euler form:
    #N(t + dt) = N(t) - N(t)dt/tau

# Variables
dt = [0.01, 0.005, 0.001] # Time step
tmax =  10 # Maximum time
tau = 2.0 # Time constant

# Initial Conditions
t = 0 # Start time
N = 10 # Initial quantity

# Arrays
Nt = np.array([N]) # No. Radiation at a given time array
time = np.array([t]) # Time array

# Function to run multiple calculations
def calculations(time, Nt, dt, tau):
    
    # Loop which calculates new values
    while True:
        # Calculating new N value
        N = Nt[-1] - ((Nt[-1]/tau) * dt)
        # Calculate next time
        t = time[-1] + dt
        # Append N and t to arrays
        Nt = np.append(Nt, [N]) # Append to Radiation No. array
        time = np.append(time, [t]) # Append to time array
        # Loop ending condition
        if abs(t - tmax) < dt/2:
            break

for i in dt:
    calculations(time,Nt,dt,tau)
    

print(f"N-array: {Nt} // No. Elements: {Nt.size}")
print()
print(f"Time-array: {time} // No. Elements: {Nt.size}")
    


#Plotting a graph to represent data
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(time, Nt, label = 'dt = 0.1') # Creates plot of time (x) against decay (Nt)
ax.set(xlabel = 'No. Partciles (Count)', ylabel = 'Time(s)') # Labels the graph
ax.grid() # Creates a grid for data analysis.
ax.legend()

plt.show()


