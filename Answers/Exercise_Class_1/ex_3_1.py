#from IPython.display import display, Latex
import numpy as np
import matplotlib.pyplot as plt
def v(t,v_0,a):
    return(v_0+a*t)
def z(t,z_0,a,v_array):
    return(z_0+v_array*t)


z_0=int(input('Please input the inital height'))
v_0=int(input('Please input the inital velocity'))
m=int(input('Please input the mass'))
g=int(input('Please input the gravitational constant you wish to use'))

n=10
t=np.arange(n,step=0.05)
a=(-int(g))
f=m*a

a_array=np.repeat(a,len(t))
print(a_array)
v_array=v(t,v_0,a)
z_array=z(t,z_0,a,v_array)


plt.plot(t,z_array, label='Height, $z(t)$', color='cornflowerblue')
plt.plot(t,v_array,label='Velocity, $ \dot{z}$', color='firebrick')
plt.plot(t,a_array, label='Acceleration, $ \ddot{z}$', color='mediumseagreen')
plt.xlabel('$t$')
plt.legend()
plt.grid(True)
plt.title('Trajectory of a Point Mass')
plt.show()



