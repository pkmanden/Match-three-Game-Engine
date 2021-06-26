import math

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

df = pd.read_csv("exp_mean_median_results_playable_settings.csv")
max_colors = df['Number of Colors'].unique().tolist()
grid_sizes = df['Grid Size'].unique().tolist()
agents = ["top_agent", "bottom_agent", "random_agent"]

for grid_size in grid_sizes:
    labels = []
    ax = plt.figure().gca()
    (row, col) = grid_size.split(',')[0].replace("(", ""), grid_size.split(",")[1].replace(" ", "").replace(")", "")
    for agent in agents:
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
        y = df1['Mean score per Game Setting']
        plt.xlabel('Number of Colours')
        # ====================================Score per game============================================
        # plt.ylabel('Mean score per game')
        # plt.plot(x, y)
        # ====================================Avalanche per game============================================
        y_avalanche = df1['Mean Avalanche Matches per game']
        plt.plot(x, y_avalanche)
        plt.ylabel('Mean avalanche matches per game')
        if agent == 'top_agent':
            labels.append("RBA1")
        if agent == 'bottom_agent':
            labels.append("RBA2")
        if agent == 'random_agent':
            labels.append("random")
        plt.legend(labels)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        # yint = range(math.ceil(min(y_avalanche)), math.ceil(max(y_avalanche))+1)
        # plt.yticks(yint)

        # ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    title = "%sX%s Grid" % (row, col)
    plt.title(title)
    plt.show()


