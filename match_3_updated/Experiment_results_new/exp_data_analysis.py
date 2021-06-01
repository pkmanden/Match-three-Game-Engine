import csv
import os
import pandas as pd


df = pd.read_csv('exp_results.csv')
# grid_sizes = ['(5, 5)', '(7, 7)', '(10, 10)', '(15, 15)', '(20, 20)']
# input_data = pd.read_csv('../m3/exp_game_setting.csv')
max_colors = sorted(df['Number of Colors'].unique().tolist())
grid_sizes = df['Grid Size'].unique().tolist()
agents = ["top_agent", "bottom_agent", "NotApplicable"]

for agent in agents:
    # data = pd.DataFrame()
    for grid_size in grid_sizes:
        # grid_size = '(' + size + ')'
        for max_color in max_colors:
            data_1 = df[(df['Grid Size'] == grid_size) & (df['Number of Colors'] == max_color) & (df['Agent'] == agent)]
            # data.append(data_1)
            if not data_1.empty:
                data_regen_mean = data_1['Total No. of Regenerations until valid board generation'].mean()
                data_regen_median = data_1['Total No. of Regenerations until valid board generation'].median()
                data_regen_match_mean = data_1['Total No. of Times Matches Occurred during init'].mean()
                data_regen_match_median = data_1['Total No. of Times Matches Occurred during init'].median()
                data_regen_deadlock_mean = data_1['Total No. of Deadlocks during init'].mean()
                data_regen_deadlock_median = data_1['Total No. of Deadlocks during init'].median()
                data_deadlock_per_move_mean = data_1['Avg No. of Shuffles/Deadlocks Occurred per move'].mean()
                data_deadlock_per_move_median = data_1['Avg No. of Shuffles/Deadlocks Occurred per move'].median()
                data_deadlock_per_game_mean = data_1['Avg No. of Shuffles/Deadlocks Occurred per game'].mean()
                data_deadlock_per_game_median = data_1['Avg No. of Shuffles/Deadlocks Occurred per game'].median()
                data_score_mean = data_1['Avg score per Game Setting'].mean()
                data_score_median = data_1['Avg score per Game Setting'].median()
                data_valid_moves_mean = data_1['Avg Valid Moves Made'].mean()
                data_valid_moves_median = data_1['Avg Valid Moves Made'].median()
                data_possible_moves_mean = data_1['Avg No. of Possible/Playable Moves per config'].mean()
                data_possible_moves_median = data_1['Avg No. of Possible/Playable Moves per config'].median()
                data_avalanche_mean = data_1['Avg No. of Avalanche Matches per game'].mean()
                data_avalanche_median = data_1['Avg No. of Avalanche Matches per game'].median()
                data_det_score_mean = data_1['Avg deterministic score after first move'].mean()
                data_det_score_median = data_1['Avg deterministic score after first move'].median()
                data_nondet_score_mean = data_1['Avg non-deterministic score after first move'].mean()
                data_nondet_score_median = data_1['Avg non-deterministic score after first move'].median()

                # print(data_regen_mean)
                # filename = "%s.csv" % agent
                # data_regen_mean.to_csv(filename, index=False)
                file_exists = os.path.isfile("exp_mean_median_results.csv")
                with open('exp_mean_median_results.csv', 'a+', newline='') as csv_file:
                    fieldnames = ['Agent',
                                  'Grid Size',
                                  'Number of Colors',
                                  'Mean regenerations during init',
                                  'Median regenerations during init',
                                  'Mean Matches Occurred during init',
                                  'Median Matches Occurred during init',
                                  'Mean Deadlocks during init',
                                  'Median Deadlocks during init',
                                  'Mean Shuffles/Deadlocks Occurred per move',
                                  'Median Shuffles/Deadlocks Occurred per move',
                                  'Mean Shuffles/Deadlocks Occurred per game',
                                  'Median Shuffles/Deadlocks Occurred per game',
                                  'Mean score per Game Setting',
                                  'Median score per Game Setting',
                                  'Mean Valid Moves Made',
                                  'Median Valid Moves Made',
                                  'Mean Possible/Playable Moves per config',
                                  'Median Possible/Playable Moves per config',
                                  'Mean Avalanche Matches per game',
                                  'Median Avalanche Matches per game',
                                  'Mean deterministic score after first move',
                                  'Median deterministic score after first move',
                                  'Mean non-deterministic score after first move',
                                  'Median non-deterministic score after first move']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                    if not file_exists:
                        print("File does not exist")
                        writer.writeheader()

                    writer.writerow({
                        'Agent': agent,
                        'Grid Size': grid_size,
                        'Number of Colors': max_color,
                        'Mean regenerations during init': data_regen_mean,
                        'Median regenerations during init': data_regen_median,
                        'Mean Matches Occurred during init': data_regen_match_mean,
                        'Median Matches Occurred during init': data_regen_match_median,
                        'Mean Deadlocks during init': data_regen_deadlock_mean,
                        'Median Deadlocks during init': data_regen_deadlock_median,
                        'Mean Shuffles/Deadlocks Occurred per move': data_deadlock_per_move_mean,
                        'Median Shuffles/Deadlocks Occurred per move': data_deadlock_per_move_median,
                        'Mean Shuffles/Deadlocks Occurred per game': data_deadlock_per_game_mean,
                        'Median Shuffles/Deadlocks Occurred per game': data_deadlock_per_game_median,
                        'Mean score per Game Setting': data_score_mean,
                        'Median score per Game Setting': data_score_median,
                        'Mean Valid Moves Made': data_valid_moves_mean,
                        'Median Valid Moves Made': data_valid_moves_median,
                        'Mean Possible/Playable Moves per config': data_possible_moves_mean,
                        'Median Possible/Playable Moves per config': data_possible_moves_median,
                        'Mean Avalanche Matches per game': data_avalanche_mean,
                        'Median Avalanche Matches per game': data_avalanche_median,
                        'Mean deterministic score after first move': data_det_score_mean,
                        'Median deterministic score after first move': data_det_score_median,
                        'Mean non-deterministic score after first move': data_nondet_score_mean,
                        'Median non-deterministic score after first move': data_nondet_score_median
                    })
            # print(data_1)

