from lyapunov import lyapunovCalculator
import numpy as np 
from numpy.linalg import inv
from math import cos, sin, pi
import time as ti
from multiprocessing import Pool

def cl(args,):
    i, j = args

    return lyapunovCalculator(i, j)

def lyapunovFromRange(theta1_range, theta2_range):
    result_array = []
    if __name__ == "__main__":
        with Pool(processes=4) as pool:
            results = pool.imap(cl, [(i, j) for i in theta1_range for j in theta2_range])
            for result in results:
                print(result)
                result_array.append(result)
        result_array = np.array(result_array).reshape(len(theta1_range), len(theta2_range))
    return result_array
            
theta1_range = np.linspace(0, pi, 5)
theta2_range = np.linspace(0, pi, 5)

print(lyapunovFromRange(theta1_range,theta2_range))
