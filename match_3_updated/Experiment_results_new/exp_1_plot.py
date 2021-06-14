import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.expanduser("~/Desktop/Desktop/Prathisha/Master_Thesis/Experiments/plots/1/")

df = pd.read_csv("exp_mean_median_results_1.csv")
max_colors = sorted(df['Number of Colors'].unique().tolist())
grid_sizes = df['Grid Size'].unique().tolist()
agents = ["top_agent", "bottom_agent"]

for grid_size in grid_sizes:
    for agent in agents:
        # grid_size = '(' + size + ')'
        (row, col) = grid_size.split(',')[0].replace("(", ""), grid_size.split(",")[1].replace(" ", "").replace(")", "")
        # for max_color in max_colors:
        df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent)]
        x = df1['Number of Colors']
        y = df1['Mean regenerations during init']
        plt.xlabel('Number of Colors')
        # plt.ylabel('Regenerations during init')
        plt.plot(x, y)
        y2 = df1['Mean Matches Occurred during init']
        plt.plot(x, y2)
        y3 = df1['Mean Deadlocks during init']
        plt.plot(x, y3)

        plt.legend(['Regenerations during init',
                    'Matches Occurred during init',
                    'Deadlocks during init'])
        title = "%sX%s Grid" % (row, col)
        plt.title(title)
        filename = "%sX%s_regen_init" % (row, col)
        plt.savefig(path+filename)
        plt.show()
        plt.clf()
        y4 = df1['Mean Shuffles/Deadlocks Occurred per move']
        plt.plot(x, y4)
        plt.legend(['Shuffles/Deadlocks Occurred per move'])
        title = "%sX%s Grid played by %s" % (row, col, agent)
        plt.title(title)
        filename = "%sX%s_mean_deadlock_%s" % (row, col, agent)
        plt.savefig(path+filename)
        # plt.show()
        plt.clf()
        y5 = df1['Mean Shuffles/Deadlocks Occurred per game']
        plt.plot(x, y5)
        plt.legend(['Shuffles/Deadlocks Occurred per game'])
        title = "%sX%s Grid" % (row, col)
        plt.title(title)
        filename = "%sX%s_mean_shuffle_per_game" % (row, col)
        plt.savefig(path+filename)
        # plt.show()
        plt.clf()
        # y6 = df1['Mean Possible/Playable Moves per config']
        # plt.plot(x, y6)
        # plt.legend(['Possible/Playable Moves per config'])
        # title = "%sX%s Grid played by %s" % (row, col, agent)
        # plt.title(title)
        # filename = "%sX%s_mean_possible_moves_%s" % (row, col, agent)
        # # plt.savefig(path+filename)
        # # plt.show()
        # plt.clf()
        # y7 = df1['Mean Avalanche Matches per game']
        # plt.plot(x, y7)
        # if grid_size == '(20, 20)':
        #     print('20X20 grid avalanche')
        #     plt.yticks(np.arange(0, 2, 0.30))
        #
        # plt.legend(['Avalanche Matches per game'])
        # title = "%sX%s Grid played by %s" % (row, col, agent)
        # plt.title(title)
        # filename = "%sX%s_mean_avalanche_%s" % (row, col, agent)
        # # plt.savefig(path+filename)
        # # plt.show()
        # plt.clf()
        # filename = "%s.csv" % agent
        # title = "%sX%s Grid played by %s" % (row, col, agent)
        # plt.show()
