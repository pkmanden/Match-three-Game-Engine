import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("exp_mean_median_results.csv")
# df = pd.read_csv("exp_mean_median_results_playable_settings.csv")
max_colors = sorted(df['Number of Colors'].unique().tolist())
grid_sizes = df['Grid Size'].unique().tolist()
agents = ["top_agent", "bottom_agent", "random_agent"]

for grid_size in grid_sizes:
    labels = []
    for agent in agents:
        (row, col) = grid_size.split(',')[0].replace("(", ""), grid_size.split(",")[1].replace(" ", "").replace(")", "")
        df1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == agent)]
        x = df1['Number of Colors']
        plt.xlabel('Number of Colours')
        # =============================Regenerations===================================================
        y = df1['Mean regenerations during init']
        plt.xlabel('Number of Colours')
        plt.ylabel('Regenerations during init')
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
        plt.show()
        plt.clf()
        plt.close()
        # =================================Deadlocks per move===============================================
        # y4 = df1['Mean Shuffles/Deadlocks Occurred per move']
        # plt.plot(x, y4)
        # plt.legend(['Shuffles/Deadlocks Occurred per move'])
        # title = "%sX%s Grid played by %s" % (row, col, agent)
        # plt.title(title)
        # plt.show()
        # plt.clf()
        # plt.close()
        # ================================Deadlocks per game================================================
        y5 = df1['Mean Shuffles/Deadlocks Occurred per game']
        plt.plot(x, y5)
        plt.legend(['Shuffles/Deadlocks Occurred per game'])
        title = "%sX%s Grid" % (row, col)
        plt.title(title)
        plt.show()
        plt.clf()
        plt.close()
        # ======================================Possible moves==========================================
        # y6 = df1['Mean Possible/Playable Moves per config']
        # plt.plot(x, y6)
        # plt.legend(['Possible/Playable Moves per config'])
        # title = "%sX%s Grid played by %s" % (row, col, agent)
        # plt.title(title)
        # plt.show()
        # plt.clf()
        # plt.close()
        # ====================================Valid moves made per game============================================
        y8 = df1['Mean Valid Moves Made']
        plt.plot(x, y8)
        plt.ylabel('Mean valid moves made per game')
        # plt.yticks(np.arange(5, 15, step=2.0))
        # plt.legend('Mean valid moves made')
        title = "%sX%s Grid" % (row, col)
        plt.title(title)
        plt.show()
        plt.clf()
