import numpy as np
from calc.lyapunov import lyapunovCalculator
import time
set_theta1 = [x for x in np.linspace(0, 2*np.pi, 1260)]

print(set_theta1[155])
print(set_theta1[574])
start = time.time()

print(lyapunovCalculator(1, 1.5))

end = time.time()
print(end-start)