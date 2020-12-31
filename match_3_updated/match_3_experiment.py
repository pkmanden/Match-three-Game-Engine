import logging
# import time
import csv
import os
import math
from match_3_constants import  *


class Experiment:

    def __init__(self):
        print("Exp init")
        file_exists = os.path.isfile("match_3_updated/exp_game_results.csv")
        print(file_exists)
        with open('exp_game_results.csv', 'w', newline='') as csv_file:
            fieldnames = ['Grid Size', 'Number of Colors',
                          'Average Number of Regenerations until valid board generation',
                          'Average Number of Moves until Shuffle occurs',
                          'Average Number of Times Deadlock Occurred',
                          'Average Score per Move',
                          'Average Number of Possible Moves per Configuration',
                          'Average Number of Avalanche matches occurred']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

    def experiment_reinit(self):
        self.exp_total_score = 0  # total score for a given setting across multiple plays
        self.exp_total_num_regenerations = 0  # count for getting total number of regenerations during init
        self.exp_total_num_shuffles = 0  # count for getting total number of shuffles
        self.exp_total_moves = 0  # count for getting average number of moves per shuffle
        #self.exp_total_deadlock_count = 0  # count of occurences of no moves
        #self.exp_total_config_count = 0  # count of total number of board configurations
        self.exp_total_possible_moves_count = 0  # count of total number of possible moves
        self.exp_total_avalanche_match_count = 0  # count the number of avalanche matches occurred

    def store_experiment_result(self, grid_size, number_of_colors, experiment_repeats):
        global NUM_OF_MOVES_PER_GAME

        logging.info("Cumulative game score is: " + str(self.exp_total_score))
        logging.info("Cumulative regeneration is: " + str(self.exp_total_num_regenerations))
        logging.info("Cumulative no of shuffles is: " + str(self.exp_total_num_shuffles))
        logging.info("Cumulative no of valid moves made is: " + str(self.exp_total_moves))
        logging.info("Cumulative no of possible moves: " + str(self.exp_total_possible_moves_count) + "\n")

        score_per_move = self.exp_total_score / (self.exp_total_moves * experiment_repeats)
        if self.exp_total_num_shuffles == 0:
            avg_moves_per_shuffle = math.inf
        else:
            avg_moves_per_shuffle = (NUM_OF_MOVES_PER_GAME * experiment_repeats) / self.exp_total_num_shuffles

        average_regeneration_for_init = self.exp_total_num_regenerations / experiment_repeats
        average_deadlock_count = self.exp_total_num_shuffles / experiment_repeats

        avg_possible_moves_per_config = self.exp_total_possible_moves_count / (NUM_OF_MOVES_PER_GAME * experiment_repeats)

        print("avg_moves_per_shuffle : ", avg_moves_per_shuffle)
        print("score_per_move : ", score_per_move )
        #    print("avg_move_per_config", avg_move_per_config)

        logging.info("Average game score is: " + str(score_per_move))
        logging.info("Average regeneration for init: " + str(average_regeneration_for_init))
        logging.info("Average no deadlocks: " + str(average_deadlock_count))
        logging.info("Average possible moves per configuration: " + str(avg_possible_moves_per_config))
        logging.info("Average move per shuffle: " + str(avg_moves_per_shuffle))

        with open('match_3_updated/exp_game_results.csv', 'a+',  newline='') as csv_file:
            fieldnames = ['Grid Size', 'Number of Colors',
                          'Average Number of Regenerations until valid board generation',
                          'Average Number of Moves until Shuffle occurs',
                          'Average Number of Times Deadlock Occurred',
                          'Average Score per Move',
                          'Average Number of Possible Moves per Configuration',
                          'Average Number of Avalanche matches occurred']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'Grid Size': grid_size,
                             'Number of Colors': number_of_colors,
                             'Average Number of Regenerations until valid board generation': average_regeneration_for_init,
                             'Average Number of Moves until Shuffle occurs': avg_moves_per_shuffle,
                             'Average Number of Times Deadlock Occurred': average_deadlock_count,
                             'Average Score per Move': score_per_move,
                             'Average Number of Possible Moves per Configuration': avg_possible_moves_per_config,
                             'Average Number of Avalanche matches occurred': self.exp_total_avalanche_match_count / experiment_repeats})

