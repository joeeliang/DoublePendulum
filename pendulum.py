import numpy as np 
from numpy.linalg import inv
from math import cos, sin, pi

class Pendulum:
    def __init__(self, a1, a2, m1=1, m2=1, l1=1.0, l2=1.0):
        self.m1 = m1
        self.m2 = m2
        self.l1 = l1
        self.l2 = l2
        self.g = 9.81
        self.state = np.array([0, 0, a1, a2])

    def G(self, y, t): 
        a1d, a2d = y[0], y[1]
        a1, a2 = y[2], y[3]

        m11, m12 = (self.m1+self.m2)*self.l1, self.m2*self.l2*cos(a1-a2)
        m21, m22 = self.l1*cos(a1-a2), self.l2
        m = np.array([[m11, m12],[m21, m22]])

        f1 = -self.m2*self.l2*a2d*a2d*sin(a1-a2) - (self.m1+self.m2)*self.g*sin(a1)
        f2 = self.l1*a1d*a1d*sin(a1-a2) - self.g*sin(a2)
        f = np.array([f1, f2])
        accel = inv(m).dot(f)

        return np.array([accel[0], accel[1], a1d, a2d])

    def RK4_step(self, y, t, dt):
        k1 = self.G(y,t)
        k2 = self.G(y+0.5*k1*dt, t+0.5*dt)
        k3 = self.G(y+0.5*k2*dt, t+0.5*dt)
        k4 = self.G(y+k3*dt, t+dt)

        return dt * (k1 + 2*k2 + 2*k3 + k4)/6
    
    def position(self):
        x1 = sin(self.state[2])
        y1 = cos(self.state[2])
        x2 = x1 +  sin(self.state[3])
        y2 = y1 + cos(self.state[2])
        return (x1, y1), (x2, y2)  
    
    def update(self, t, dt):
        self.state += self.RK4_step(self.state, t, dt)
