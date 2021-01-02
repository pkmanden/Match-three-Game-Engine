from match_3_experiment import *
import csv
import random
import sys
import numpy as np
import collections
from match_3_constants import *
from match_3_agents import *
import pandas as pd


logging.basicConfig(filename='match3.log', filemode='w', level=logging.INFO)

board_horizontal_matches = []
board_vertical_matches = []


class Game:
    game_grid = []
    possible_move_positions = []
    score = 0
    color_start_range = 1
    color_end_range = 5
    grid_size = 5, 5

    error_status = False

    def check_matches(self,board):
        # check the whole board for vertical matches and return true if match found
        for j in range(len(board[0])):
            count = 1
            for i in range(len(board) - 1):
                if board[i][j] == board[i + 1][j]:
                    count += 1
                else:
                    count = 1
                if count >= 3:
                    return True

        # check the whole board for horizontal matches and return true if match found
        for i in range(len(board)):
            count = 1
            for j in range(len(board[0]) - 1):
                if board[i][j] == board[i][j + 1]:
                    count += 1
                else:
                    count = 1
                if count >= 3:
                    return True

        return False

    def get_matches(self,board):
        global board_horizontal_matches
        global board_vertical_matches

        match_found_flag = False
        # function for checking all the matches in the board

        board_horizontal_matches = []
        for i in range(len(board)):
            horizontal_chain = []
            for j in range(len(board[0]) - 1):
                chain_continue_flag = False
                if board[i][j] == board[i][j + 1]:
                    if (i, j) not in horizontal_chain:
                        horizontal_chain.append((i, j))
                    horizontal_chain.append((i, j + 1))
                    chain_continue_flag = True
                if j == len(board[0]) - 2:
                    chain_continue_flag = False
                if not chain_continue_flag:
                    if len(horizontal_chain) >= 3:
                        board_horizontal_matches.append(horizontal_chain)
                        match_found_flag = True
                        break
                    else:
                        horizontal_chain.clear()

        board_vertical_matches = []
        for j in range(len(board[0])):
            vertical_chain = []
            for i in range(len(board) - 1):
                chain_continue_flag = False
                if board[i][j] == board[i + 1][j]:
                    if (i, j) not in vertical_chain:
                        vertical_chain.append((i, j))
                    vertical_chain.append((i + 1, j))
                    chain_continue_flag = True
                if i == len(board) - 2:
                    chain_continue_flag = False
                if not chain_continue_flag:
                    if len(vertical_chain) >= 3:
                        board_vertical_matches.append(vertical_chain)
                        match_found_flag = True
                        break
                    else:
                        vertical_chain.clear()

        return match_found_flag

    def find_moves(self):
        # function for checking if there is any possible move in the board

        co_ords = []
        # vertical swap and check for matches
        for i in range(len(self.game_grid) - 1):
            for j in range(len(self.game_grid[0])):
                board_copy = self.game_grid.copy()
                board_copy[i][j], board_copy[i + 1][j] = board_copy[i + 1][j], board_copy[i][j]
                match = self.check_matches(board_copy)
                if match:
                    co_ords.append([(i, j), (i + 1, j)])

        # horizontal swap and check for matches
        for i in range(len(self.game_grid)):
            for j in range(len(self.game_grid[0]) - 1):
                board_copy = self.game_grid.copy()
                board_copy[i][j], board_copy[i][j + 1] = board_copy[i][j + 1], board_copy[i][j]
                match = self.check_matches(board_copy)
                if match:
                    co_ords.append([(i, j), (i, j + 1)])

        self.possible_move_positions = co_ords
        experiment.exp_total_possible_moves_count += len(co_ords)
        return co_ords

    # initialize the board with configured size and color ranges
    def init_board(self, grid_size, color_end_range):
        self.color_end_range = color_end_range
        self.grid_size = grid_size
        # generate a 2D array with values between color_start_range and color_end_range
        # value 0 is used later to show removed tiles and empty spaces on top of the grid
        self.game_grid = np.random.randint(self.color_start_range, color_end_range, size=grid_size)
        logging.debug("Generated board is \n"+ str(self.game_grid))
        # to consider a board as valid, below conditions are checked:
        # 1. no existing matches are present in the board
        # 2. atleast one valid move is possible

        count_reinit = 0
        while self.check_matches(self.game_grid) or not self.find_moves():
            logging.info("Generated board is invalid. Regenerating board.")
            if count_reinit < NUM_OF_DEADLOCK_RETRIES:
                logging.info("Regenerating attempt " + str(count_reinit + 1))
                self.game_grid = np.random.randint(self.color_start_range, color_end_range, size=grid_size)
                logging.debug("Generated board is \n" + str(self.game_grid))
                count_reinit += 1
                experiment.exp_total_num_regenerations +=1
            else:
                logging.info("No valid board generated after "+ str(NUM_OF_DEADLOCK_RETRIES) + " attempts. Setting skipped")
                return False

        logging.info("Generated board is valid after " + str(count_reinit) + " attempts . Starting game")
        logging.info("Cumulative regeneration count " + str(experiment.exp_total_num_regenerations) + "\n")
        return True

    # get the current board configuration
    def get_current_board(self):
        return self.game_grid

    # get the current board configuration
    def get_all_possible_moves(self):
        return self.possible_move_positions

    # get the current board configuration
    def input_tiles(self, move):
        (coord1, coord2) = move
        is_valid_move = self.validate_move(coord1, coord2)
        if is_valid_move:
            self.swap_tiles(coord1, coord2)
        return is_valid_move

    def validate_board(self, board):
        # global three_matches_count
        new_board = board
        # check whether the board contains any 3-matches
        while self.check_matches(new_board):
            # three_matches_count += 1
            new_board = self.shuffle_board(new_board)
        return new_board

    def shuffle_board(self, board):
        experiment.exp_total_num_shuffles += 1
        board = board.ravel()
        np.random.shuffle(board)
        board = board.reshape(self.grid_size)
        return board

    def swap_tiles(self, coord1, coord2):
        # function for swapping the valid move and checking for the matches in
        # corresponding rows and columns

        self.game_grid[coord1[0]][coord1[1]], self.game_grid[coord2[0]][coord2[1]] = self.game_grid[coord2[0]][
                                                                                         coord2[1]], \
                                                                                     self.game_grid[coord1[0]][
                                                                                         coord1[1]]
        logging.debug("Board after swapping the tiles:\n" + str(self.game_grid))
        horizontal_matches = []
        vertical_matches = []
        if coord1[1] == coord2[1]:  # if vertical swap is performed
            for i in [coord1[0], coord2[0]]:  # check the 2 rows
                horizontal_chain = []
                for j in range(len(self.game_grid[0]) - 1):
                    chain_continue_flag = False
                    if self.game_grid[i][j] == self.game_grid[i][j + 1]:
                        if (i, j) not in horizontal_chain:
                            horizontal_chain.append((i, j))
                        horizontal_chain.append((i, j + 1))
                        chain_continue_flag = True
                    if j == len(self.game_grid[0]) - 2:
                        chain_continue_flag = False
                    if not chain_continue_flag:
                        if len(horizontal_chain) >= 3:
                            horizontal_matches.append(horizontal_chain)
                            break
                        else:
                            horizontal_chain.clear()

            vertical_chain = []
            for i in range(len(self.game_grid) - 1):  # check the 1 column
                chain_continue_flag = False
                if self.game_grid[i][coord1[1]] == self.game_grid[i + 1][coord1[1]]:
                    if (i, coord1[1]) not in vertical_chain:
                        vertical_chain.append((i, coord1[1]))
                    vertical_chain.append((i + 1, coord1[1]))
                    chain_continue_flag = True
                if i == len(self.game_grid) - 2:
                    chain_continue_flag = False
                if not chain_continue_flag:
                    if len(vertical_chain) >= 3:
                        vertical_matches.append(vertical_chain)
                        break
                    else:
                        vertical_chain.clear()

        if coord1[0] == coord2[0]:  # if horizontal swap is performed
            for j in [coord1[1], coord2[1]]:  # check the 2 columns
                vertical_chain = []
                for i in range(len(self.game_grid) - 1):
                    chain_continue_flag = False
                    if self.game_grid[i][j] == self.game_grid[i + 1][j]:
                        if (i, j) not in vertical_chain:
                            vertical_chain.append((i, j))
                        vertical_chain.append((i + 1, j))
                        chain_continue_flag = True
                    if i == len(self.game_grid) - 2:
                        chain_continue_flag = False
                    if not chain_continue_flag:
                        if len(vertical_chain) >= 3:
                            vertical_matches.append(vertical_chain)
                            break
                        else:
                            vertical_chain.clear()

            horizontal_chain = []
            for j in range(len(self.game_grid[0]) - 1):  # check the 1 row
                chain_continue_flag = False
                if self.game_grid[coord1[0]][j] == self.game_grid[coord1[0]][j + 1]:
                    if (coord1[0], j) not in horizontal_chain:
                        horizontal_chain.append((coord1[0], j))
                    horizontal_chain.append((coord1[0], j + 1))
                    chain_continue_flag = True
                if j == len(self.game_grid[0]) - 2:
                    chain_continue_flag = False
                if not chain_continue_flag:
                    if len(horizontal_chain) >= 3:
                        horizontal_matches.append(horizontal_chain)
                        break
                    else:
                        horizontal_chain.clear()
        self.shift_tiles(horizontal_matches, vertical_matches)

    # function for shifting tiles above removed tiles
    def shift_tiles(self, row_matches, column_matches):
        return_error_flag = False
        matched_cells = {}
        if row_matches:
            for match in row_matches:
                self.add_score(match)
                for (row, col) in match:
                    self.game_grid[row][col] = 0
                    if row in matched_cells:
                        if col not in matched_cells[row]:
                            matched_cells[row].append(col)
                    else:
                        matched_cells[row] = [col]
        if column_matches:
            for match in column_matches:
                self.add_score(match)
                for (row, col) in match:
                    self.game_grid[row][col] = 0
                    if row in matched_cells:
                        if col not in matched_cells[row]:
                            matched_cells[row].append(col)
                    else:
                        matched_cells[row] = [col]
        logging.debug("Matched tiles removed :\n"+str(self.game_grid))
        matched_cells = collections.OrderedDict(sorted(matched_cells.items()))

        for matched_cell in matched_cells:
            for cell in matched_cells.get(matched_cell):
                for i in range(matched_cell, -1, -1):
                    if i == 0:
                        self.game_grid[i][cell] = 0
                    else:
                        self.game_grid[i][cell] = self.game_grid[i - 1][cell]

        logging.debug("Tiles above removed tiles moved down\n"+str(self.game_grid))
        self.distribute_new_tiles()

    def distribute_new_tiles(self):
        new_arr = np.argwhere(self.game_grid == 0)
        for i in new_arr:
            self.game_grid[i[0]][i[1]] = random.randint(self.color_start_range, self.color_end_range)
        print("Score : ", self.score)

        logging.debug("New tiles added :\n" + str(self.game_grid))
        avalanche = self.get_matches(self.game_grid)
        if avalanche:
            experiment.exp_total_avalanche_match_count += 1
            logging.info("Avalanche detected. Cumulative avalanche count: " + str(experiment.exp_total_avalanche_match_count))
            print("Avalanche matches!")
            self.shift_tiles(board_horizontal_matches, board_vertical_matches)
        else:
            count_reshuffle = 0
            while not self.find_moves():
                if count_reshuffle < NUM_OF_DEADLOCK_RETRIES:
                    self.game_grid =self.shuffle_board(self.game_grid)
                    count_reshuffle += 1
                    logging.info("Deadlock detected. Attempting " + str(count_reshuffle) + "th shuffle")
                else:
                    logging.error("No valid board after " + str(NUM_OF_DEADLOCK_RETRIES) + " shuffles.")
                    self.error_status = True
                    break

    def add_score(self, removed_tiles):
        logging.info("Score for the match is "+ str(len(removed_tiles)))
        self.score += len(removed_tiles)
        experiment.exp_total_score += len(removed_tiles)
        logging.info("Game score: "+ str(self.score) + " and cumulative score: "+ str(experiment.exp_total_score ))

    def get_score(self):
        return self.score

    def validate_move(self, coord1, coord2):
        if ([coord1, coord2]) or ([coord2,coord1]) in self.possible_move_positions:
            return True
        logging.error("Invalid move.")
        return False

    def get_error_status(self):
        return self.error_status


def play():
    moves_to_end = NUM_OF_MOVES_PER_GAME
    move_validity = False
    next_move = []

    while moves_to_end > 0:
        logging.info("\tMoves left:"+ str(moves_to_end))
        current_config = game_instance.get_current_board()
        logging.debug("Board Setting\n"+str(current_config))

        # get next move from the agent
        agent.prepare_agent(game_instance.get_all_possible_moves())
        next_move = agent.select_move(current_config)
        logging.debug("Selected Move " + str(next_move))

        # check if selected move is valid
        move_validity = game_instance.input_tiles(next_move)
        if not move_validity:
            print("Invalid move.")
        else:
            experiment.exp_total_moves += 1
            moves_to_end -= 1

        if game_instance.get_error_status():
            moves_to_end = 0


arguments = len(sys.argv) - 1

if arguments < 1 or sys.argv[1] == "nor":
    game_settings = [[NORMAL_BOARD_SIZE, NORMAL_COLOR_RANGE, NORMAL_REPEAT]]
    game_mode = "nor"
    logging.debug("Normal Mode Active")

else:
    game_mode = "exp"
    game_settings = []

    with open('exp_game_results.csv', newline='') as settings_file:
        settings_reader = csv.reader(settings_file)
        next(settings_reader)
        for setting in settings_reader:
            gs = setting[0].split(', ')
            game_settings.append([(int(gs[0]), int(gs[1])), int(setting[1]), EXP_REPEAT])

    logging.info("Experiment Mode Active")

experiment = Experiment()


for each_setting in game_settings:

    experiment.experiment_reinit()
    board_size = each_setting[0]
    color_range_end = each_setting[1]
    experiment_repeat = each_setting[2]
    logging.info("Starting game with board size " + str(board_size) + " and " + str(color_range_end - 1) + " colors." )

    # initialize the agent to play the game
    logging.info("Initializing.")
    agent = Agent()

    # play for number of times configured
    for i in range(experiment_repeat):
        logging.info("\tRepeating experiment " + str(i+1) + " of " + str(experiment_repeat) + " times.")
        # initialize the game and create a game instance
        game_instance = Game()
        init_status = game_instance.init_board(board_size, color_range_end)
        if init_status:
            play()

    if game_mode == "exp":
        experiment.store_experiment_result(board_size, color_range_end - 1, experiment_repeat)