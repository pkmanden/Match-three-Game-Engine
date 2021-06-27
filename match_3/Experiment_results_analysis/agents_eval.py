import csv
import os
import pandas as pd


df = pd.read_csv('exp_results_compare_agents.csv')
max_colors = df['Number of Colors'].unique().tolist()
grid_sizes = df['Grid Size'].unique().tolist()
agents = ["top_agent", "random_agent", "bottom_agent", "RL Agent(PPO)"]

for agent in agents:
    # data = pd.DataFrame()
    for grid_size in grid_sizes:
        # grid_size = '(' + size + ')'
        for max_color in max_colors:
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == max_color) & (df['Agent'] == agent)]
            # data.append(data_1)
            if not data_1.empty:
                file_exists = os.path.isfile("agents_eval.csv")
                with open('agents_eval.csv', 'a+', newline='') as csv_file:
                    fieldnames = ['Agent',
                                  'Grid Size',
                                  'Number of Colors',
                                  'Score Mean',
                                  'Score Median',
                                  'Score Std',
                                  'Score Variance',
                                  'Avalanche count Mean',
                                  'Avalanche count Median',
                                  'Avalanche count Std',
                                  'Avalanche count Variance',
                                  'Avalanche score Mean',
                                  'Avalanche score Median',
                                  'Avalanche score Std',
                                  'Avalanche score Variance',
                                  'Deterministic score Mean',
                                  'Deterministic score Median',
                                  'Deterministic score Std',
                                  'Deterministic score Variance']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                    if not file_exists:
                        print("File does not exist")
                        writer.writeheader()

                    writer.writerow({
                        'Agent': agent,
                        'Grid Size': grid_size,
                        'Number of Colors': max_color,
                        'Score Mean': round(data_1['Total score per game'].mean(), 2),
                        'Score Median': round(data_1['Total score per game'].median(), 2),
                        'Score Std': round(data_1['Total score per game'].std(), 2),
                        'Score Variance': round(data_1['Total score per game'].var(), 2),
                        'Avalanche count Mean': round(data_1['Total avalanche matches per game'].mean(), 2),
                        'Avalanche count Median': round(data_1['Total avalanche matches per game'].median(), 2),
                        'Avalanche count Std': round(data_1['Total avalanche matches per game'].std(), 2),
                        'Avalanche count Variance': round(data_1['Total avalanche matches per game'].var(), 2),
                        'Avalanche score Mean': round(data_1['Total avalanche score per game'].mean(), 2),
                        'Avalanche score Median': round(data_1['Total avalanche score per game'].median(), 2),
                        'Avalanche score Std': round(data_1['Total avalanche score per game'].std(), 2),
                        'Avalanche score Variance': round(data_1['Total avalanche score per game'].var(), 2),
                        'Deterministic score Mean': round(data_1['Total deterministic score per game'].mean(), 2),
                        'Deterministic score Median': round(data_1['Total deterministic score per game'].median(), 2),
                        'Deterministic score Std': round(data_1['Total deterministic score per game'].std(), 2),
                        'Deterministic score Variance': round(data_1['Total deterministic score per game'].var(), 2)
                    })
            # print(data_1)

