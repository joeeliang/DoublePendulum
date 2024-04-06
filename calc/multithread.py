from .lyapunov import lyapunovCalculator
import numpy as np 
from numpy.linalg import inv
from math import cos, sin, pi
import time as ti
from multiprocessing import Pool
from tqdm import tqdm

def cl(args,):
    i, j = args

    return lyapunovCalculator(i, j)

def lyapunovFromRange(theta1_range, theta2_range):
    result_array = []
    total_iterations = len(theta1_range) * len(theta2_range)
    progress_bar = tqdm(total=total_iterations, desc="Processing")
    with Pool(processes=4) as pool:
        results = pool.imap(cl, [(i, j) for i in theta1_range for j in theta2_range])
        for result in results:
            progress_bar.update(1)
            result_array.append(result)
    progress_bar.close()
    result_array = np.array(result_array).reshape(len(theta1_range), len(theta2_range))
    return result_array
