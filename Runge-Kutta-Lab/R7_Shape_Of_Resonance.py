# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:21:42 2026

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import R3_phase_space as R3

from scipy import integrate
from pathlib import Path

def placeholder_amplitudes(tf, n, omega0, b, y0, A):
    """
    The code in this function needs to be extracted and incorporated into existing code
    """
    amplitudes = []  # Create empty list to store amplitudes
    t = np.linspace(0.8*tf, tf, n)  # Change time array to include only later points

    driving_freq = np.linspace(0, 2*omega0, 100)  # Create range of omega_d 20%-200% of omega_0

    # Loop through driving frequencies
    for omega in driving_freq:
        # Define the anonymous function, including the changing omegad
        lfun = lambda t, y, : driven_pendulum(t, y, b, omega0, A, omega)
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
        # End of loop, continue with next omegad
    # Out of the loop
    # Plot the amplitudes
    plt.plot(driving_freq, amplitudes)  
    plt.title(f'Resonance Curve for A={A}, b={b}, w0={omega0}')
    plt.ylabel('Amplitide (m)')
    plt.xlabel('Frequency (Hz)')
    plt.grid()
    #plt.legend()
    

def driven_pendulum(t, y, b, omega0, A, omega):
    # 'omega' represents the driving frequency
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x+A*np.sin(omega*t)
    dydt = np.array([dxdt, dvdt])
    return dydt

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
    blist = [2]#, 2, 5] # damping coefficient for oscillator
    omega0 = 10
    omega = 0.9 # Driving Frequency
    A = 5 # Amplitide

    # define the final time and the number of time steps
    tf = 30*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps
    # Scipy will take more steps if required to control the error in the solution
    
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated
    
    # Exact Solution
    #y = np.sin(t)
    for b in blist:
        print(b)
        #fig, (ax1,ax2) = plt.subplots(1,2, figsize=(12,5))
    
        # Calls the method integrate.solve_ivp()
        # define a lambda function in a proper program that takes these arguments
        lfun = lambda t, y, : driven_pendulum(t, y, b, omega0, A, omega)
        
        
        # The part of the code running the solver then needs to read:
        result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                                     t_span=(t0, tf),  # Initial and final times
                                     y0=y0,  # Initial state
                                     method="RK45",  # Integration method
                                     t_eval=t)  # Time points for result to be defined at

    
        # Read the solution and time from the result array returned by Scipy
        x, v = result.y
        t = result.t
        
        # phase_space = R3.phase_space(v, x) # Runs phase space function to be plotted.
        
        # # plot position ad velocity as a function of time.
        # ax1.plot(t, x, label=f"x(t), b={b}")
        # ax1.plot(t, v, label=f"v(t), b={b}")
        # ax2.plot(phase_space[0], phase_space[1], 'k', label='Phase Space')
    
        # plt.legend(loc=1)
        
        
        # # Titles
        # if b == 0.1:
        #     ax1.set_title(f"Underdamped Harmonic Oscillation as a function of time, b={b}")
        # elif b == 2:
        #     ax1.set_title(f"Critically Damped Harmonic Oscillation as a function of time, b={b}")
        # elif b == 5:
        #     ax1.set_title(f"Overdamped Harmonic Oscillation as a function of time, b={b}")
        # else:
        #     ax1.set_title(f"Damped Harmonic Oscillation as a function of time, b={b}")



        # ax2.set_title(f'Phase Space Diagram, b={b}')
        # # Name Axis & Graph
        # ax1.set_ylabel('Position (m), Velocity (m/s')
        # ax1.set_xlabel('Time (s)')
        # ax1.grid()
        # ax1.legend()
        

        # ax2.set_ylabel('Velocity (m/s)')
        # ax2.set_xlabel('Distance (m)')
        # ax2.legend()
        # ax2.grid()
        # plt.show()
    
        
        # creates the path to store the data. Note that the data is not stored in the code repo directory.
        #filename = generate_path(basename=f'Damped-Harmonic-init-b-{b}', extension='png')  # uses the function defined above

        # saves and displays the file
       # fig.savefig(filename, bbox_inches='tight')
        #print("Output file saved to {}.".format(filename))
        plt.show()
    
    # Create a new figure for lambda loop 
    plt.figure()
    print(y0)
    # Loop through list of three driving frequencies (100%, 90%, 50% of omega0)
    for omega in (omega0, 0.9 * omega0, 0.5 * omega0):
        # Define the anonymous function, including the changing omegad
        lfun = lambda t, y,: driven_pendulum(t, y, b, omega0, A,  omega)
        # Call the solver for this definition of lfun
        result = integrate.solve_ivp(fun=lfun,
                                     t_span=(0, tf),
                                     y0=y0,
                                     method="RK45",
                                     t_eval=t)
        # Store result of this run in variables t, x, v
        t = result.t
        x, v = result.y
        # Plot the result x(t) for this run, lable it with omegad as well
    #     plt.plot(t, x, label='$x(t): \omega_d =${}'.format(omega))
    # plt.xlabel('Time (s)')
    # plt.ylabel('Displacement (m)')
    # plt.legend()
    # plt.grid()
    # plt.title('Driven Oscillator Response for Varying Driving Frequency')  # you're missing a title here too
    # plt.show()
    # End of loop, continue with next omegad
    
    placeholder_amplitudes(tf, n, omega0, b, y0, A)
    
if __name__ == '__main__':
    main()