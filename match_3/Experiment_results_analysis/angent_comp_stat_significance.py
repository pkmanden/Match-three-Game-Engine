import os
import numpy as np
import pandas as pd
import scikit_posthocs as sp
from scipy.stats import friedmanchisquare

df = pd.read_csv('exp_results_compare_agents.csv', usecols=["Grid Size", "Number of Colors", "Agent", "Total score per game"])
max_colors = df['Number of Colors'].unique().tolist()
grid_sizes = ['(5, 5)', '(10, 10)', '(15, 15)', '(20, 20)']
agents = ["top_agent", "bottom_agent", "random_agent", "RL Agent(PPO)"]
step = 50
for grid_size in grid_sizes:
    labels = []
    (row, col) = grid_size.split(',')[0].replace("(", ""), grid_size.split(",")[1].replace(" ", "").replace(")", "")
    for color in max_colors:
        data_1 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == color) & (df['Agent'] == "top_agent")]
        data_2 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == color) & (df['Agent'] == "bottom_agent")]
        data_3 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == color) & (df['Agent'] == "random_agent")]
        data_4 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == color) & (df['Agent'] == "RL Agent(PPO)")]
        if not data_1.empty and not data_2.empty and not data_3.empty and not data_4.empty:

            data1 = data_1['Total score per game'].copy().reset_index(drop=True)
            df_1 = data1.groupby(data1.index // step).mean().tolist()
            # del df_1[20:]
            data2 = data_2['Total score per game'].copy().reset_index(drop=True)
            df_2 = data2.groupby(data2.index // step).mean().tolist()
            # del df_2[20:]
            data3 = data_3['Total score per game'].copy().reset_index(drop=True)
            df_3 = data3.groupby(data3.index // step).mean().tolist()
            # del df_3[20:]
            data4 = data_4['Total score per game'].copy().reset_index(drop=True)
            df_4 = data4.groupby(data4.index // step).mean().tolist()
            # del df_4[20:]
            # -----------------------Friedman Test-------------------
            # compare samples
            print(friedmanchisquare(df_1, df_2, df_3, df_4))
            stat, p = friedmanchisquare(df_1, df_2, df_3, df_4)
            file_exists = os.path.isfile("stat_significance_agent_comp.csv")
            # with open('stat_significance_agent_comp.csv', 'a+', newline='') as csv_file:
            #     fieldnames = ['Grid Size',
            #                   'Number of Colors',
            #                   'statistics',
            #                   'p-value',
            #                   'Top agent Mean score',
            #                   'Top agent Median score',
            #                   'Top agent Std',
            #                   'Bottom agent Mean score',
            #                   'Bottom agent Median score',
            #                   'Bottom agent Std',
            #                   'Random agent Mean score',
            #                   'Random agent Median score',
            #                   'Random agent Std',
            #                   'RL agent Mean score',
            #                   'RL agent Median score',
            #                   'RL agent Std']
            #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #
            #     if not file_exists:
            #         print("File does not exist")
            #         writer.writeheader()
            #
            #     writer.writerow({
            #         'Grid Size': grid_size,
            #         'Number of Colors': color,
            #         'statistics': '%f' % stat,
            #         'p-value': '%f' % p,
            #         'Top agent Mean score': round(statistics.mean(df_1), 2),
            #         'Top agent Median score': round(statistics.median(df_1), 2),
            #         'Top agent Std': round(statistics.stdev(df_1), 2),
            #         'Bottom agent Mean score': round(statistics.mean(df_2), 2),
            #         'Bottom agent Median score': round(statistics.median(df_2), 2),
            #         'Bottom agent Std': round(statistics.stdev(df_2), 2),
            #         'Random agent Mean score': round(statistics.mean(df_3), 2),
            #         'Random agent Median score': round(statistics.median(df_3), 2),
            #         'Random agent Std': round(statistics.stdev(df_3), 2),
            #         'RL agent Mean score': round(statistics.mean(df_4), 2),
            #         'RL agent Median score': round(statistics.median(df_4), 2),
            #         'RL agent Std': round(statistics.stdev(df_4), 2)
            #     })
            #
            # print('Statistics=%f, p=%f' % (stat, p))
            # interpret
            alpha = 0.05
            if p > alpha:
                print(f'Same distribution (fail to reject H0) for {grid_size} and {color}')
            else:
                print(f'Different distribution (reject H0) for {grid_size} and {color}')

            #combine three groups into one array
            data = np.array([df_1, df_3, df_2, df_4])

            #perform Nemenyi post-hoc test
            print(sp.posthoc_nemenyi_friedman(data.T).round(3))

