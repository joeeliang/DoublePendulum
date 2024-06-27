import numpy as np 
from matplotlib import pyplot as plt
import animation
def plot_lyapunov_heatmap(lyapunov_heatmap, theta1_range, theta2_range):
    vmin = np.min(lyapunov_heatmap)
    vmax = np.max(lyapunov_heatmap)
    extent = [theta2_range.min(), theta2_range.max(), theta1_range.min(), theta1_range.max()]
    # plt.figure(figsize=(8, 8))
    plt.imshow(lyapunov_heatmap, origin='lower', cmap='hot', extent=extent, aspect='equal')
    plt.colorbar(label='Lyapunov Exponent')
    plt.xlabel('θ2 (radians)')
    plt.ylabel('θ1 (radians)')

    # Function to format the tooltip text
    def format_coord(x, y):
        if x >= theta2_range.min() and x <= theta2_range.max() and y >= theta1_range.min() and y <= theta1_range.max():
            x_index = int(x / 2/np.pi *1260)
            y_index = int(y / 2/np.pi *1260)
            return f't1={theta1_range[y_index]:.2f}, t2={theta2_range[x_index]:.2f}, x={x_index}, y={y_index}'
        else:
            return ''

    plt.gca().format_coord = format_coord

    # Event handler for key press
    t1 = None
    t2 = None
    def on_key(event):
        global t1, t2
        if event.key == 'u':
            x, y = event.xdata, event.ydata
            if x is not None and y is not None:
                if theta2_range.min() <= x <= theta2_range.max() and theta1_range.min() <= y <= theta1_range.max():
                    x_index = int(x / (2 * np.pi) * 1260)
                    y_index = int(y / (2 * np.pi) * 1260)
                    t1 = theta1_range[y_index]
                    t2 = theta2_range[x_index]
                    print(f'Pressed u at (t1, t2): {theta1_range[y_index]}, {theta2_range[x_index]}')
                    # Debug print before calling the animation
                    print("Calling animation.animate with:", theta1_range[y_index], theta2_range[x_index])
                    animation.animate(theta1_range[y_index], theta2_range[x_index])
        if event.key == 'y':
            try:
                with open("heatmapData/output.txt", "a") as f:
                    f.write(f"{t1}, {t2}\n")
                    print(f"{t1}, {t2}\n")
            except NameError:
                print("t1 and t2 not defined")

    plt.gcf().canvas.mpl_connect('key_press_event', on_key)
    # plt.axis([0.7, 2.2, 1.2, 2.7])
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
