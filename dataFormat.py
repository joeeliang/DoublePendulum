import csv
import unicodedata
from math import pi

reduction = 7
dimension = 1260

with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))

    with open('redoData.csv', 'w', newline='') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(["t1", "t2", "value"])

        for row in range(0, dimension, reduction):
            for col in range(0, dimension, reduction):
                writer.writerow([round(row/1260 * 2 * pi,10), round(col/1260 * 2 * pi,10), round(float(data[row][col]), 3)])
