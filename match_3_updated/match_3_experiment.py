import logging
# import time
import csv
import os
import math
from match_3_constants import *


class Experiment:

    def __init__(self):
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

    def store_experiment_result(self, grid_size, number_of_colors, experiment_repeats):

        logging.info("Cumulative game score is: " + str(self.exp_total_score))
        logging.info("Cumulative regeneration is: " + str(self.exp_total_num_regenerations))
        logging.info("Cumulative no of shuffles is: " + str(self.exp_total_num_shuffles))
        logging.info("Cumulative no of valid moves made is: " + str(self.exp_total_moves))
        logging.info("Cumulative no of possible moves: " + str(self.exp_total_possible_moves_count) + "\n")

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

        average_regeneration_for_init = self.exp_total_num_regenerations / experiment_repeats
        average_deadlock_count_per_setting = self.exp_total_num_shuffles / experiment_repeats
        avg_avalanche_count_per_setting = self.exp_total_avalanche_match_count / experiment_repeats

        logging.info("Average game score is: " + str(score_per_move))
        logging.info("Average regeneration for init: " + str(average_regeneration_for_init))
        logging.info("Average no deadlocks: " + str(average_deadlock_count_per_setting))
        logging.info("Average possible moves per configuration: " + str(avg_possible_moves_per_config))
        logging.info("Average move per shuffle: " + str(avg_moves_per_shuffle))

        print("Exp init")
        file_exists = os.path.isfile("Experiments/exp_game_results_1.csv")
        print(file_exists)

        with open('Experiments/exp_game_results_1.csv', 'a+', newline='') as csv_file:
            fieldnames = ['Grid Size',
                          'Number of Colors',
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
                             'Number of Colors': number_of_colors,
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
                             'Total Moves Available per Game Setting': NUM_OF_MOVES_PER_GAME,
                             'Experiment Repeat': EXP_REPEAT})
