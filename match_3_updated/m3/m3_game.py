import csv
import os

from m3_globals import *
import numpy as np
import collections
import random
import time

#
# import builtins
#
# def print(*str):
#     pass


class GameStats:

    def __init__(self,grid_size, color_end):
        self.color_end = color_end
        self.grid_size = grid_size
        self.stat_init_matched_count = 0
        self.stat_init_deadlock_count = 0
        self.stat_init_regen_count = 0
        self.stat_init_regen_count = 0
        self.reinit()

    def reinit(self):
        #self.stat_init_matched_count = 0
        #self.stat_init_deadlock_count = 0
        #self.stat_init_regen_count = 0

        self.stat_firstmove_nondetscore = 0
        self.stat_firstmove_detscore = 0
        self.stat_firstmove_avalanche_count = 0

        self.stat_valid_moves_made = 0
        self.stat_game_score = 0
        self.stat_move_score = 0
        self.stat_total_deadlock_count = 0
        self.stat_total_avalanche_count = 0
        self.stat_total_possible_moves = 0
        self.stat_game_move_time = 0
        self.stat_game_init_time = 0

        self.stat_gameplay_status= "NoStart"

    def print_stats(self):
        print(f'InitMatchedCount: {self.stat_init_matched_count}')
        print(f'InitDeadLockCount: {self.stat_init_deadlock_count}')
        print(f'InitRegenCount: {self.stat_init_regen_count}')
        print(f'FirstMoveNonDetScore: {self.stat_firstmove_nondetscore}')
        print(f'FirstMoveDetScore: {self.stat_firstmove_detscore}')
        print(f'FirstMoveAvalanche: {self.stat_firstmove_avalanche_count}')
        print(f'ValidMovesMade: {self.stat_valid_moves_made}')
        print(f'GameScore: {self.stat_game_score}')
        print(f'DeadlockCount: {self.stat_total_deadlock_count}')
        print(f'AvalancheCount: {self.stat_total_avalanche_count}')
        print(f'TotalPossibleMoves: {self.stat_total_possible_moves}')
        print(f'LastMoveStatus: {self.stat_gameplay_status}')
        print(f'GameInitTime: {self.stat_game_init_time}')
        print(f'GameMoveTime: {self.stat_game_move_time}')

    def write_csv(self, agent):
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
                          'Total avalanche count after first move']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exists:
                print("File does not exist")
                writer.writeheader()


            writer.writerow({
                    'Agent': agent,
                    'Grid Size': self.grid_size,
                    'Number of Colors': self.color_end,
                    'Total No. of Regenerations until valid board generation': self.stat_init_regen_count,
                    'Total No. of Times Matches Occurred during init': self.stat_init_matched_count,
                    'Total No. of Deadlocks during init': self.stat_init_deadlock_count,
                    'Total No. of Shuffles/Deadlocks Occurred': self.stat_total_deadlock_count,
                    'Total Valid Moves Made': self.stat_valid_moves_made,
                    'Total score per Game Setting': self.stat_game_score,
                    'Total No. of Possible/Playable Moves': self.stat_total_possible_moves,
                    'Total No. of Avalanche Matches': self.stat_total_avalanche_count,
                    'Total Moves Available per Game Setting': NUM_OF_MOVES_PER_GAME,
                    'Total deterministic score after first move': self.stat_firstmove_detscore,
                    'Total non-deterministic score after first move': self.stat_firstmove_nondetscore,
                    'Total avalanche count after first move': self.stat_firstmove_avalanche_count
                })


class Game:
    board_horizontal_matches = []
    board_vertical_matches = []

    def __init__(self, grid_size, color_end):
        self.game_stats=GameStats(grid_size, color_end)
        self.color_start = 1
        self.color_end = color_end
        self.grid_size = grid_size
        self.possible_move_positions = []
        self.first_move_flag = True
        # self.game_grid = np.random.randint(self.color_start, self.color_end + 1, size=self.grid_size)

    def init_board(self):

        # generate a 2D array with values between color_start and color_end
        # value 0 is used later to show removed tiles and empty spaces on top of the grid

        self.game_grid = np.random.randint(self.color_start, self.color_end + 1, size=self.grid_size)
        # to consider a board as valid, below conditions are checked:
        # 1. no existing matches are present in the board
        # 2. at least one valid move is possible

        count_reinit = 0

        while self.__check_matches(self.game_grid) or not self.find_moves():
            if count_reinit < NUM_OF_DEADLOCK_RETRIES:
                print("Reiniting board")
                self.game_grid = np.random.randint(self.color_start, self.color_end + 1, size=self.grid_size)
                count_reinit += 1

                if self.__check_matches(self.game_grid):
                    self.game_stats.stat_init_matched_count += 1
                else:
                    self.game_stats.stat_init_deadlock_count += 1

                self.game_stats.stat_init_regen_count += 1

            else:
                return self.game_stats

        self.game_stats.stat_gameplay_status = "Start"
        print("Starting game with board size ", self.grid_size, " and ", self.color_end, " colors.")
        print(self.game_grid)

        return self.game_stats

    def reinit_board(self, board, moves):
        self.game_grid = board
        self.game_stats.reinit()
        self.possible_move_positions = moves
        self.first_move_flag = True

    def get_board(self):
        return self.game_grid

    def play_move(self):
        pass

    def move_helper(self):
        return self.possible_move_positions

    def get_stats(self):
        return self.game_stats

    def get_score(self):
        return self.game_stats.stat_game_score

    def get_move_score(self):
        return self.game_stats.stat_move_score

    def __swap(self):
        pass

    # move coordinates for swapping
    def input_tiles(self, move):
        (coord1, coord2) = move
        is_valid_move = self.validate_move(coord1, coord2)

        if is_valid_move:
            self.game_stats.stat_gameplay_status = "Valid"
            self.__swap_tiles(coord1, coord2)
            self.first_move_flag = False
            self.game_stats.stat_valid_moves_made += 1
        else:
            print("Invalid move. Please try again")
            self.game_stats.stat_gameplay_status = "Invalid"

    def shuffle_board(self, board):
        self.game_stats.stat_total_deadlock_count += 1
        board = board.ravel()
        np.random.shuffle(board)
        board = board.reshape(self.grid_size)
        return board

    def __swap_tiles(self, coord1, coord2):
        # function for swapping the valid move and checking for the matches in
        # corresponding rows and columns
        # logging.debug("Board before swapping : \n" + str(self.game_grid))

        self.game_grid[coord1[0]][coord1[1]], self.game_grid[coord2[0]][coord2[1]] = self.game_grid[coord2[0]][
                                                                                         coord2[1]], \
                                                                                     self.game_grid[coord1[0]][
                                                                                         coord1[1]]
        # logging.debug("Board after swapping the tiles:\n" + str(self.game_grid))
        print(f'Board after swapping the tiles:\n {self.game_grid}')
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
        self.__shift_tiles(horizontal_matches, vertical_matches, param="UserMove")

    # function for shifting tiles above removed tiles
    def __shift_tiles(self, row_matches, column_matches, param):
        matched_cells = {}
        total_matches = row_matches + column_matches
        self.__add_score(total_matches, param)
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
        print(f'Matched tiles removed\n {self.game_grid}')
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
        print(f'Tiles above removed tiles moved down\n {self.game_grid}')
        self.__distribute_new_tiles()

    def __distribute_new_tiles(self):
        new_arr = np.argwhere(self.game_grid == 0)
        for i in new_arr:
            self.game_grid[i[0]][i[1]] = random.randint(self.color_start, self.color_end)
        print("Score : ", self.game_stats.stat_game_score)
        # logging.debug("New tiles added :\n" + str(self.game_grid))
        print(f'New tiles added :\n {self.game_grid}')
        avalanche = self.get_matches(self.game_grid)
        if avalanche:
            self.game_stats.stat_total_avalanche_count += 1
            self.__shift_tiles(board_horizontal_matches, board_vertical_matches, param="Avalanche")

        else:
            count_reshuffle = 0
            while not self.find_moves():
                if count_reshuffle < NUM_OF_DEADLOCK_RETRIES:
                    self.game_grid = self.shuffle_board(self.game_grid)
                    count_reshuffle += 1
                    # logging.debug("Deadlock detected. Attempting " + str(count_reshuffle) + "th shuffle")
                else:
                    # logging.error("No valid board after " + str(NUM_OF_DEADLOCK_RETRIES) + " shuffles.")
                    self.game_stats.stat_gameplay_status = "Error"
                    break

    def __add_score(self, removed_tiles, param):
        unique_tiles = []
        for tile in removed_tiles:
            unique_tiles += tile
        unique_tiles = set(unique_tiles)
        self.game_stats.stat_game_score += len(unique_tiles)
        # logging.debug("Score for the match is " + str(len(unique_tiles)))
        if param == "UserMove":
            self.game_stats.stat_move_score = len(unique_tiles)
        if param == "Avalanche":
            self.game_stats.stat_move_score += len(unique_tiles)

        if self.first_move_flag:
            if param == "UserMove":
                self.game_stats.stat_firstmove_detscore += len(unique_tiles)
            if param == "Avalanche":
                self.game_stats.stat_firstmove_nondetscore += len(unique_tiles)
                self.game_stats.stat_firstmove_avalanche_count += 1

    def validate_move(self, coord1, coord2):
        # if ([coord1, coord2]) or ([coord2, coord1]) in self.possible_move_positions:
        if any(c in self.possible_move_positions for c in ([coord1, coord2], [coord2, coord1])):
            return True
        # logging.error("Invalid move.")
        return False

    def __check_matches(self,board):
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

    def find_moves(self):
        # function for returning possible moves in the current board

        co_ords = []
        # vertical swap and check for matches
        for i in range(len(self.game_grid) - 1):
            for j in range(len(self.game_grid[0])):
                board_copy = self.game_grid.copy()
                board_copy[i][j], board_copy[i + 1][j] = board_copy[i + 1][j], board_copy[i][j]
                match = self.__check_matches(board_copy)
                if match:
                    co_ords.append([(i, j), (i + 1, j)])

        # horizontal swap and check for matches
        for i in range(len(self.game_grid)):
            for j in range(len(self.game_grid[0]) - 1):
                board_copy = self.game_grid.copy()
                board_copy[i][j], board_copy[i][j + 1] = board_copy[i][j + 1], board_copy[i][j]
                match = self.__check_matches(board_copy)
                if match:
                    co_ords.append([(i, j), (i, j + 1)])

        self.possible_move_positions = co_ords
        self.game_stats.stat_total_possible_moves += len(co_ords)
        return co_ords

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
