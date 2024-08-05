import numpy as np
from .pendulum import Pendulum
import time

def grabPerturbed(di, df, perturbed_state, initial_state):
    perturbed = initial_state + (di * (perturbed_state - initial_state)) / df
    return perturbed

def tempLyapunov(di, df):
    return np.log(abs(df/di))

def lyapunovCalculator(theta1, theta2):
    delta_t = 0.01
    totalTime = 25
    time = np.arange(0, totalTime, delta_t)
    divisor = 20

    lyapunovExponents = []
    initial = Pendulum(theta1, theta2)
    perturbed = Pendulum(theta1 + 0.001, theta2)
    distanceInitial = np.linalg.norm(perturbed.state-initial.state)
    
    counter = 0
    for t in time:
        counter = counter + 1
        initial.update(t, delta_t)
        perturbed.update(t, delta_t)

        if counter % divisor == 0:
            distanceFinal = np.linalg.norm(perturbed.state-initial.state)
            lyapunovExponents.append(tempLyapunov(distanceInitial, distanceFinal))
            perturbed.state = grabPerturbed(distanceInitial, distanceFinal, perturbed.state, initial.state)
            distanceInitial = np.linalg.norm(perturbed.state-initial.state)
    
    return np.sum(lyapunovExponents) * (1/totalTime)
