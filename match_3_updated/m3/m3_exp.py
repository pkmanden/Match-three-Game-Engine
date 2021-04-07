import csv
import os

from m3_game import *
import pprint

class ExpStatus:
    def __init__(self, agent_type):
        self.agent_type = agent_type
        self.consolidated_result = {}

    def consolidate_result(self, gamestats):

        current_key = (gamestats.grid_size, gamestats.color_end)

        if current_key in self.consolidated_result.keys():
            self.consolidated_result[current_key]['stat_init_matched_count'] += gamestats.stat_init_matched_count
            self.consolidated_result[current_key]['stat_init_deadlock_count'] += gamestats.stat_init_deadlock_count
            self.consolidated_result[current_key]['stat_init_regen_count'] += gamestats.stat_init_regen_count
            self.consolidated_result[current_key]['stat_firstmove_nondetscore'] += gamestats.stat_firstmove_nondetscore
            self.consolidated_result[current_key]['stat_firstmove_detscore'] += gamestats.stat_firstmove_detscore
            self.consolidated_result[current_key]['stat_firstmove_avalanche_count'] += gamestats.stat_firstmove_avalanche_count
            self.consolidated_result[current_key]['stat_valid_moves_made'] += gamestats.stat_valid_moves_made
            self.consolidated_result[current_key]['stat_game_score'] += gamestats.stat_game_score
            self.consolidated_result[current_key]['stat_total_deadlock_count'] += gamestats.stat_total_deadlock_count
            self.consolidated_result[current_key]['stat_total_avalanche_count'] += gamestats.stat_total_avalanche_count
            self.consolidated_result[current_key]['stat_total_possible_moves'] += gamestats.stat_total_possible_moves
            self.consolidated_result[current_key]['stat_game_init_time'] += gamestats.stat_game_init_time
            self.consolidated_result[current_key]['stat_game_move_time'] += gamestats.stat_game_move_time

        else:
            self.consolidated_result[current_key] =  {
            'stat_init_matched_count' : gamestats.stat_init_matched_count,
            'stat_init_deadlock_count': gamestats.stat_init_deadlock_count,
            'stat_init_regen_count': gamestats.stat_init_regen_count,
            'stat_firstmove_nondetscore': gamestats.stat_firstmove_nondetscore,
            'stat_firstmove_detscore': gamestats.stat_firstmove_detscore,
            'stat_firstmove_avalanche_count': gamestats.stat_firstmove_avalanche_count,
            'stat_valid_moves_made': gamestats.stat_valid_moves_made,
            'stat_game_score': gamestats.stat_game_score,
            'stat_total_deadlock_count': gamestats.stat_total_deadlock_count,
            'stat_total_avalanche_count': gamestats.stat_total_avalanche_count,
            'stat_total_possible_moves': gamestats.stat_total_possible_moves,
            'stat_game_move_time':  gamestats.stat_game_move_time,
            'stat_game_init_time':  gamestats.stat_game_init_time
            }

    #For a given grid size, over 20 moves, over 50 games with same board, repeated 200 times


    def pretty_print(self):
        print(f'Agent type {self.agent_type}')
        pprint.pprint(self.consolidated_result)


    def write_csv(self):
        file_exists = os.path.isfile("exp_results.csv")
        with open('exp_results.csv', 'a+', newline='') as csv_file:
            fieldnames = ['Agent',
                          'Grid Size',
                          'Number of Colors',
                          'Total No. of Regenerations until valid board generation',
                          'Total No. of Times Matches Occurred during init',
                          'Total No. of Deadlocks during init',
                          'Total No. of Shuffles/Deadlocks Occurred',
                          'Total score per Game Setting',
                          'Total Valid Moves Made',
                          'Total No. of Possible/Playable Moves',
                          'Total No. of Avalanche Matches',
                          'Total Moves Available per Game Setting',
                          'Total deterministic score after first move',
                          'Total non-deterministic score after first move',
                          'Total avalanche count after first move',
                          'Init Time',
                          'Move Time']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exists:
                print("File does not exist")
                writer.writeheader()

            for key in self.consolidated_result:
                writer.writerow({
                 'Agent': self.agent_type,
                 'Grid Size': key[0],
                 'Number of Colors': key[1],
                 'Total No. of Regenerations until valid board generation': self.consolidated_result[key]['stat_init_regen_count'],
                 'Total No. of Times Matches Occurred during init': self.consolidated_result[key]['stat_init_matched_count'],
                 'Total No. of Deadlocks during init': self.consolidated_result[key]['stat_init_deadlock_count'],
                 'Total No. of Shuffles/Deadlocks Occurred': self.consolidated_result[key]['stat_total_deadlock_count'],
                 'Total Valid Moves Made': self.consolidated_result[key]['stat_valid_moves_made'],
                 'Total score per Game Setting': self.consolidated_result[key]['stat_game_score'],
                 'Total No. of Possible/Playable Moves': self.consolidated_result[key]['stat_total_possible_moves'],
                 'Total No. of Avalanche Matches': self.consolidated_result[key]['stat_total_avalanche_count'],
                 'Total Moves Available per Game Setting': NUM_OF_MOVES_PER_GAME,
                 'Total deterministic score after first move': self.consolidated_result[key]['stat_firstmove_detscore'],
                 'Total non-deterministic score after first move': self.consolidated_result[key]['stat_firstmove_nondetscore'],
                 'Total avalanche count after first move': self.consolidated_result[key]['stat_firstmove_avalanche_count'],
                 'Init Time': self.consolidated_result[key]['stat_game_init_time'],
                 'Move Time': self.consolidated_result[key]['stat_game_move_time']
                                 })
