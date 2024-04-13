import numpy as np
def zeroCreator(rows, cols, name):
    # Create the table filled with zeros
    table = [[0 for _ in range(cols)] for _ in range(rows)]
    # Write the table to a file
    with open(f"{name}.csv", "w") as file:
        for row in table:
            file.write(','.join(map(str, row)) + '\n')

def replace(start, end, replacement_data,file):
    # Step 1: Load the CSV data into a numpy array
    data = np.loadtxt(f'heatmap/{file}.csv', delimiter=',')

    # Step 2: Replace the specified section within the data array
    # Note that Python uses 0-based indexing. Adjust indices accordingly if your start coordinates are 1-based.
    # Also, slice end indices are exclusive, so we add 1 to include the end row and column.
    data[start[0]-1:end[0], start[1]-1:end[1]] = replacement_data

    # Step 3: Save the modified array back to a CSV file
    np.savetxt(f'heatmap/{file}.csv', data, delimiter=',',fmt='%s')
