import mpld3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_lyapunov_heatmap_3d(lyapunov_heatmap, theta1_range, theta2_range, downsample_factor=10):
    theta1, theta2 = np.meshgrid(theta1_range, theta2_range)
    
    # Downsample the data
    theta1 = theta1[::downsample_factor, ::downsample_factor]
    theta2 = theta2[::downsample_factor, ::downsample_factor]
    lyapunov_heatmap = lyapunov_heatmap[::downsample_factor, ::downsample_factor]
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(theta2, theta1, lyapunov_heatmap, cmap='hot')
    fig.colorbar(surf, label='Lyapunov Exponent')
    
    # Set Z-axis limits
    z_min = np.min(lyapunov_heatmap)
    z_max = 3
    ax.set_zlim(z_min, z_max)
    
    ax.set_xlabel('θ2 (radians)')
    ax.set_ylabel('θ1 (radians)')
    ax.set_zlabel('Lyapunov Exponent')
    plt.show()

def read_lyapunov_heatmap_from_csv(input_file):
    lyapunov_heatmap = np.loadtxt(input_file, delimiter=',')
    return lyapunov_heatmap

# Read Lyapunov heatmap from CSV file
input_file = "data.csv"
lyapunov_heatmap = read_lyapunov_heatmap_from_csv(input_file)

Hdimensions = 1260
Wdimensions = Hdimensions

theta1_range = np.linspace(0, 2 * np.pi, Hdimensions)  # Adjust the number of points as needed
theta2_range = np.linspace(0, 2 * np.pi, Wdimensions)

# Plot the Lyapunov heatmap in 3D with downsampling
plot_lyapunov_heatmap_3d(lyapunov_heatmap, theta1_range, theta2_range, downsample_factor=10)
