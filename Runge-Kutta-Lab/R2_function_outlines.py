# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

# This file isn't a complete template, but rather gives an outline of what you need the function to do.
# If you're feeling ambitious, you can keep these functions in a separate file and import them.
# Look up how to do so for yourself, or experiment based on what you see in library imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def differential_rl(t, i, v, r, l):
    """
    Calculates the change in current over time from the formula
    L(dI/dt) = V - RI
    :param v: Float for voltage
    :param r:
    :param l:
    :param i:
    :return:
    """
    dI = (v - r*i)/l # Calculate the differential 
    
    return dI # Return the differential
    # complete the docstring
    # do some maths to calculate the difference
    # return the difference


def exact_solution_rl(t, v, r, l):
    """
    Calculates the change in current over time from the formula
    I = (V/R)(1-exp(-Rt/L))
    :param v: Float for voltage
    :param r:
    :param l:
    :param t:
    :return:
    """
    
    I = (v / r) * (1 - np.exp((-r * t) / l)) # Calculate the exact value at a given time
    
    return I # Return the exact value
    # complete the docstring
    # do some maths to calculate the exact solution at a given time
    # return the difference
    
def main():
    """
    A main function used to ensure that the code is portable. By using if __name__ == '__main__': main() we can ensure
    that python will not execute the code when functions or methods in this module are imported, only if we run it
    directly. At this point, this structure isn't needed, but it's a good habit to get into.
    :return:
    """
    # Initial variables
    v, r, l = 10,50,100
    y0 = np.array([0]) # Initial array for current
    t0 = 0  # initial time
    tf = 40  # final time
    nlist = [101, 205, 350] # Number of points at which output will be evaluated (note 101 points are needed for 100 spaces)
    
    # Initialising Number of steps for RK 
    for i in nlist:
        n = i
        t = np.linspace(t0, tf, n) # create a numpy array of n times linearly spaced between t0 and tf
        
        
        result = integrate.solve_ivp(fun=differential_rl,  # The function defining the derivative
                                     t_span=(t0, tf),  # Initial and final times
                                     y0=y0,  # Initial state
                                     method="RK45",  # Integration method
                                     t_eval=t, # Time points for result to be reported
                                     args=(v,r,l)) 
        # Read the solution and time from the array returned by Scipy
        y = result.y[0]
        t = result.t
        plt.plot(t,y, label=f"Calculated Value for n={n}") # Plot calculated value
        
        # Exact solution
        yexact = exact_solution_rl(t, v, r, l) # Plot exact values
        plt.plot(t, yexact, label=f"Actual Value for n={n}")

        
    # Plotting the data
    plt.title('Exact vs Calculated data')
    plt.ylabel('Current (A)')
    plt.xlabel('Time (s)')
    plt.legend()
    plt.grid()
    plt.show()
        
    # Plot the difference
    # Calculate the difference and graph it
    diff = yexact - y
    plt.plot(diff, label=f"Difference for n={n}")
    plt.title('Calculated difference')
    plt.ylabel('Difference')
    plt.xlabel('Count')
    plt.legend()
    plt.grid()
    plt.plot(diff)
    plt.show()



    # Check the values make sense
    #print(f"yexact = {yexact} // y = {y} // diff = {diff}")
if __name__ == '__main__':
    main()

