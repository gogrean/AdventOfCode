import numpy as np

start = np.loadtxt("grid.txt", dtype=str, comments='', \
    converters={0: lambda x: list(x.decode("utf-8"))})
start[start=='#'] = 1
start[start=='.'] = 0
start = start.astype(int)

grid = np.pad(start, pad_width=((1, 1),(1 ,1)), mode='constant', constant_values=0)

rows, cols = np.shape(grid)

n_steps = 100
current_step = 1

while current_step <= n_steps:
    end = np.zeros((rows, cols))
    tmp = np.zeros((rows, cols))
    shift_up = grid[0:rows-2, 0:cols-2] + grid[0:rows-2, 2:cols] + \
        grid[0:rows-2, 1:cols-1]
    shift_down = grid[2:rows, 0:cols-2] + grid[2:rows, 1:cols-1] + \
        grid[2:rows, 2:cols]
    shift_left = grid[1:rows-1, 0:cols-2]
    shift_right = grid[1:rows-1, 2:cols]
    end[1:rows-1, 1:cols-1] = shift_up + shift_down + shift_left + shift_right
    tmp[((grid == 0) & (end == 3)) | ((grid == 1) & ((end == 2) | (end == 3)))] = 1
    grid = tmp
    current_step += 1

print("The sum of the ligths is %i." % np.sum(grid))


######## 


current_step = 1

grid = np.pad(start, pad_width=((1, 1),(1 ,1)), mode='constant', constant_values=0)
grid[[1, 1, rows-2, rows-2], [1, cols-2, 1, cols-2]] = 1

while current_step <= n_steps:
    end = np.zeros((rows, cols))
    tmp = np.zeros((rows, cols))
    shift_up = grid[0:rows-2, 0:cols-2] + grid[0:rows-2, 2:cols] + \
        grid[0:rows-2, 1:cols-1]
    shift_down = grid[2:rows, 0:cols-2] + grid[2:rows, 1:cols-1] + \
        grid[2:rows, 2:cols]
    shift_left = grid[1:rows-1, 0:cols-2]
    shift_right = grid[1:rows-1, 2:cols]
    end[1:rows-1, 1:cols-1] = shift_up + shift_down + shift_left + shift_right
    tmp[((grid == 0) & (end == 3)) | ((grid == 1) & ((end == 2) | (end == 3)))] = 1
    tmp[[1, 1, rows-2, rows-2], [1, cols-2, 1, cols-2]] = 1
    grid = tmp
    current_step += 1

print("The sum of the ligths is %i." % np.sum(grid))
       
