from joblib import Parallel, delayed

from match_3_experiment import *
import csv
import sys
import numpy as np
import random
import collections
from match_3_constants_exp_2 import *
from match_3_agents_exp_2 import *

# logging.basicConfig(filename='match_3_experiment_3.log', filemode='w', level=logging.DEBUG)

board_horizontal_matches = []
board_vertical_matches = []

# logging.info("Board Size |  Max.No. of Colors   |   Actual No. of Colors   |   Total User Moves count   |   Total deterministic score    |   Total Avalanche count   |   Total non-deterministic score  |   Total score")



# def log_stages(stage, size, max_num_colors, actual_num_colors, action, score=0):
#
#     logging.info(str(stage) + "|" + str(size) + "|" + str(max_num_colors) + "|" + str(actual_num_colors) + "|" + str(action) + "|" + str(score))


class Game:
    game_grid = []
    possible_move_positions = []
    score = 0
    color_start_range = 1
    color_end_range = 5
    grid_size = 5, 5


    error_status = False

    def check_matches(self, board):
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

    def get_matches(self, board):
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
        # function for returning possible moves in the current board

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

    # def generate_random_board(self):
    #     m, n = self.grid_size
    #     # print("total tiles : ", m * n)
    #     total_tiles = m * n
    #     temp_board_1 = np.arange(self.color_start_range, self.color_end_range + 1)
    #     # print("temp_board_1: ", temp_board_1)
    #     temp_board_2 = np.random.randint(self.color_start_range, self.color_end_range + 1, size=(total_tiles - len(temp_board_1)))
    #     # print("temp_board_2: ", temp_board_2)
    #     board = np.concatenate((temp_board_1, temp_board_2), axis=None)
    #     np.random.shuffle(board)
    #     board = board.reshape(self.grid_size)
    #     return board

    # initialize the board with configured size and color ranges
    def init_board(self, grid_size, color_end_range):
        # np.random.seed(0)
        r = np.random.RandomState(1234)
        self.color_end_range = color_end_range
        self.grid_size = grid_size
        # generate a 2D array with values between color_start_range and color_end_range
        # value 0 is used later to show removed tiles and empty spaces on top of the grid

        # self.game_grid = self.generate_random_board()
        self.game_grid = r.randint(self.color_start_range, self.color_end_range + 1, size=grid_size)

        # logging.debug("Generated board is \n" + str(self.game_grid))

        # to consider a board as valid, below conditions are checked:
        # 1. no existing matches are present in the board
        # 2. at least one valid move is possible

        count_reinit = 0
        while self.check_matches(self.game_grid) or not self.find_moves():
            # logging.debug("Generated board is invalid. Regenerating board.")
            if count_reinit < NUM_OF_DEADLOCK_RETRIES:
                # logging.debug("Regenerating attempt " + str(count_reinit + 1))
                self.game_grid = r.randint(self.color_start_range, self.color_end_range + 1, size=grid_size)
                # self.game_grid = self.generate_random_board()
                # logging.debug("Generated board is \n" + str(self.game_grid))
                count_reinit += 1
                # log_stages("Init", grid_size, len(np.unique(self.game_grid)), "Regenerate")
                experiment.exp_total_num_regenerations += 1
                if self.check_matches(self.game_grid):
                    experiment.exp_init_invalid_match_three_count += 1
                    # log_stages("Init", grid_size, len(np.unique(self.game_grid)), "Matches")
                else:
                    experiment.exp_init_deadlock += 1
                    # log_stages("Init", grid_size, len(np.unique(self.game_grid)), "Deadlock")
            else:
                # logging.debug("No valid board generated after " + str(NUM_OF_DEADLOCK_RETRIES) + " attempts. Setting skipped")
                return False

        # logging.debug("Generated board is valid after " + str(count_reinit) + " attempts . Starting game")
        # logging.debug("Starting game with board size " + str(board_size) + " and " + str(len(np.unique(self.game_grid))) + " colors.")
        print("Starting game with board size ", board_size, " and ", len(np.unique(self.game_grid)), " colors.")
        # print("Board: \n", self.game_grid)
        # log_stages("Init", grid_size, len(np.unique(self.game_grid)), "Start")
        experiment.exp_total_game_starts += 1
        # logging.debug("Cumulative regeneration count " + str(experiment.exp_total_num_regenerations) + "\n")
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
        # logging.debug("Board after swapping the tiles:\n" + str(self.game_grid))
        # print("Board after swapping the tiles:\n", self.game_grid)
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
        self.shift_tiles(horizontal_matches, vertical_matches, param="UserMove")

    # function for shifting tiles above removed tiles
    def shift_tiles(self, row_matches, column_matches, param):
        return_error_flag = False
        matched_cells = {}
        total_matches = row_matches + column_matches
        self.add_score(total_matches, param)
        if row_matches:
            for match in row_matches:
                # self.add_score(match, param)
                for (row, col) in match:
                    self.game_grid[row][col] = 0
                    if row in matched_cells:
                        if col not in matched_cells[row]:
                            matched_cells[row].append(col)
                    else:
                        matched_cells[row] = [col]
        if column_matches:
            for match in column_matches:
                # self.add_score(match, param)
                for (row, col) in match:
                    self.game_grid[row][col] = 0
                    if row in matched_cells:
                        if col not in matched_cells[row]:
                            matched_cells[row].append(col)
                    else:
                        matched_cells[row] = [col]
        # logging.debug("Matched tiles removed :\n" + str(self.game_grid))

        matched_cells = collections.OrderedDict(sorted(matched_cells.items()))

        for matched_cell in matched_cells:
            for cell in matched_cells.get(matched_cell):
                for i in range(matched_cell, -1, -1):
                    if i == 0:
                        self.game_grid[i][cell] = 0
                    else:
                        self.game_grid[i][cell] = self.game_grid[i - 1][cell]

        # logging.debug("Tiles above removed tiles moved down\n" + str(self.game_grid))
        # logging.debug("Score Updated:" + str(self.score))
        self.distribute_new_tiles()

    def distribute_new_tiles(self):
        new_arr = np.argwhere(self.game_grid == 0)
        for i in new_arr:
            self.game_grid[i[0]][i[1]] = random.randint(self.color_start_range, self.color_end_range)
        print("Score : ", self.score)
        # logging.debug("New tiles added :\n" + str(self.game_grid))
        # print("New Board : \n", self.game_grid)
        # log_stages("Game", self.grid_size, len(np.unique(self.game_grid)), param, score=self.score)

        avalanche = self.get_matches(self.game_grid)
        if avalanche:
            experiment.exp_total_avalanche_match_count += 1
            # logging.debug("Avalanche detected. Cumulative avalanche count: " + str(
            #     experiment.exp_total_avalanche_match_count))
            # print("Avalanche matches!")
            self.shift_tiles(board_horizontal_matches, board_vertical_matches, param="Avalanche")

        else:
            count_reshuffle = 0
            while not self.find_moves():
                if count_reshuffle < NUM_OF_DEADLOCK_RETRIES:
                    self.game_grid = self.shuffle_board(self.game_grid)
                    count_reshuffle += 1
                    # logging.debug("Deadlock detected. Attempting " + str(count_reshuffle) + "th shuffle")
                    # log_stages("Game", self.grid_size, len(np.unique(self.game_grid)), "Deadlock", score=self.score)
                    # print("Deadlock detected. Attempting ", count_reshuffle, "th shuffle.")
                else:
                    # logging.error("No valid board after " + str(NUM_OF_DEADLOCK_RETRIES) + " shuffles.")
                    self.error_status = True
                    break


    def add_score(self, removed_tiles, param):
        # logging.debug("Score for the match is " + str(len(removed_tiles)))
        # print(removed_tiles)
        if param == "UserMove":
            experiment.total_user_move_count += 1
        if param == "Avalanche":
            experiment.total_avalanche_count += 1
        # move_score = 0
        for match in removed_tiles:
            self.score += len(match)
            if param == "UserMove":
                experiment.total_user_move_score += len(match)
            if param == "Avalanche":
                experiment.total_avalanche_score += len(match)
            experiment.exp_total_score += len(match)
            # logging.debug("Game score: "+ str(self.score) + " and cumulative score: "+ str(experiment.exp_total_score))

    def get_score(self):
        return self.score

    def validate_move(self, coord1, coord2):
        if ([coord1, coord2]) or ([coord2, coord1]) in self.possible_move_positions:
            return True
        # logging.error("Invalid move.")
        return False

    def get_error_status(self):
        return self.error_status


actual_num_colors_start = 0


def play():
    # initialize the game and create a game instance
    game_instance = Game()
    init_status = game_instance.init_board(board_size, color_range_end)
    if init_status:
        # ============== Change for experiment 2=============
        global actual_num_colors_start
        actual_num_colors_start = len(np.unique(game_instance.game_grid))
        # print("Actual colors start : ", len(np.unique(game_instance.game_grid)))
        # move = game_instance.get_all_possible_moves()[0]
        # print("Selected Move : ", move)
        #
        # game_instance.input_tiles(move)
        # logging.info("Game Ended. Score : " + str(game_instance.score))
        # ============== === === === === === == ============
        moves_to_end = NUM_OF_MOVES_PER_GAME
        move_validity = False
        next_move = []

        while moves_to_end > 0:
            # logging.debug("\tMoves left:" + str(moves_to_end))
            current_config = game_instance.get_current_board()
            # logging.debug("Board Setting\n" + str(current_config))

            # get next move from the agent
            agent.prepare_agent(game_instance.get_all_possible_moves())
            next_move = agent.select_move(current_config)
            # logging.debug("Selected Move " + str(next_move))

            # check if selected move is valid
            move_validity = game_instance.input_tiles(next_move)
            if not move_validity:
                print("Invalid move.")
            else:
                experiment.exp_total_moves += 1
                moves_to_end -= 1

            if game_instance.get_error_status():
                moves_to_end = 0


# arguments = len(sys.argv) - 1
#
# if arguments < 1 or sys.argv[1] == "nor":
#     game_settings = [[NORMAL_BOARD_SIZE, NORMAL_COLOR_RANGE, NORMAL_REPEAT]]
#     game_mode = "nor"
#     # logging.debug("Normal Mode Active")

# else:
game_settings = []
with open('exp_2_game_setting.csv', newline='') as settings_file:
    settings_reader = csv.reader(settings_file)
    next(settings_reader)
    for setting in settings_reader:
        gs = setting[0].split(', ')
        game_settings.append([(int(gs[0]), int(gs[1])), int(setting[1]), EXP_REPEAT])

# logging.debug("Experiment Mode Active")

for each_setting in game_settings:
    user_move_count = 0
    avalanche_count = 0
    experiment = Experiment()

    board_size = each_setting[0]
    color_range_end = each_setting[1]
    experiment_repeat = each_setting[2]
    # initialize the agent to play the game
    # logging.debug("Initializing.")
    agent = Agent()

    # play for number of times configured
    Parallel(n_jobs=2, require='sharedmem')(delayed(play)() for i in range(experiment_repeat))
    # for i in range(experiment_repeat):
    #     play()
    # logging.debug("\tRepeating experiment " + str(i + 1) + " of " + str(experiment_repeat) + " times.")
    # logging.info(str(board_size) + "|" + str(color_range_end) + "|" + str(actual_num_colors_start) + "|" + str(experiment.total_user_move_count) + "|" + str(experiment.total_user_move_score) + "|" + str(experiment.total_avalanche_count) + "|" + str(experiment.total_avalanche_score) + "|" + str(experiment.exp_total_score))
    # log_stages("Game", board_size, color_range_end, len(np.unique(game_instance.game_grid)), score=move_score)

    experiment.store_experiment_2_result(board_size, color_range_end, actual_num_colors_start)
