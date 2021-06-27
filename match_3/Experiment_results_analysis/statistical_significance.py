# Mann-Whitney U test
import csv
import os
import pandas as pd
from scipy.stats import mannwhitneyu

df = pd.read_csv('exp_results.csv', usecols=["Grid Size", "Number of Colors", "Agent", "Avg score per Game Setting"])
max_colors = df['Number of Colors'].unique().tolist()
grid_sizes = ['(5, 5)', '(10, 10)', '(15, 15)', '(20, 20)']
agents = ["top_agent", "bottom_agent"]

for grid_size in grid_sizes:
    labels = []
    (row, col) = grid_size.split(',')[0].replace("(", ""), grid_size.split(",")[1].replace(" ", "").replace(")", "")
    for color in max_colors:
        data_1 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == color) & (df['Agent'] == "top_agent")]
        data_2 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == color) & (df['Agent'] == "bottom_agent")]

        if grid_size == '(5, 5)':
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "top_agent") & (df['Number of Colors'] == color) & (df['Number of Colors'] >= 5) & (df['Number of Colors'] <= 8)]
            data_2 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "bottom_agent") & (df['Number of Colors'] == color) & (df['Number of Colors'] >= 5) & (df['Number of Colors'] <= 8)]
        if grid_size == '(10, 10)':
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "top_agent") & (df['Number of Colors'] == color) & (df['Number of Colors'] >= 10) & (df['Number of Colors'] <= 20)]
            data_2 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "bottom_agent") & (df['Number of Colors'] == color) & (df['Number of Colors'] >= 10) & (df['Number of Colors'] <= 20)]
        if grid_size == '(15, 15)':
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "top_agent") & (df['Number of Colors'] == color) & (df['Number of Colors'] >= 15) & (df['Number of Colors'] <= 30)]
            data_2 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "bottom_agent") & (df['Number of Colors'] == color) & (df['Number of Colors'] >= 15) & (df['Number of Colors'] <= 30)]
        if grid_size == '(20, 20)':
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "top_agent") & (df['Number of Colors'] == color) & (df['Number of Colors'] >= 20) & (df['Number of Colors'] <= 50)]
            data_2 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "bottom_agent") & (df['Number of Colors'] == color) & (df['Number of Colors'] >= 20) & (df['Number of Colors'] <= 50)]

        if not data_1.empty and not data_2.empty:
            data1 = data_1['Avg score per Game Setting'].copy()
            data2 = data_2['Avg score per Game Setting'].copy()
            # -----------------------Mann-Whitney U Test-------------------
            # compare samples
            stat, p = mannwhitneyu(data1, data2)
            file_exists = os.path.isfile("stat_significance.csv")
            with open('stat_significance.csv', 'a+', newline='') as csv_file:
                fieldnames = ['Grid Size',
                              'Number of Colors',
                              'statistics',
                              'p-value',
                              'Top agent Mean score',
                              'Top agent Median score',
                              'Top agent Std',
                              'Bottom agent Mean score',
                              'Bottom agent Median score',
                              'Bottom agent Std']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                if not file_exists:
                    print("File does not exist")
                    writer.writeheader()

                writer.writerow({
                    'Grid Size': grid_size,
                    'Number of Colors': color,
                    'statistics': '%f' %stat,
                    'p-value': '%f' % p,
                    'Top agent Mean score': round(data_1['Avg score per Game Setting'].mean(), 2),
                    'Top agent Median score': round(data_1['Avg score per Game Setting'].median(), 2),
                    'Top agent Std': round(data_1['Avg score per Game Setting'].std(), 2),
                    'Bottom agent Mean score': round(data_2['Avg score per Game Setting'].mean(), 2),
                    'Bottom agent Median score': round(data_2['Avg score per Game Setting'].median(), 2),
                    'Bottom agent Std': round(data_2['Avg score per Game Setting'].std(), 2)
                })

            print('Statistics=%f, p=%f' % (stat, p))
            # interpret
            alpha = 0.05
            if p > alpha:
                print(f'Same distribution (fail to reject H0) for {grid_size} and {color}')
            else:
                print(f'Different distribution (reject H0) for {grid_size} and {color}')
