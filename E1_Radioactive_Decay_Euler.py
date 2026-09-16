# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:19:32 2026

@author: Aaron Dignam
"""

import numpy as np

# Euler form:
    #N(t + dt) = N(t) - N(t)dt/tau

# Variables
dt = 0.1 # Time step
tmax =  10 # Maximum time
tau = 2.0 # Time constant

# Initial Conditions
t = 0 # Start time
ta = 0 # Start time for actual time
No = 10 # Initial quantity
NtAcalc = 10
# Arrays
Nt = np.array([No]) # No. Radiation at a given time array
time = np.array([t]) # Time array
NtA = np.array([10]) # Actual no. particles
timea = np.array([0]) # Actual time

# Loop which calculates new values for calculated
while True:
    # Calculating new N value
    N = Nt[-1] - ((Nt[-1]/tau) * dt)
    # Calculate next time
    t = t + dt
    #print(N, t)
    # Append N and t to arrays
    Nt = np.append(Nt, [N]) # Append to Radiation No. array
    time = np.append(time, [t]) # Append to time array
    # Loop ending condition
    if abs(t - tmax) < dt/2:
        break

print(f"N-array: {NtA} // No. Elements: {NtA.size}")
print()
print(f"Time-array: {timea} // No. Elements: {timea.size}")

# Loop which shows exact values of N(t)

while True:
    # Next time
    ta = ta + dt
    # Get actual N values
    Na = No * np.exp(-ta/tau)
    # Append N and t
    NtA = np.append(NtA, [Na]) # Append actual no. particles
    timea = np.append(timea, [ta]) # Append actual t
    #print(f"{NtA}, {timea}")
    # Loop breaker
    if abs(ta - tmax) < dt/2:
        break

# print(f"N-array(actual): {NtA} // No. Elements: {NtA.size}")
# print()
# print(f"Time-array(actual): {timea} // No. Elements: {timea.size}")


#Plotting a graph to represent data
import matplotlib.pyplot as plt

#Calculated graph
fig, ax = plt.subplots()
ax.plot(time, Nt, label = 'Calculated') # Creates plot of time (x) against decay (Nt)
ax.plot(timea, NtA, label = 'Actual') # Actual graph
ax.set(xlabel = 'Time(s)', ylabel = 'No. Particles (Count)') # Labels the graph
ax.grid() # Creates a grid for data analysis.
ax.legend()

plt.show()

# Calculating the difference
difference = NtA - Nt
#print(difference, f"Difference array: {difference.size}")

# Print NtA
# print(f"NtA: {NtA}, No. {NtA.size}")
# print('Differences: ',NtA[2], Nt[2], NtA[2] - Nt[2], difference[2])

# Plotting the difference]
fig2, ax2 = plt.subplots()
ax2.plot(time, difference)
ax2.set(xlabel = 'Time(s)', ylabel = 'Difference')
plt.show()
ax.grid()