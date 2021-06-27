import pandas as pd
import os
import csv

df = pd.read_csv("exp_results_playable_range.csv")
max_colors = df['Number of Colors'].unique().tolist()
grid_sizes = ['(5, 5)', '(10, 10)', '(15, 15)', '(20, 20)']
agents = ["top_agent", "bottom_agent", "random_agent"]

for grid_size in grid_sizes:
    labels = []
    (row, col) = grid_size.split(',')[0].replace("(", ""), grid_size.split(",")[1].replace(" ", "").replace(")", "")
    for color in max_colors:
        data_1 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == color) & (df['Agent'] == "top_agent")]
        data_2 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == color) & (df['Agent'] == "bottom_agent")]
        data_3 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == color) & (df['Agent'] == "random_agent")]

        if grid_size == '(5, 5)':
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "top_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 5) & (df['Number of Colors'] <= 8)]
            data_2 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "bottom_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 5) & (df['Number of Colors'] <= 8)]
            data_3 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "random_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 5) & (df['Number of Colors'] <= 8)]
        if grid_size == '(10, 10)':
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "top_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 10) & (df['Number of Colors'] <= 20)]
            data_2 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "bottom_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 10) & (df['Number of Colors'] <= 20)]
            data_3 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "random_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 10) & (df['Number of Colors'] <= 20)]
        if grid_size == '(15, 15)':
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "top_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 15) & (df['Number of Colors'] <= 30)]
            data_2 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "bottom_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 15) & (df['Number of Colors'] <= 30)]
            data_3 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "random_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 15) & (df['Number of Colors'] <= 30)]
        if grid_size == '(20, 20)':
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "top_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 20) & (df['Number of Colors'] <= 50)]
            data_2 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "bottom_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 20) & (df['Number of Colors'] <= 50)]
            data_3 = df[(df['Grid Size'] == grid_size) & (df['Agent'] == "random_agent") &
                        (df['Number of Colors'] == color) & (df['Number of Colors'] >= 20) & (df['Number of Colors'] <= 50)]

        if not data_1.empty and not data_2.empty and not data_3.empty:
            file_exists = os.path.isfile("exp_2_det_score.csv")
            with open('exp_2_det_score.csv', 'a+', newline='') as csv_file:
                fieldnames = ['Grid Size',
                              'Number of Colors',
                              'Top agent mean det score',
                              'Top agent std',
                              'Bottom agent mean det score',
                              'Bottom agent Std',
                              'Random agent mean det score',
                              'Random agent std']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                if not file_exists:
                    print("File does not exist")
                    writer.writeheader()

                writer.writerow({
                    'Grid Size': grid_size,
                    'Number of Colors': color,
                    'Top agent mean det score': round(data_1['Avg deterministic score after first move'].mean(), 2),
                    'Top agent std': round(data_1['Avg deterministic score after first move'].std(), 2),
                    'Bottom agent mean det score': round(data_2['Avg deterministic score after first move'].mean(), 2),
                    'Bottom agent Std': round(data_2['Avg deterministic score after first move'].std(), 2),
                    'Random agent mean det score': round(data_3['Avg deterministic score after first move'].mean(), 2),
                    'Random agent std': round(data_3['Avg deterministic score after first move'].std(), 2)
                })
