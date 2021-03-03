import csv
import os
import pandas as pd
from scipy.stats import spearmanr


df = pd.read_csv('exp_game_results_3.csv')
# grid_sizes = ['(5, 5)', '(7, 7)', '(10, 10)', '(15, 15)', '(20, 20)']
input_data = pd.read_csv('exp_3_game_setting.csv')
max_colors = input_data['color_end'].unique().tolist()
grid_sizes = input_data['grid_size'].unique().tolist()

for size in grid_sizes:
    grid_size = '(' + size + ')'
    rows = int(grid_size.split(',', 1)[0].replace('(', ""))
    for max_color in max_colors:
        data_1 = df[(df['Grid Size'] == grid_size) & (df['Max Colors'] == max_color)]
        if not data_1.empty:
            for row in range(rows):
                # print(row)
                data = data_1[(data_1['Selected Move'].str.contains(r'\[\(' + str(row) + ', .\), \(' + str(row) + ', .\)\]'))]
                row_avalanche = data['Avalanche per selected move'].mean()
                row_score = data['Move Score'].mean()
                file_exists = os.path.isfile("exp_3_analysis.csv")
                with open('exp_3_analysis.csv', 'a+', newline='') as csv_file:
                    fieldnames = ['Grid Size',
                                  'Max Colors',
                                  'Move Position / Row',
                                  'Avalanche count',
                                  'Score per Move']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow({'Grid Size': grid_size,
                                     'Max Colors': max_color,
                                     'Move Position / Row': row,
                                     'Avalanche count': row_avalanche,
                                     'Score per Move': row_score})

dataframe = pd.read_csv('exp_3_analysis.csv')
for size in grid_sizes:
    grid_size = '(' + size + ')'
    rows = int(grid_size.split(',', 1)[0].replace('(', ""))
    for max_color in max_colors:
        df_1 = dataframe[(dataframe['Grid Size'] == grid_size) & (dataframe['Max Colors'] == max_color)]
        if not df_1.empty:
            x = df_1['Move Position / Row']
            y = df_1['Score per Move']
            corr, _ = spearmanr(x, y)
            print(f'Spearmans correlation for {rows} x {rows} grid with max {max_color} colors: {corr:.3f}')

