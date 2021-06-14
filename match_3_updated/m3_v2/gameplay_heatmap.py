import csv
import os
from itertools import product

import numpy as np

from m3_globals import *
import matplotlib.pyplot as plt
import seaborn as sb

class GameplayHeatmap:

    def points_generator(self):
        # iterates over points on the board
        (rows, cols) = BOARD_SIZE
        points = [(i, j) for i, j in product(range(rows), range(cols))]
        for point in points:
            yield point


    def __init__(self):
        actions = list()
        (rows, cols) = BOARD_SIZE
        for point in self.points_generator():
            (a, b) = point
            neighbors = [(i, j) for i, j in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)) if
                         0 <= i < rows and 0 <= j < cols]
            for n in neighbors:
                actions.append([point, n])
        for action in actions:
            [coord1, coord2] = action
            if [coord2, coord1] and [coord1, coord2] in actions:
                actions.remove([coord2, coord1])

        action_num = [i for i in range(len(actions))]
        self.action_dict = dict(zip(action_num, actions))
        self.edge_freq_random_agent = np.zeros(BOARD_SIZE)
        self.edge_freq_bottom_agent = np.zeros(BOARD_SIZE)
        self.edge_freq_rl_agent = np.zeros(BOARD_SIZE)
        # return action_dict


    def add_move_to_graph(self, move, agent):
        (coord1, coord2) = move
        if agent == "random_agent":
            self.edge_freq_random_agent[coord1] += 1
            self.edge_freq_random_agent[coord2] += 1
        if agent == "bottom_agent":
            self.edge_freq_bottom_agent[coord1] += 1
            self.edge_freq_bottom_agent[coord2] += 1
        if agent == "rl_agent":
            self.edge_freq_rl_agent[coord1] += 1
            self.edge_freq_rl_agent[coord2] += 1

    def draw_map(self, agent):
        heat_map = None
        heat_array = None
        if agent == "random_agent":
            heat_map = sb.heatmap(self.edge_freq_random_agent, cmap="Reds")
            heat_array = self.edge_freq_random_agent
        if agent == "bottom_agent":
            heat_map = sb.heatmap(self.edge_freq_bottom_agent, cmap="Reds")
            heat_array = self.edge_freq_bottom_agent
        if agent == "rl_agent":
            heat_map = sb.heatmap(self.edge_freq_rl_agent, cmap="Reds")
            heat_array = self.edge_freq_rl_agent

        heat_map.xaxis.tick_top()
        filename = '%s_heatmap' % agent
        plt.savefig(filename)
        file_exists = os.path.isfile("heatmap.csv")
        with open('heatmap.csv', 'a+', newline='') as csv_file:
            fieldnames = ['Agent',
                          'Grid Size',
                          'Number of Colors',
                          'Game Grid']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exists:
                print("File does not exist")
                writer.writeheader()

            writer.writerow({
                'Agent': agent,
                'Grid Size': BOARD_SIZE,
                'Number of Colors': COLOR_END,
                'Game Grid': heat_array
            })
        plt.show()