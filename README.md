
# Interactive Double Pendulum Periodicity Finder
This is a demonstration of interactively dropping a double pendulum at various points outlined on a heatmap, which shows the degree of chaos exhibited by the specific drop angle.

## Features
- **Lyapunov Exponent Heatmap**: A heatmap that describes the sensitivity to initial conditions of each drop angle.
- **Interactive Double Pendulum Simulation**: Hover over points on the heatmap and see the corresponding animations.


## Installation


1. Clone the repository

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
## Usage


1. Run the main script to start the interactive simulation:
    ```bash
    python main.py
    ```

2. There will be a graph with an interactive heatmap of the Lyapunov exponents at different drop angles. Hover over them to see the exact angles and their corresponding Lyapunov exponents at the bottom right corner.

3. Press "u" to animate the corresponding double pendulum.

## Files

- `main.py`: The main script to run the interactive simulation.
- `3d.py: A three-dimensional version of the heatmap.
- `animation.py`: Contains the methods to animate the double pendulum.
- `data.csv`: Contains the data of the Lyapunov exponents for different drop angles.
- `requirements.txt`: List of Python packages required for the project.
- `README.md`: This file.