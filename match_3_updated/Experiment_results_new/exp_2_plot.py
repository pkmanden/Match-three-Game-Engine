import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

df = pd.read_csv("exp_mean_median_results_playable_settings.csv")
grid_sizes = ['(5, 5)', '(10, 10)', '(15, 15)', '(20, 20)']
max_colors = df['Number of Colors'].unique().tolist()
agents = ["top_agent", "bottom_agent", "random_agent"]

# ============for non-deterministic score plot===========
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
        y = df1['Mean non-deterministic score after first move']
        # y = df1['Mean avalanche matches after first move']
        plt.xlabel('Number of Colours')
        plt.ylabel('Mean non-deterministic score')
        # plt.ylabel('Mean avalanche matches')
        plt.plot(x, y)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        if agent == 'bottom_agent':
            labels.append("RBA2")
        if agent == 'top_agent':
            labels.append("RBA1")
        if agent == 'random_agent':
            labels.append("random")
        plt.legend(labels)
    title = "%sX%s Grid" % (row, col)
    plt.title(title)
    plt.show()
    plt.close()

