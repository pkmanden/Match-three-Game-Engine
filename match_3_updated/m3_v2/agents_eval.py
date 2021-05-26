import csv
import os
import pandas as pd


df = pd.read_csv('exp_results_compare_agents_10X10_15.csv')
# grid_sizes = ['(5, 5)', '(7, 7)', '(10, 10)', '(15, 15)', '(20, 20)']
# input_data = pd.read_csv('../m3/exp_game_setting.csv')
max_colors = df['Number of Colors'].unique().tolist()
grid_sizes = df['Grid Size'].unique().tolist()
agents = ["random_agent", "bottom_agent", "RL Agent(PPO)"]

for agent in agents:
    # data = pd.DataFrame()
    for grid_size in grid_sizes:
        # grid_size = '(' + size + ')'
        for max_color in max_colors:
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == max_color) & (df['Agent'] == agent)]
            # data.append(data_1)
            if not data_1.empty:

                data_score_mean = data_1['Total score per Game Setting'].mean()
                data_score_median = data_1['Total score per Game Setting'].median()
                data_score_std = data_1['Total score per Game Setting'].std()
                data_score_var = data_1['Total score per Game Setting'].var()

                # print(data_regen_mean)
                # filename = "%s.csv" % agent
                # data_regen_mean.to_csv(filename, index=False)
                file_exists = os.path.isfile("agents_eval_total_score_reward.csv")
                with open('agents_eval_total_score_reward.csv', 'a+', newline='') as csv_file:
                    fieldnames = ['Agent',
                                  'Grid Size',
                                  'Number of Colors',
                                  'Mean',
                                  'Median',
                                  'Standard Deviation',
                                  'Variance']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                    if not file_exists:
                        print("File does not exist")
                        writer.writeheader()

                    writer.writerow({
                        'Agent': agent,
                        'Grid Size': grid_size,
                        'Number of Colors': max_color,
                        'Mean': data_score_mean,
                        'Median': data_score_median,
                        'Standard Deviation': data_score_std,
                        'Variance': data_score_var
                    })
            # print(data_1)

