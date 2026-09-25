# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

import numpy as np
import matplotlib.pyplot as plt
import R3_phase_space as ps

from scipy import integrate
from pathlib import Path


def simple_pendulum(t, y):
    """
    Define the two derivatives
    note that dydt is now an array that holds both of the derivatives
    :param t: an array of times (floats) - not used in this template
    :param y: a tuple containing the values x and v
    :return: the derivative of x and v
    """
    x, v = y  # extracts the x and v values from the tuple
    dydt = np.array([v, -x])  # generates an array with the rates of change: dxdt = v, dvdt = -x
    return dydt  # returns the array


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
    t0 = 0  # initial time

    # define the final time and the number of time steps
    tf = 10*np.pi  # final time
    nlist = [200, 500, 1001]  # Number of points at which output will be evaluated
    # Note: this does not mean the integrator will take only n steps
    # Scipy will take more steps if required to control the error in the solution
    
    # Iterate through different steps:
    for n in nlist:
        # creates an array of the time steps
        t = np.linspace(t0, tf, n)  # Points at which output will be evaluated
        
        # Exact Solution
        y = np.sin(t)
    
        # Calls the method integrate.solve_ivp()
        result = integrate.solve_ivp(fun=simple_pendulum,  # The function defining the derivative
                                     t_span=(t0, tf),  # Initial and final times
                                     y0=y0,  # Initial state
                                     method="RK45",  # Integration method
                                     t_eval=t)  # Time points for result to be defined at
    
        # Read the solution and time from the result array returned by Scipy
        x, v = result.y
        t = result.t
    
        
        # plot position ad velocity as a function of time.
        plt.plot(t, x, label=f"$x(t), n={n}$")
        plt.plot(t, v, label=f"$v(t), n={n}$")
    
        plt.legend(loc=1)
        
        
        # Name Axis & Graph
        plt.title('Harmonic Oscillation as a function of time')
        plt.ylabel('Position (m), Velocity (m/s')
        plt.xlabel('Time (s)')
    plt.plot(t, y, label="Sin(t)")
    ps.phase_space(v, x) # Plots the phase spac using R3_phase_space

    # creates the path to store the data. Note that the data is not stored in the code repo directory.
    filename = generate_path(basename='Harmonic-init', extension='png')  # uses the function defined above

    # saves and displays the file
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    plt.show()


if __name__ == '__main__':
    main()
