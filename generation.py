import calc
from calc import multithread

theta1 = [x in int(x) for x in range(0, 3.14, 10)]
theta2 = theta1 

multithread.lyapunovFromRange(theta1,theta2)