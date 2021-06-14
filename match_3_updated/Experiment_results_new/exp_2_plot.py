import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os
from matplotlib.ticker import FormatStrFormatter


path = os.path.expanduser("~/Desktop/Desktop/Prathisha/Master_Thesis/Experiments/plots/1/")

df = pd.read_csv("exp_mean_median_results_1.csv")
grid_sizes = ['(5, 5)', '(10, 10)', '(15, 15)', '(20, 20)']
# input_data = pd.read_csv('../m3/exp_game_setting.csv')
max_colors = df['Number of Colors'].unique().tolist()
# grid_sizes = df['Grid Size'].unique().tolist()
agents = ["top_agent", "bottom_agent"]


for grid_size in grid_sizes:

    # for non-deterministic score plot
    # labels = []
    # ax = plt.figure().gca()

    # ======================
    # grid_size = '(' + size + ')'
    (row, col) = grid_size.split(',')[0].replace("(", ""), grid_size.split(",")[1].replace(" ", "").replace(")", "")
    for agent in agents:
        # for deterministic score plot
        labels = []
        ax = plt.figure().gca()
        # =====================
        df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent)]

        if grid_size == '(5, 5)':
            df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent) & (df['Number of Colors'] >= 5) & (df['Number of Colors'] <= 8)]
        if grid_size == '(10, 10)':
            df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent) & (df['Number of Colors'] >= 10) & (df['Number of Colors'] <= 20)]
        if grid_size == '(15, 15)':
            df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent) & (df['Number of Colors'] >= 15) & (df['Number of Colors'] <= 30)]
        if grid_size == '(20, 20)':
            df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent) & (df['Number of Colors'] >= 20) & (df['Number of Colors'] <= 50)]

        x = df1['Number of Colors']
        y = df1['Mean deterministic score after first move']

        # for non-deterministic score plot
        # y = df1['Mean non-deterministic score after first move']
        # ============================
        plt.xlabel('Number of Colors')
        plt.ylabel('Mean deterministic score')

        # for non-deterministic score plot
        # plt.ylabel('Mean non-deterministic score')
        color = 'tab:blue'
        if agent == 'bottom_agent':
            color = 'tab:orange'

        # for deterministic score plot
        plt.ylim(0, 6)
        plt.plot(x, y, color=color)
        # ==========================

        # plt.plot(x, y)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        labels.append(agent)
        plt.legend(labels)
        # for deterministic score plot
        filename = "%sX%s_mean_det_score_%s" % (row, col, agent)
        title = "%sX%s Grid played by %s" % (row, col, agent)
        plt.title(title)
        plt.savefig(path+filename)
        # plt.show()
        plt.clf()
    #     =============================

    # for non-deterministic score plot
    # filename = "%sX%s_mean_nondet_score" % (row, col)
    # title = "%sX%s Grid" % (row, col)
    # plt.title(title)
    # plt.savefig(path+filename)
    # plt.show()
    # plt.clf()
    # =============================

