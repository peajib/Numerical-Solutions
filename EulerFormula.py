# Solving a differential equation using Euler's method
# For a given differential equation: dy/dt = f(t,y) ; y(t_0)=y_0
# Approximate solution can be obtained by starting at the intial value
# and 'propagating' to a nearby point by fitting a tangent line of the form
# y = mx+b. This works out to give the Euler formula:
# y_n+1 = y_n + h*f_n

#imports:
import numpy as np
import matplotlib.pyplot as plt

# example: dy/dt = 3t with y(0) = 2
t = np.linspace(0,10,1000)
dydt = lambda t:3*t**2

# the analytic solution is: y = (3/2)t^2 + 2
soln_analytic = (1)*t**3 + 2


# the numerical solution is:
soln_num = np.zeros(len(t))
h = t[1]-t[0]
soln_num[0] = 2+(3*0)  # find the first point using the initial values.


for i in range(0,len(t)-1):
    soln_num[i+1] = soln_num[i]+h*dydt(t[i])

plt.plot(t,soln_analytic)
plt.plot(t,soln_num,'--')





    