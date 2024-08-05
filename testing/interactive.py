import numpy as np 
from matplotlib import pyplot as plt
import mpld3
def plot_lyapunov_heatmap(lyapunov_heatmap, theta1_range, theta2_range):
    vmin = np.min(lyapunov_heatmap)
    vmax = np.max(lyapunov_heatmap)
    extent = [theta2_range.min(), theta2_range.max(), theta1_range.min(), theta1_range.max()]
    fig = plt.figure(figsize=(8, 8))
    plt.imshow(lyapunov_heatmap, origin='lower', cmap='hot', extent=extent, aspect='equal')
    plt.colorbar(label='Lyapunov Exponent')
    plt.xlabel('θ2 (radians)')
    plt.ylabel('θ1 (radians)')
    html_str = mpld3.fig_to_html(fig)
    Html_file= open("index.html","w")
    Html_file.write(html_str)
    Html_file.close()
    plt.show() 

def read_lyapunov_heatmap_from_csv(input_file):
    lyapunov_heatmap = np.loadtxt(input_file, delimiter=',')
    return lyapunov_heatmap

# Read Lyapunov heatmap from CSV file
input_file = "data.csv"
lyapunov_heatmap = read_lyapunov_heatmap_from_csv(input_file)

Hdimensions = 1260
Wdimensions = Hdimensions

theta1_range = np.linspace(0, 2 *np.pi, Hdimensions)  # Adjust the number of points as needed
theta2_range = np.linspace(0, 2 *np.pi, Wdimensions)

# Plot the Lyapunov heatmap
plot_lyapunov_heatmap(lyapunov_heatmap, theta1_range, theta2_range)
