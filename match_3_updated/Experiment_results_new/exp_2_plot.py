import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.expanduser("~/Desktop/Desktop/Prathisha/Master_Thesis/Experiments/plots/1/")

df = pd.read_csv("exp_mean_median_results.csv")
# grid_sizes = ['(5, 5)', '(7, 7)', '(10, 10)', '(15, 15)', '(20, 20)']
# input_data = pd.read_csv('../m3/exp_game_setting.csv')
max_colors = df['Number of Colors'].unique().tolist()
grid_sizes = df['Grid Size'].unique().tolist()
agents = ["top_agent", "bottom_agent"]


for grid_size in grid_sizes:
    labels = []
    # grid_size = '(' + size + ')'
    (row, col) = grid_size.split(',')[0].replace("(", ""), grid_size.split(",")[1].replace(" ", "").replace(")", "")
    for agent in agents:
        df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent)]

        if grid_size == '(5, 5)':
            df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent) & (df['Number of Colors'] >= 5) & (df['Number of Colors'] <= 10)]
        if grid_size == '(10, 10)':
            df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent) & (df['Number of Colors'] >= 10) & (df['Number of Colors'] <= 20)]
        if grid_size == '(15, 15)':
            df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent) & (df['Number of Colors'] >= 10) & (df['Number of Colors'] <= 40)]
        if grid_size == '(20, 20)':
            df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent) & (df['Number of Colors'] >= 15) & (df['Number of Colors'] <= 50)]

        x = df1['Number of Colors']
        y = df1['Mean non-deterministic score after first move']
        plt.xlabel('Number of Colors')
        plt.ylabel('Mean non-deterministic score')
        plt.plot(x, y)
        labels.append(agent)
        plt.legend(labels)
    filename = "%sX%s_mean_nondet_score" % (row, col)
    title = "%sX%s Grid" % (row, col)
    plt.title(title)
    plt.savefig(path+filename)
    # plt.show()
    plt.clf()


