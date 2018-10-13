import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# mech. vibration book by rakheja pg# 542

def function(x,t):
    x1 = x[0] 
    dx1 = x[1] 
    x2 = x[2]
    dx2 = x[3]

    xdot = [[],[],[],[]]
    xdot[0] = x[1]
    xdot[1] = np.cos(3*t) - 4*x[1] + 2*x[3] - 5*x[0] + 2*x[2]
    xdot[2] = x[3]
    xdot[3] = np.cos(3*t) + 0.5*x[1] - x[3] + x[0] - 1.5*x[2]

    return (xdot)

time = np.linspace(0,20,500)
sol = odeint(function,[0.2,1.0,0,0],time)

plt.plot(time,sol[:,0])
plt.grid()
plt.show()

