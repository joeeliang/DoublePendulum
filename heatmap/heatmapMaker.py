import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.colors import SymLogNorm
import animation

def read_lyapunov_heatmap_from_csv(input_file):
    # Read the CSV file
    data = pd.read_csv(input_file)
    
    # Extract θ1 and θ2 ranges
    theta1_range = data.iloc[:, 0].values
    theta2_range = data.columns[1:].astype(float).values
    print(theta1_range)
    print(theta2_range)
    # Extract the Lyapunov heatmap (excluding the first column for θ1 and the header row for θ2)
    lyapunov_heatmap = data.iloc[:, 1:].values
    
    return lyapunov_heatmap, theta1_range, theta2_range

def plot_lyapunov_heatmap(lyapunov_heatmap, theta1_range, theta2_range):
    vmin = np.min(lyapunov_heatmap)
    vmax = np.max(lyapunov_heatmap)
    extent = [theta2_range.min(), theta2_range.max(), theta1_range.min(), theta1_range.max()]
    plt.imshow(lyapunov_heatmap, origin='lower', cmap='hot', extent=extent, aspect='auto')
    plt.colorbar(label='Lyapunov Exponent')
    plt.xlabel('θ2')
    plt.ylabel('θ1')

    # Function to format the tooltip text
    def format_coord(x, y):
        row = np.searchsorted(theta2_range, x - (theta2_range[0]-theta2_range[1])/2)
        col = np.searchsorted(theta1_range, y - (theta1_range[0]-theta1_range[1])/2)
        if 0 <= col < len(theta2_range) and 0 <= row < len(theta1_range):
            return f't1={theta1_range[row]}, t2={theta2_range[col]}, exponent={lyapunov_heatmap[row, col]:.2f}'
        else:
            return ''

    plt.gca().format_coord = format_coord

    # Event handler for key press
    def on_key(event):
        if event.key == 'u':
            try:
                x, y = event.xdata, event.ydata
                col = np.searchsorted(theta2_range, x)
                row = np.searchsorted(theta1_range, y)
                if 0 <= col < len(theta2_range) and 0 <= row < len(theta1_range):
                    print(f'Pressed u at (t1, t2): {theta1_range[row]}, {theta2_range[col]}')
                    # Debug print before calling the animation
                    print("Calling animation.animate with:", theta1_range[row], theta2_range[col])
                    animation.animate(theta1_range[row], theta2_range[col])
            except Exception as e:
                print(f"Error during animation: {e}")
                
    plt.gcf().canvas.mpl_connect('key_press_event', on_key)
    plt.show()

# Read Lyapunov heatmap from CSV file
input_file = "/Users/joeliang/Joe/Coding/DoublePendulum/heatmapData/lyapunov_exponents.csv"  # Update this path to your actual CSV file path
lyapunov_heatmap, theta1_range, theta2_range = read_lyapunov_heatmap_from_csv(input_file)

# Plot the Lyapunov heatmap
plot_lyapunov_heatmap(lyapunov_heatmap, theta1_range, theta2_range)
