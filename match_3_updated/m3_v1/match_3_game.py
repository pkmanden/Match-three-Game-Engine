import collections
import sys
from itertools import product

import numpy as np

from match_3_agents import *
from match_3_experiment import *

# logging.basicConfig(filename='match3.log', level=logging.DEBUG)

board_horizontal_matches = []
board_vertical_matches = []
game_mode = "normal"


class Game:

    def __init__(self, board_size, color_end):

        self.game_grid = []
        self.possible_move_positions = []
        self.score = 0
        self.color_start_range = 1
        self.color_end_range = color_end
        self.grid_size = board_size
        self.error_status = False
        self.all_coordinate_pairs = list()
        (rows, cols) = board_size
        for point in self.points_generator():
            (a, b) = point
            neighbors = [(i,j) for i,j in ((a-1,b), (a+1,b), (a,b-1), (a,b+1)) if 0<=i<rows and 0<=j<cols]
            for n in neighbors:
                self.all_coordinate_pairs.append([point, n])
        for coord in self.all_coordinate_pairs:
            [coord1, coord2] = coord
            if [coord2, coord1] and [coord1, coord2] in self.all_coordinate_pairs:
                self.all_coordinate_pairs.remove([coord2, coord1])

    def check_matches(self, board):
        # check the whole board for vertical matches and return true if match found
        for j in range(len(board[0])):
            count = 1
            for i in range(len(board) - 1):
                if board[i, j] == board[i + 1, j]:
                    count += 1
                else:
                    count = 1
                if count >= 3:
                    return True

        # check the whole board for horizontal matches and return true if match found
        for i in range(len(board)):
            count = 1
            for j in range(len(board[0]) - 1):
                if board[i, j] == board[i, j + 1]:
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
                if board[i, j] == board[i, j + 1]:
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
                if board[i, j] == board[i + 1, j]:
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

    def points_generator(self):
        """ iterates over points on the board """
        (rows, cols) = board_size
        # coord = tuple()
        points = [(i, j) for i, j in product(range(rows), range(cols))]
        # points = [Point(i, j) for i, j in product(range(rows), range(cols))]
        for point in points:
            yield point

    def find_moves(self, board):
        # function for returning possible moves in the current board
        possible_moves = list()
        co_ords = self.all_coordinate_pairs

        for co_ord in co_ords:
            [co_ord1, co_ord2] = co_ord
            board_copy = board.copy()
            board_copy[co_ord1], board_copy[co_ord2] = board_copy[co_ord2], board_copy[co_ord1]
            if self.check_matches(board_copy):
                possible_moves.append(co_ord)


        # # vertical swap and check for matches
        # for i in range(len(self.game_grid) - 1):
        #     for j in range(len(self.game_grid[0])):
        #         board_copy = self.game_grid.copy()
        #         board_copy[i][j], board_copy[i + 1][j] = board_copy[i + 1][j], board_copy[i][j]
        #         match = self.check_matches(board_copy)
        #         if match:
        #             co_ords.append([(i, j), (i + 1, j)])
        #
        # # horizontal swap and check for matches
        # for i in range(len(self.game_grid)):
        #     for j in range(len(self.game_grid[0]) - 1):
        #         board_copy = self.game_grid.copy()
        #         board_copy[i][j], board_copy[i][j + 1] = board_copy[i][j + 1], board_copy[i][j]
        #         match = self.check_matches(board_copy)
        #         if match:
        #             co_ords.append([(i, j), (i, j + 1)])

        self.possible_move_positions = possible_moves
        if game_mode == "exp":
            experiment.exp_total_possible_moves_count += len(possible_moves)
        return possible_moves

    # initialize the board with configured size and color ranges
    def init_board(self, grid_size, color_end_range):
        self.color_end_range = color_end_range
        self.grid_size = grid_size

        # generate a 2D array with values between color_start_range and color_end_range
        # value 0 is used later to show removed tiles and empty spaces on top of the grid

        self.game_grid = np.random.randint(self.color_start_range, self.color_end_range + 1, size=grid_size)

        # to consider a board as valid, below conditions are checked:
        # 1. no existing matches are present in the board
        # 2. at least one valid move is possible

        count_reinit = 0
        while self.check_matches(self.game_grid) or not self.find_moves(self.game_grid):
            # logging.debug("Generated board is invalid. Regenerating board.")
            if count_reinit < NUM_OF_DEADLOCK_RETRIES:
                # logging.debug("Regenerating attempt " + str(count_reinit + 1))
                self.game_grid = np.random.randint(self.color_start_range, self.color_end_range + 1, size=grid_size)
                # logging.debug("Generated board is \n" + str(self.game_grid))
                count_reinit += 1
                if game_mode == "exp":
                    experiment.exp_total_num_regenerations += 1
                    if self.check_matches(self.game_grid):
                        experiment.exp_init_invalid_match_three_count += 1
                    else:
                        experiment.exp_init_deadlock += 1
            else:
                # logging.debug("No valid board generated after " + str(NUM_OF_DEADLOCK_RETRIES) + " attempts. Setting skipped")
                return False

        # logging.debug("Generated board is valid after " + str(count_reinit) + " attempts . Starting game")
        # logging.debug("Starting game with board size " + str(grid_size) + " and " + str(len(np.unique(self.game_grid))) + " colors.")
        print("Starting game with board size ", grid_size, " and ", color_end_range, " colors.")
        if game_mode == "exp":
            experiment.exp_total_game_starts += 1
            # logging.debug("Cumulative regeneration count " + str(experiment.exp_total_num_regenerations) + "\n")
        return True

    # get the current board configuration
    def get_current_board(self):
        return self.game_grid

    # get all the possible moves in the current board configuration
    def get_all_possible_moves(self):
        return self.possible_move_positions

    # move coordinates for swapping
    def input_tiles(self, move):
        (coord1, coord2) = move
        is_valid_move = self.validate_move(coord1, coord2)
        if is_valid_move:
            self.swap_tiles(coord1, coord2)
        return is_valid_move

    def shuffle_board(self, board):
        if game_mode == "exp":
            experiment.exp_total_num_shuffles += 1
        board = board.ravel()
        np.random.shuffle(board)
        board = board.reshape(self.grid_size)
        return board

    def swap_tiles(self, coord1, coord2):
        # function for swapping the valid move and checking for the matches in
        # corresponding rows and columns
        # logging.debug("Board before swapping : \n" + str(self.game_grid))

        self.game_grid[coord1[0]][coord1[1]], self.game_grid[coord2[0]][coord2[1]] = self.game_grid[coord2[0]][
                                                                                         coord2[1]], \
                                                                                     self.game_grid[coord1[0]][
                                                                                         coord1[1]]
        # logging.debug("Board after swapping the tiles:\n" + str(self.game_grid))
        # print(f'Board after swapping the tiles:\n {self.game_grid}')
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
                # self.add_score(match)
                for (row, col) in match:
                    self.game_grid[row][col] = 0
                    if row in matched_cells:
                        if col not in matched_cells[row]:
                            matched_cells[row].append(col)
                    else:
                        matched_cells[row] = [col]
        if column_matches:
            for match in column_matches:
                # self.add_score(match)
                for (row, col) in match:
                    self.game_grid[row][col] = 0
                    if row in matched_cells:
                        if col not in matched_cells[row]:
                            matched_cells[row].append(col)
                    else:
                        matched_cells[row] = [col]
        # logging.debug("Matched tiles removed :\n" + str(self.game_grid))
        # print(f'Matched tiles removed\n {self.game_grid}')
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
        # print(f'Tiles above removed tiles moved down\n {self.game_grid}')
        self.distribute_new_tiles()

    def distribute_new_tiles(self):
        new_arr = np.argwhere(self.game_grid == 0)
        for i in new_arr:
            self.game_grid[i[0]][i[1]] = random.randint(self.color_start_range, self.color_end_range)
        print("Score : ", self.score)
        # logging.debug("New tiles added :\n" + str(self.game_grid))
        # print(f'New tiles added :\n {self.game_grid}')
        avalanche = self.get_matches(self.game_grid)
        if avalanche:
            if game_mode == "exp":
                experiment.exp_total_avalanche_match_count += 1
                # logging.debug("Avalanche detected. Cumulative avalanche count: " + str(experiment.exp_total_avalanche_match_count))
            self.shift_tiles(board_horizontal_matches, board_vertical_matches, param="Avalanche")

        else:
            count_reshuffle = 0
            while not self.find_moves(self.game_grid):
                if count_reshuffle < NUM_OF_DEADLOCK_RETRIES:
                    self.game_grid = self.shuffle_board(self.game_grid)
                    count_reshuffle += 1
                    # logging.debug("Deadlock detected. Attempting " + str(count_reshuffle) + "th shuffle")
                else:
                    # logging.error("No valid board after " + str(NUM_OF_DEADLOCK_RETRIES) + " shuffles.")
                    self.error_status = True
                    break

    def add_score(self, removed_tiles, param):
        unique_tiles = []
        for tile in removed_tiles:
            unique_tiles += tile
        unique_tiles = set(unique_tiles)
        self.score += len(unique_tiles)
        # logging.debug("Score for the match is " + str(len(unique_tiles)))
        if game_mode == "exp":
            if param == "UserMove":
                # experiment.total_user_move_count += 1
                # experiment.total_user_move_score += len(unique_tiles)
                experiment.first_move_user_score = len(unique_tiles)
                experiment.first_move_user_count = 1
            if param == "Avalanche":
                # experiment.total_avalanche_count += 1
                # experiment.total_avalanche_score += len(unique_tiles)
                experiment.first_move_avalanche_score = len(unique_tiles)
                experiment.first_move_avalanche_count = 1
            experiment.exp_total_score += len(unique_tiles)
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


def play(starting_board):
    moves_to_end = NUM_OF_MOVES_PER_GAME
    while moves_to_end > 0:
        # logging.debug("\tMoves left:" + str(moves_to_end))
        if moves_to_end == NUM_OF_MOVES_PER_GAME:
            game_instance.game_grid = starting_board
        current_config = game_instance.get_current_board()
        # logging.debug("Board Setting\n" + str(current_config))

        # get next move from the agent
        # agent.prepare_agent(game_instance.get_all_possible_moves())
        possible_moves = game_instance.find_moves(current_config)
        next_move = agent.select_move(current_config, possible_moves)
        # logging.debug("Selected Move " + str(next_move))
        # print(f'Selected Move :\n {next_move}')
        # check if selected move is valid
        move_validity = game_instance.input_tiles(next_move)

        if not move_validity:
            print("Invalid move.")
        else:
            if moves_to_end == NUM_OF_MOVES_PER_GAME:
                experiment.total_first_move_user_score += experiment.first_move_user_score
                experiment.total_first_move_avalanche_score += experiment.first_move_avalanche_score
                experiment.total_first_move_avalanche_count += experiment.first_move_avalanche_count
                experiment.total_first_move_user_count += experiment.first_move_user_count
            experiment.exp_total_moves += 1
            moves_to_end -= 1

        if game_instance.get_error_status():
            moves_to_end = 0


if __name__ == '__main__':
    arguments = len(sys.argv) - 1
    # if arguments < 1 or sys.argv[1] == "normal":
    game_mode = sys.argv[1]
    exp_agents = ["top-agent", "bottom-agent"]
    if game_mode == "normal":
        game_settings = [[NORMAL_BOARD_SIZE, NORMAL_COLOR_RANGE, NORMAL_REPEAT]]
        game_mode = "normal"
        # logging.debug("Normal Mode Active")
    else:
        game_settings = []
        with open('exp_game_setting.csv', newline='') as settings_file:
            settings_reader = csv.reader(settings_file)
            next(settings_reader)
            for setting in settings_reader:
                gs = setting[0].split(', ')
                game_settings.append([(int(gs[0]), int(gs[1])), int(setting[1]), EXP_REPEAT])

        # logging.debug("Experiment Mode Active")

    for each_setting in game_settings:
        if game_mode == "exp":
            print("Experiment mode")
        experiment = Experiment()
        board_size = each_setting[0]
        color_range_end = each_setting[1]
        # agent_name = each_setting[2]
        experiment_repeat = each_setting[2]
        # initialize the agent to play the game
        # logging.debug("Initializing.")
        # agent = Agent(agent_name)
        # experiment.agent = agent_name

        # initialize the game and create a game instance
        game_instance = Game(board_size, color_range_end)

        # if init_status:
        if game_mode == "exp":
            # Parallel(n_jobs=num_cores, require='sharedmem')(delayed(exp_start)() for i in range(EXP_DIFF_BOARD_REPEAT))
            for i in range(EXP_DIFF_BOARD_REPEAT):
                # logging.debug(f'Repeating i loop {i+1} of {EXP_DIFF_BOARD_REPEAT}')
                init_status = game_instance.init_board(board_size, color_range_end)
                if init_status:
                    initial_board = game_instance.get_current_board()
                    for ag in exp_agents:
                        print(f'agent : {ag}')
                        agent = Agent(ag)
                        experiment.reset_agent_metrics()
                        experiment.agent = ag
                        for j in range(EXP_SAME_BOARD_REPEAT):
                            same_board = initial_board.copy()
                            # logging.debug(f'Repeating j loop {j+1} of {EXP_SAME_BOARD_REPEAT}')
                            play(same_board)
                        experiment.store_experiment_result(board_size, color_range_end, experiment_repeat)
        else:
            init_status = game_instance.init_board(board_size, color_range_end)
            if init_status:
                board = game_instance.get_current_board()
                play(board)