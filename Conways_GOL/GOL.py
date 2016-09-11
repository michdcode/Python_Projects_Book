import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import argparse


def initial_state():
    """A function I added to clean up code. 0 is off and 255 is on."""

    ON = 255
    OFF = 0
    vals = [ON, OFF]
    return vals

initial_state()


def random_grid(N, vals):
    """Grid of NxN of random values, can change probability p, reshape 2 dimens."""

    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def add_pattern(i, j, grid):
    """Two-dimensional grid with pattern that moves from top left cell(i, j)."""

    glider = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
    # slices np array
    grid[i:i + 3, j:j+3] = glider


def update(frame_num, img, grid, N):
    """Copies grid & updates each square based on neighbors. Pacman boundaries."""

    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # slices array to define boundaries that wrap around edges
            total = int((grid[i, (j-1) % N] + grid[i, (j+1) % N] +
                         grid[(i-1) % N, j] + grid[(i+1) % N, j] +
                         grid[(i-1) % N, (j-1) % N] + grid[(i-1) % N, (j+1) % N] +
                         grid[(i+1) % N, (j-1) % N] + grid[(i+1) % N, (j+1) % N])/255)
            #sum value of neighbors & divide by 255 to figure out ON cells
            if grid[i, j] == ON:
                if total < 2 or total > 3:
                    new_grid[i, j] = OFF
                elif total == 3:
                    new_grid[i, j] = ON

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


def main():
    """Command line arguments and set up."""

    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()

    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)
    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)
    # declare grid
    grid = np.array([])
    # check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        add_pattern(1, 1, grid)
    else:
        # populate grid with random on/off - more off than on
        grid = random_grid(N)
    # set up the animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)
     # set the output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()

    if __name__ == '__main__':
        main()
