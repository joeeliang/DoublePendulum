import pandas as pd

# Simulating the CSV read with the provided data example

df = pd.read_csv("heatmap/1260Square.csv", header=None)

# Copy the top of the DataFrame
top = df.loc[:629].copy()  # Assuming we want to flip the whole provided DataFrame

# Flip both rows and columns
flipped_top = top.iloc[::-1, ::-1]

# Reset the column names of flipped_top to match those of top
flipped_top.columns = top.columns

# Concatenate original top and flipped_top with reset index
result = pd.concat([top, flipped_top], ignore_index=True)

# Display the result
result.to_csv('heatmap/result.csv', header=False, index=False, sep=',')
