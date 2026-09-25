# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:21:42 2026

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import R3_phase_space as R3
from R6_excerpt import driven_pendulum


from scipy import integrate
from pathlib import Path


def double_loop(y0, t0, tf, n, A):
    """
    The code in this function needs to be extracted and incorporated into existing code
    """
    # define an iterable (e.g. a list, numpy array) of damping coefficients
    # (put in your 5 different values of b here where 0 < b < 1):
    damping_coefficients = [0.05, 0.1, 0.2, 0.5, 1]

    # define the driving frequencies over which your inner loop will iterate
    # I recommend using a numpy linspace.
    # Consider: why am I defining this outside the loop?  Is that OK
    driving_frequencies = np.linspace(0 , 2, num=500)

    # define your resonant frequency
    omega = 1.

    # creates an array of the time steps
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

    # First (outer) loop through Damping coefficients
    for b in damping_coefficients:
        amplitudes = [] # Clear list to store amplitudes needs to be done for each b

        # Second (inner) loop through driving freq. define earlier!
        for omegad in driving_frequencies:
            # Define the anonymous function, including the changing omegad
            lfun = lambda t, y, : driven_pendulum(t, y, b, omega, A, omegad)

            # Call the solver for this definition of lfun
            result = integrate.solve_ivp(fun=lfun,
                                         t_span=(0, tf),
                                         y0=y0,
                                         method="RK45",
                                         t_eval=t)
            # Store result of this run in variables t, x, v
            t = result.t
            v, x = result.y
            amplitudes.append((max(x)-min(x))/2)  # Find peak to peak amplitude
            # End of inner loop, continue with next omegad

        # Out of the inner loop
        # Save plot of amplitudes
        plt.plot(driving_frequencies, amplitudes, label=f"b={b}")
    plt.title(f'Resonance Curve')
    plt.ylabel('Amplitide (m)')
    plt.xlabel('Driving Frequency (Hz)')
    plt.grid()
    plt.legend()
    # End of outer loop
    # Out of outer loop
    plt.savefig('Oscillator-freq-multi.pdf', bbox_inches='tight')
    

def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='txt'):
    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    # uses the method Path.home() to find the home directory in any OS
    output_folder = home_folder + subfolder  # appends a subdirectory within it.
    filename = basename + '.' + extension  # defines the filename the output is to be saved in
    output_path = output_folder + filename  # creates the output path
    return output_path

def main():
    """
    A main function used to ensure that the code is portable. By using if __name__ == '__main__': main() we can ensure
    that python will not execute the code when functions or methods in this module are imported, only if we run it
    directly. At this point, this structure isn't needed, but it's a good habit to get into.
    :return:
    """

    # define the initial parameters
    x0 = 0  # initial position
    v0 = 1  # initial velocity
    y0 = (x0, v0)  # initial state
    t0 = 0  # initial time#
    A = 20 # Amplitide

    # define the final time and the number of time steps
    tf = 30*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps
    # Scipy will take more steps if required to control the error in the solution
    
    
    
    double_loop(y0, t0, tf, n, A)
    
if __name__ == '__main__':
    main()