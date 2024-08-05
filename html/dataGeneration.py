import csv
import random

def generate_heatmap_csv(filename, groups, variables):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["group", "variable", "value"])

        for group in groups:
            for variable in variables:
                value = random.randint(0, 100)
                writer.writerow([group, variable, value])

# Define groups and variables
groups = [f'a{i}' for i in range(1, 1000)]  # Add more groups as needed
variables = [f'v{i}' for i in range(1, 1000)]  # Add more variables as needed

# Generate the CSV file
generate_heatmap_csv('html/data.csv', groups, variables)
