import numpy as np
import collections
import random
import time

class Game:
    score = 0
    game_grid = []
    possible_move_positions = []
    board_horizontal_matches = []
    board_vertical_matches = []

    # grid size and range of colors
    grid_size = 5, 5
    color_start_range = 1
    color_end_range = 4

    def init_board(self):
        # generate a 2D array with values between color_start_range and color_end_range
        # value 0 is used later to show removed tiles and empty spaces on top of the grid
        init_board = np.random.randint(self.color_start_range, self.color_end_range, size=self.grid_size)
        self.game_grid = self.validate_board(init_board)
        print("Generated Board : ")
        print(self.game_grid)
        self.possible_move_positions = self.get_possible_move_positions(self.game_grid)
        self.input_tiles()   

    def validate_board(self, board):
        new_board = board
        # check whether the board contains any 3-matches
        while self.check_matches(new_board, False):
            new_board = self.shuffle_board(new_board)
        return new_board

    def shuffle_board(self, board):
        board = board.ravel()
        np.random.shuffle(board)
        board = board.reshape(self.grid_size)
        return board
    
    def check_matches(self, board, get_matches_flag):
        
        # function for checking all the matches in the board
        if not get_matches_flag:
            # check the whole board for vertical matches and return true if match found
            for j in range(len(board[0])):
                count = 1
                for i in range(len(board) - 1):
                    if (board[i][j] == board[i + 1][j]):
                        count += 1
                    else:
                        count = 1
                    if (count >= 3):
                        return True

            # check the whole board for horizontal matches and return true if match found
            for i in range(len(board)):
                count = 1
                for j in range(len(board[0]) - 1):
                    if (board[i][j] == board[i][j+1]):
                        count += 1
                    else:
                        count = 1
                    if (count >= 3):
                        return True
        
        else:
            self.board_horizontal_matches = []
            for i in range(len(board)):
                
                horizontal_chain = []
                for j in range(len(board[0])-1):
                    chain_continue_flag = False
                    if (board[i][j] == board[i][j+1]):
                        if (i,j) not in horizontal_chain:
                            horizontal_chain.append((i,j))
                        horizontal_chain.append((i,j+1))
                        chain_continue_flag = True
                    if (j == len(self.game_grid[0]) - 2):
                        chain_continue_flag = False
                    if (not chain_continue_flag):
                        if len(horizontal_chain)>=3:
                            self.board_horizontal_matches.append(horizontal_chain) 
                            break
                        else:
                            horizontal_chain.clear()
            self.board_vertical_matches = []
            for j in range(len(board[0])):
                vertical_chain = []
                for i in range(len(board) - 1):
                    chain_continue_flag = False
                    if (board[i][j] == board[i+1][j]):
                        if((i,j) not in vertical_chain):
                            vertical_chain.append((i, j))
                        vertical_chain.append((i+1, j))
                        chain_continue_flag = True
                    if (i == len(board) - 2):
                        chain_continue_flag = False
                    if (not chain_continue_flag):
                        if len(vertical_chain)>=3:
                            self.board_vertical_matches.append(vertical_chain) 
                            break
                        else:
                            vertical_chain.clear()
            if (self.board_horizontal_matches or self.board_vertical_matches):
                return True

        return False

    def get_possible_move_positions(self, board):
        self.possible_move_positions = self.find_moves(board)
        while not self.possible_move_positions:
            board = self.shuffle_board(board)
            self.possible_move_positions = self.find_moves(board)
        return self.possible_move_positions

    def input_tiles(self):
        # move = self.possible_move_positions.pop() #pop the last pair of co-ordinates from the possible moves for swap
        move = random.choice(self.possible_move_positions)
        (coord1, coord2) = move
        print("One move taken from possible moves: ", coord1, coord2)
        is_valid_move = self.validate_move(coord1, coord2)
        if is_valid_move:
            self.swap_tiles(coord1, coord2)
        else:
            print("Invalid move!!")
    
    def find_moves(self, board):
        # function for checking if there is any possible move in the board
        global co_ords
        co_ords = []
        # vertical swap and check for matches
        for i in range(len(board) - 1):
            for j in range(len(board[0])):
                board_copy = board.copy()
                board_copy[i][j], board_copy[i+1][j] = board_copy[i+1][j], board_copy[i][j]
                match = self.check_matches(board_copy, False)
                if match:
                    co_ords.append([(i, j), (i+1, j)])

        # horizontal swap and check for matches
        for i in range(len(board)):
            for j in range(len(board[0]) - 1):
                board_copy = board.copy()
                board_copy[i][j], board_copy[i][j+1] = board_copy[i][j+1], board_copy[i][j]
                match = self.check_matches(board_copy, False)
                if match:
                    co_ords.append([(i, j), (i, j+1)])
        return co_ords

    def swap_tiles(self, coord1, coord2):
        # function for swapping the valid move and checking for the matches in 
        # corresponding rows and columns
        
        self.game_grid[coord1[0]][coord1[1]], self.game_grid[coord2[0]][coord2[1]] = self.game_grid[coord2[0]][coord2[1]], self.game_grid[coord1[0]][coord1[1]]
        print("Board after swapping the tiles:")
        print(self.game_grid)
        horizontal_matches = []
        vertical_matches = []
        if coord1[1] == coord2[1]:  # if vertical swap is performed
            for i in [coord1[0], coord2[0]]:    # check the 2 rows
                horizontal_chain = []
                for j in range(len(self.game_grid[0])-1):
                    chain_continue_flag = False
                    if (self.game_grid[i][j] == self.game_grid[i][j+1]):
                        if((i,j) not in horizontal_chain):
                            horizontal_chain.append((i, j))
                        horizontal_chain.append((i, j + 1))
                        chain_continue_flag = True
                    if (j == len(self.game_grid[0]) - 2):
                        chain_continue_flag = False
                    if (not chain_continue_flag):
                        if len(horizontal_chain)>=3:
                            horizontal_matches.append(horizontal_chain) 
                            break
                        else:
                            horizontal_chain.clear()

            vertical_chain = []
            for i in range(len(self.game_grid)-1):   # check the 1 column
                chain_continue_flag = False
                if (self.game_grid[i][coord1[1]] == self.game_grid[i+1][coord1[1]]):
                    if ((i, coord1[1]) not in vertical_chain):
                        vertical_chain.append((i, coord1[1]))
                    vertical_chain.append((i+1, coord1[1]))
                    chain_continue_flag = True
                if (i == len(self.game_grid) - 2):
                        chain_continue_flag = False
                if (not chain_continue_flag):
                    if len(vertical_chain)>=3:
                        vertical_matches.append(vertical_chain) 
                        break
                    else:
                        vertical_chain.clear()
        
        if coord1[0] == coord2[0]: # if horizontal swap is performed
            for j in [coord1[1], coord2[1]]: #check the 2 columns
                vertical_chain = []
                for i in range(len(self.game_grid) - 1):
                    chain_continue_flag = False
                    if (self.game_grid[i][j] == self.game_grid[i+1][j]):
                        if((i,j) not in vertical_chain):
                            vertical_chain.append((i, j))
                        vertical_chain.append((i+1, j))
                        chain_continue_flag = True
                    if (i == len(self.game_grid) - 2):
                        chain_continue_flag = False
                    if (not chain_continue_flag):
                        if len(vertical_chain)>=3:
                            vertical_matches.append(vertical_chain) 
                            break
                        else:
                            vertical_chain.clear()

            horizontal_chain = []
            for j in range(len(self.game_grid[0])-1):    #check the 1 row
                chain_continue_flag = False
                if (self.game_grid[coord1[0]][j] == self.game_grid[coord1[0]][j+1]):
                    if ((coord1[0], j) not in horizontal_chain):
                        horizontal_chain.append((coord1[0], j))
                    horizontal_chain.append((coord1[0],j+1)) 
                    chain_continue_flag = True
                if (j == len(self.game_grid[0]) - 2):
                    chain_continue_flag = False
                if (not chain_continue_flag):
                    if len(horizontal_chain)>=3:
                        horizontal_matches.append(horizontal_chain)
                        break
                    else:
                        horizontal_chain.clear()
        self.shift_tiles(horizontal_matches, vertical_matches)

    def shift_tiles(self, row_matches, column_matches):
        # Function for shifting tiles above removed tiles
        matched_cells = {}
        if row_matches:
            for match in row_matches:
                self.score = self.add_score(match)
                for (row, col) in match:
                    self.game_grid[row][col] = 0
                    if(row in matched_cells):
                        if col not in matched_cells[row]:
                            matched_cells[row].append(col)
                    else:
                        matched_cells[row]=[col]
        if column_matches:
            for match in column_matches:
                self.score = self.add_score(match)
                for (row, col) in match:
                    self.game_grid[row][col] = 0
                    if(row in matched_cells):
                        if col not in matched_cells[row]:
                            matched_cells[row].append(col)
                    else:
                        matched_cells[row]=[col]
        print("Matched tiles removed :")
        print(self.game_grid)
        matched_cells = collections.OrderedDict(sorted(matched_cells.items()))

        for matched_cell in matched_cells:
            for cell in matched_cells.get(matched_cell):
                for i in range(matched_cell, -1, -1):
                    if (i == 0):
                        self.game_grid[i][cell] = 0
                    else:
                        self.game_grid[i][cell] = self.game_grid[i - 1][cell]

        print("Tiles above removed tiles moved down :")
        print(self.game_grid)
        self.distribute_new_tiles()
        
    def distribute_new_tiles(self):
        new_arr = np.argwhere(self.game_grid == 0)
        for i in new_arr:
            self.game_grid[i[0]][i[1]] = random.randint(self.color_start_range, self.color_end_range)
        
        print("Score : ", self.score)
        print("Tiles added:")
        print(self.game_grid)
        
        avalanche = self.check_matches(self.game_grid, True)
        if avalanche:
            print("Avalanche matches!")
            self.shift_tiles(self.board_horizontal_matches, self.board_vertical_matches)
        else:
            self.game_grid = self.validate_board(self.game_grid)
            time.sleep(2)
            self.possible_move_positions = self.get_possible_move_positions(self.game_grid)
            self.input_tiles()
        
    def add_score(self, removed_tiles):
        self.score += len(removed_tiles)
        return self.score

    def validate_move(self, coord1, coord2):
        if ([coord1[0], coord1[1]], [coord2[0], coord2[1]]) or ([coord2[0], coord2[1]], [coord1[0], coord1[1]]) in self.possible_move_positions:
            return True

if __name__ == "__main__":
    g = Game()
    g.init_board()