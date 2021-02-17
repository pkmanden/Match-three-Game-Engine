import logging
# import time
import csv
import os
import math
from match_3_constants_exp import *


class Experiment:

    def __init__(self):
        self.actual_num_colors_start = 0
        # ===============# for experiment 1#===================
        self.exp_total_game_starts = 0 # total number of times game started
        self.exp_total_score = 0  # total score for a given setting across multiple plays
        self.exp_total_num_regenerations = 0  # count for getting total number of regenerations during init
        self.exp_total_num_shuffles = 0  # count for getting total number of shuffles
        self.exp_total_moves = 0  # count for getting average number of moves per shuffle
        # self.exp_total_deadlock_count = 0  # count of occurences of no moves
        # self.exp_total_config_count = 0  # count of total number of board configurations
        self.exp_total_possible_moves_count = 0  # count of total number of possible moves
        self.exp_total_avalanche_match_count = 0  # count the number of avalanche matches occurred
        self.exp_init_invalid_match_three_count = 0  # count of total number of times matches occurred during board regeneration
        self.exp_init_deadlock = 0  # count of total number of times no possible moves found during board regeneration
        # ============================================================
        # ===============# for experiment 2#===================
        self.total_user_move_count = 0
        self.total_avalanche_count = 0
        self.total_user_move_score = 0
        self.total_avalanche_score = 0
        # ======================================================
        # ===============# for experiment 3#===================
        self.move_score = 0
        self.avalanche_per_move = 0
        # ======================================================

    def store_experiment_1_result(self, grid_size, max_colors):

        if self.exp_total_moves == 0:
            score_per_move = 0
            avg_possible_moves_per_config = math.inf
        else:
            score_per_move = self.exp_total_score / self.exp_total_moves
            avg_possible_moves_per_config = self.exp_total_possible_moves_count / self.exp_total_moves

        if self.exp_total_num_shuffles == 0:
            avg_moves_per_shuffle = math.inf
        else:
            avg_moves_per_shuffle = self.exp_total_moves / self.exp_total_num_shuffles

        average_regeneration_for_init = self.exp_total_num_regenerations / EXP_1_REPEAT
        average_deadlock_count_per_setting = self.exp_total_num_shuffles / EXP_1_REPEAT
        avg_avalanche_count_per_setting = self.exp_total_avalanche_match_count / EXP_1_REPEAT

        print("Exp init")
        file_exists = os.path.isfile("plots_2/exp_game_results_1.csv")
        print(file_exists)

        with open('plots_2/exp_game_results_1.csv', 'a+', newline='') as csv_file:
            fieldnames = ['Grid Size',
                          'Max Colors',
                          'Actual Colors',
                          'Total No. of Regenerations until valid board generation',
                          'Total No. of Times Matches Occurred during init',
                          'Total No. of Deadlocks during init',
                          'Total No. of Times Game Started',
                          'Total No. of Shuffles/Deadlocks Occurred',
                          'Average No. of Moves until Shuffle occurs per game setting',
                          'Total score per Game Setting',
                          'Total Valid Moves Made',
                          'Total No. of Possible/Playable Moves',
                          'Total No. of Avalanche Matches',
                          'Total Moves Available per Game Setting',
                          'Experiment Repeat']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if not file_exists:
                print("File does not exist")
                writer.writeheader()

            writer.writerow({'Grid Size': grid_size,
                             'Max Colors': max_colors,
                             'Actual Colors': self.actual_num_colors_start,
                             'Total No. of Regenerations until valid board generation': self.exp_total_num_regenerations,
                             'Total No. of Times Matches Occurred during init': self.exp_init_invalid_match_three_count,
                             'Total No. of Deadlocks during init': self.exp_init_deadlock,
                             'Total No. of Times Game Started': self.exp_total_game_starts,
                             'Total No. of Shuffles/Deadlocks Occurred': self.exp_total_num_shuffles,
                             'Average No. of Moves until Shuffle occurs per game setting': avg_moves_per_shuffle,
                             'Total Valid Moves Made': self.exp_total_moves,
                             'Total score per Game Setting': self.exp_total_score,
                             'Total No. of Possible/Playable Moves': self.exp_total_possible_moves_count,
                             'Total No. of Avalanche Matches': self.exp_total_avalanche_match_count,
                             'Total Moves Available per Game Setting': EXP_1_NUM_OF_MOVES_PER_GAME,
                             'Experiment Repeat': EXP_1_REPEAT})

    def store_experiment_2_result(self, grid_size, max_colors):
        file_exists = os.path.isfile("exp_game_results_2.csv")
        print(file_exists)

        with open('exp_game_results_2.csv', 'a+', newline='') as csv_file:
            fieldnames = ['Grid Size',
                          'Max Colors',
                          'Actual colors',
                          'Total User Moves count',
                          'Total deterministic score',
                          'Total Avalanche count',
                          'Total non-deterministic score',
                          'Total score',
                          'Total Moves Available per Game Setting',
                          'Experiment Repeat']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if not file_exists:
                print("File does not exist")
                writer.writeheader()

            writer.writerow({'Grid Size': grid_size,
                             'Max Colors': max_colors,
                             'Actual colors': self.actual_num_colors_start,
                             'Total User Moves count': self.total_user_move_count,
                             'Total deterministic score': self.total_user_move_score,
                             'Total Avalanche count': self.total_avalanche_count,
                             'Total non-deterministic score': self.total_avalanche_score,
                             'Total score': self.exp_total_score,
                             'Total Moves Available per Game Setting': EXP_2_NUM_OF_MOVES_PER_GAME,
                             'Experiment Repeat': EXP_2_REPEAT})

    def store_experiment_3_result(self, grid_size, max_colors, selected_move):
        file_exists = os.path.isfile("exp_game_results_3.csv")
        with open('exp_game_results_3.csv', 'a+', newline='') as csv_file:
            fieldnames = ['Grid Size',
                          'Max Colors',
                          'Actual colors',
                          'Total User Moves count',
                          'Total deterministic score',
                          'Total Avalanche count',
                          'Total non-deterministic score',
                          'Total score',
                          'Selected Move',
                          'Move Score',
                          'Avalanche per selected move',
                          'Total Moves Available per Game Setting',
                          'Experiment Repeat']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()

            writer.writerow({'Grid Size': grid_size,
                             'Max Colors': max_colors,
                             'Actual colors': self.actual_num_colors_start,
                             'Total User Moves count': self.total_user_move_count,
                             'Total deterministic score': self.total_user_move_score,
                             'Total Avalanche count': self.total_avalanche_count,
                             'Total non-deterministic score': self.total_avalanche_score,
                             'Total score': self.exp_total_score,
                             'Selected Move': selected_move,
                             'Move Score': self.move_score,
                             'Avalanche per selected move': self.avalanche_per_move,
                             'Total Moves Available per Game Setting': EXP_3_NUM_OF_MOVES_PER_GAME,
                             'Experiment Repeat': EXP_3_REPEAT})
