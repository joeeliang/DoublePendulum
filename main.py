from calc import *
import numpy as np
from util.heatmap import replace

def main(start, end):
    set_theta1 = [x for x in np.linspace(0, 2*np.pi, 1260)]
    set_theta2 = set_theta1
    
    theta1 = set_theta1[start[0]-1: end[0]]
    theta2 = set_theta2[start[1]-1: end[1]]

    final = multithread.lyapunovFromRange(theta1, theta2)

    replace(start,end,final,'1260Square')

def process_in_chunks(row_start, row_end, chunk_size):
    for start_row in range(row_start, row_end + 1, chunk_size):
        end_row = min(start_row + chunk_size - 1, row_end)
        start = [start_row, 1]
        end = [end_row, 1260]
        main(start, end)

if __name__ == "__main__":
    start = [1,1]
    end = [1,1260]
    print('"y" for yes and "n" for no \n')
    if input("Calculating Row By Row? ") == "y":
        start[0] = int(input("Input row start: "))
        end[0] = int(input("Input row end: "))
        process_in_chunks(start[0], end[0], 10)
    else:
        print("Specify your own coordinates, in the form:'x y'")
        start = list(map(int, input("Start Row and Col: ").split()))
        end = list(map(int, input("End Row and Col: ").split()))
        main(start, end)