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
    # grid_size = '(' + size + ')'
    (row, col) = grid_size.split(',')[0].replace("(", ""), grid_size.split(",")[1].replace(" ", "").replace(")", "")
    # for max_color in max_colors:
    df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "bottom_agent")]
    x = df1['Number of Colors']
    y = df1['Mean non-deterministic score after first move']
    plt.xlabel('Number of Colors')
    plt.ylabel('Mean non-deterministic score')
    plt.plot(x, y)
    filename = "%sX%s_mean_nondet_score" % (row, col)
    title = "%sX%s Grid" % (row, col)
    plt.title(title)
    plt.savefig(path+filename)
    plt.clf()


