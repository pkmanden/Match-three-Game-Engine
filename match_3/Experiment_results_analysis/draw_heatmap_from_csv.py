import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

with open('heatmap.csv', newline='') as heatmap_file:
    heatmap_reader = csv.reader(heatmap_file)
    next(heatmap_reader)
    for line in heatmap_reader:
        agent = line[0]
        grid_size = line[1]
        grid_size = int(grid_size.split(',')[0].replace("(", "")), int(grid_size.split(",")[1].replace(" ", "").replace(")", ""))
        row, col = grid_size
        num_colors = line[2]
        matrix = line[3]
        matrix = matrix.replace('[', '')
        matrix = matrix.replace(']', '')

        array1d = np.fromstring(matrix, dtype=int, sep=',')
        matrix = array1d.reshape(grid_size)

        if grid_size == (5, 5):
            max_val = 25000
        if grid_size == (10, 10):
            max_val = 6000
        if grid_size == (15, 15):
            max_val = 3000
        heat_map = sb.heatmap(matrix, cmap="Reds", vmin=0, vmax=max_val)
        heat_map.xaxis.tick_top()
        plt.show()
