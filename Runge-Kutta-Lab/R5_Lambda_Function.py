# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:21:42 2026

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import R4_function as R4
import R3_phase_space as R3

from scipy import integrate
from pathlib import Path

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
    blist = [0.1, 2, 5] # damping coefficient for oscillator
    omega0 = 5

    # define the final time and the number of time steps
    tf = 10*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps
    # Scipy will take more steps if required to control the error in the solution
    
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated
    
    # Exact Solution
    #y = np.sin(t)
    for b in blist:
        print(b)
        fig, (ax1,ax2) = plt.subplots(1,2, figsize=(12,5))
    
        # Calls the method integrate.solve_ivp()
        # define a lambda function in a proper program that takes these arguments
        lfun = lambda t, y, : R4.damped_pendulum(t, y, b, omega0)
        
        
        # The part of the code running the solver then needs to read:
        result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                                     t_span=(t0, tf),  # Initial and final times
                                     y0=y0,  # Initial state
                                     method="RK45",  # Integration method
                                     t_eval=t)  # Time points for result to be defined at

    
        # Read the solution and time from the result array returned by Scipy
        x, v = result.y
        t = result.t
        
        phase_space = R3.phase_space(v, x) # Runs phase space function to be plotted.
        
        # plot position ad velocity as a function of time.
        ax1.plot(t, x, label=f"x(t), b={b}")
        ax1.plot(t, v, label=f"v(t), b={b}")
        ax2.plot(phase_space[0], phase_space[1], 'k', label='Phase Space')
    
        plt.legend(loc=1)
        
        
        # Titles
        if b == 0.1:
            ax1.set_title(f"Underdamped Harmonic Oscillation as a function of time, b={b}")
        elif b == 2:
            ax1.set_title(f"Critically Damped Harmonic Oscillation as a function of time, b={b}")
        elif b == 5:
            ax1.set_title(f"Overdamped Harmonic Oscillation as a function of time, b={b}")
        else:
            ax1.set_title(f"Damped Harmonic Oscillation as a function of time, b={b}")



        ax2.set_title(f'Phase Space Diagram, b={b}')
        # Name Axis & Graph
        ax1.set_ylabel('Position (m), Velocity (m/s')
        ax1.set_xlabel('Time (s)')
        ax1.grid()
        ax1.legend()
        

        ax2.set_ylabel('Velocity (m/s)')
        ax2.set_xlabel('Distance (m)')
        ax2.legend()
        ax2.grid()
        plt.show()
        
        # creates the path to store the data. Note that the data is not stored in the code repo directory.
        filename = generate_path(basename=f'Damped-Harmonic-init-b-{b}', extension='png')  # uses the function defined above

        # saves and displays the file
        fig.savefig(filename, bbox_inches='tight')
        print("Output file saved to {}.".format(filename))
        plt.show()

    
       
    
if __name__ == '__main__':
    main()