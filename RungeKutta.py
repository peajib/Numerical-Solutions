# Solving a differential equation using Runge-Kutta method.
# For a given differential equation: dy/dt = f(t,y) ; y(t_0)=y_0
# Approximate solution can be obtained by starting at the intial value
# and 'propagating' to a nearby point similar to Euler's method. However, 
# in Runge-Kutta we don't use the simple slope, we use an average slope 
# from 4 separate points (k1,k2,k3,k4)

import numpy as np
import matplotlib.pyplot as plt

f = lambda t,y : 1-t+4*y    # differential equation

t_max = 2      # maximum time 
h = 0.2        # step size

# A tricky part is the time array. This needs to be setup using the desired
# step size h. The line below sets up a time array with bounds at 0 and t_max, 
# with step sizes given by h. The 'int(t_max/h)+1' line calculates the number
# of evenly spaced points the array has to have to yield the desired step size h.
t = np.linspace(0,t_max,int(t_max/h)+1)   

# Declare the solution y as all zeros, then fill in the values in the loop.
y = np.zeros(len(t))

# Set initial value
y[0] = 1


# Now the Runge-Kutta algorithm:
for i in range(0,len(t)-1):
    # calculate the 4 slopes
    k1 = f(t[i],y[i])
    k2 = f(t[i]+0.5*h,y[i]+0.5*h*k1)
    k3 = f(t[i]+0.5*h,y[i]+0.5*h*k2)
    k4 = f(t[i]+h,y[i]+h*k3)

    # calculate the i+1 solution using the k's and the previous solution at i.
    y[i+1] = y[i] + h*((k1+2*k2+2*k3+k4)/6)


# Plot the result
plt.plot(t,y)
plt.xlim([0,2])


