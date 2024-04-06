import numpy as np 
from numpy.linalg import inv
from matplotlib import pyplot as plt
from matplotlib.colors import SymLogNorm
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
        if x >= theta2_range.min() and x <= theta2_range.max() and y >= theta1_range.min() and y <= theta1_range.max():
            x_index = int(x / np.pi *1033)
            y_index = int(y / np.pi *1033)
            return f't1={theta1_range[y_index]:.2f}, t2={theta2_range[x_index]:.2f}, x={x_index}, y={y_index}'
        else:
            return ''

    plt.gca().format_coord = format_coord

    # Event handler for key press
    def on_key(event):
        if event.key == 'u':
            x, y = event.xdata, event.ydata
            if x is not None and y is not None:
                if x >= theta2_range.min() and x <= theta2_range.max() and y >= theta1_range.min() and y <= theta1_range.max():
                    x_index = int(x / np.pi *1033)
                    y_index = int(y / np.pi *1033)
                    print(f'Pressed h at (t1, t2): {theta1_range[y_index]}, {theta2_range[x_index]}')

    plt.gcf().canvas.mpl_connect('key_press_event', on_key)

    plt.show()


def read_lyapunov_heatmap_from_csv(input_file):
    lyapunov_heatmap = np.loadtxt(input_file, delimiter=',')
    return lyapunov_heatmap

# Read Lyapunov heatmap from CSV file
input_file = "heatmap/1260Square.csv"
lyapunov_heatmap = read_lyapunov_heatmap_from_csv(input_file)

Hdimensions = 1033
Wdimensions = 1033

theta1_range = np.linspace(0, np.pi, Hdimensions)  # Adjust the number of points as needed
theta2_range = np.linspace(0, np.pi, Wdimensions)
# Plot the Lyapunov heatmap
plot_lyapunov_heatmap(lyapunov_heatmap, theta1_range, theta2_range)
