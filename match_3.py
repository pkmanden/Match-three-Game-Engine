import numpy as np
import collections

def generate_board():
    board = np.random.randint(1, 4, size=(5, 5))
    # check whether the board contains any 3-matches
    if check_matches(board):
        board = generate_board()
    else:
        return board
    return board

def init_board():
    
    global game_grid
    global possible_move_positions
    
    # generate a 2D array with values between 1 and k
    # value 0 is used later to show removed tiles and empty spaces on top of the grid

    game_grid = generate_board()

    # game_grid = np.array([[1, 2, 1, 3, 2],
    #                       [2, 1, 1, 2, 1],
    #                       [1, 2, 3, 1, 1],
    #                       [1, 1, 2, 3, 3],
    #                       [2, 1, 2, 1, 3]])
    print(game_grid)

    possible_move_positions = find_moves(game_grid)

    # print("possible moves = ", possible_move_positions)

    if not possible_move_positions:
        print("No more moves possible. Shuffling...")
        game_grid = generate_board()
    else:
        print("Valid board")
        input_tiles()

        
def input_tiles():

    print("Take the swap co-ordinates")
    move = possible_move_positions.pop(0) #pop the last pair of co-ordinates from the possible moves for swap
    (coord1, coord2) = move
    print("One move taken from possible moves: ", coord1, coord2)

    is_valid_move = validate_move(coord1, coord2)
    if is_valid_move:
        print("Valid Move!")
        swap_tiles(coord1, coord2)
    else:
        print("Invalid move!!")



def find_moves(board):
    # function for checking if there is any possible move in the board
    global co_ords
    co_ords = []
    # vertical swap and check for matches
    for i in range(len(board) - 1):
        for j in range(len(board[0])):
            board_copy = board.copy()
            board_copy[i][j], board_copy[i+1][j] = board_copy[i+1][j], board_copy[i][j]
            match = check_matches(board_copy)
            if match:
                co_ords.append([(i, j), (i+1, j)])

    # horizontal swap and check for matches
    for i in range(len(board)):
        for j in range(len(board[0]) - 1):
            board_copy = board.copy()
            board_copy[i][j], board_copy[i][j+1] = board_copy[i][j+1], board_copy[i][j]
            match = check_matches(board_copy)
            if match:
                co_ords.append([(i, j), (i, j+1)])
    return co_ords

def check_matches(board):
    # function for checking all the matches in the board

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
    return False

def swap_tiles(coord1, coord2):
    # function for swapping the valid move and checking for the matches in 
    # corresponding rows and columns
    
    game_grid[coord1[0]][coord1[1]], game_grid[coord2[0]][coord2[1]] = game_grid[coord2[0]][coord2[1]], game_grid[coord1[0]][coord1[1]]
    print(game_grid)
    horizontal_matches = []
    vertical_matches = []
    if coord1[1] == coord2[1]:  # if vertical swap is performed
        for i in [coord1[0], coord2[0]]:    # check the 2 rows
            horizontal_chain = []
            for j in range(len(game_grid[0])-1):
                if (game_grid[i][j] == game_grid[i][j+1]):
                    if((i,j) not in horizontal_chain):
                        horizontal_chain.append((i, j))
                    horizontal_chain.append((i, j + 1))
                elif not horizontal_chain: 
                    continue
                else:
                    break
                if len(horizontal_chain)>=3 and horizontal_chain not in horizontal_matches:
                    horizontal_matches.append(horizontal_chain)

        vertical_chain = []
        for i in range(len(game_grid)-1):   # check the 1 column
            if (game_grid[i][coord1[1]] == game_grid[i+1][coord1[1]]):
                if ((i, coord1[1]) not in vertical_chain):
                    vertical_chain.append((i, coord1[1]))
                vertical_chain.append((i+1, coord1[1]))
            elif not vertical_chain:
                continue
            else:
                break
            if len(vertical_chain) >= 3 and vertical_chain not in vertical_matches:
                    vertical_matches.append(vertical_chain)

        # print("horizontal_matches == ", horizontal_matches)
        # print("vertical_matches == ", vertical_matches)
        shift_tiles(horizontal_matches, vertical_matches)
    
    if coord1[0] == coord2[0]: # if horizontal swap is performed
        for j in [coord1[1], coord2[1]]: #check the 2 columns
            vertical_chain = []
            for i in range(len(game_grid) - 1):
                if (game_grid[i][j] == game_grid[i+1][j]):
                    if((i,j) not in vertical_chain):
                        vertical_chain.append((i, j))
                    vertical_chain.append((i+1, j))
                elif not vertical_chain:
                    continue
                else:
                    break
                if len(vertical_chain)>=3 and vertical_chain not in vertical_matches:
                    vertical_matches.append(vertical_chain) 
        
        horizontal_chain = []
        for j in range(len(game_grid[0])-1):    #check the 1 row
            if (game_grid[coord1[0]][j] == game_grid[coord1[0]][j+1]):
                if ((coord1[0], j) not in horizontal_chain):
                    horizontal_chain.append((coord1[0], j))
                horizontal_chain.append((coord1[0],j+1))    
            elif not horizontal_chain:
                horizontal_chain.clear()
                continue
            else:
                break
            if len(horizontal_chain) >= 3 and horizontal_chain not in horizontal_matches:
                horizontal_matches.append(horizontal_chain)
                print("horizontal_matches : ", horizontal_matches)

        shift_tiles(horizontal_matches, vertical_matches)


def shift_tiles(row_matches, column_matches):
    # Function for shifting tiles above removed tiles
    matched_cells = {}
    for match in row_matches:
        for (row, col) in match:
            game_grid[row][col] = 0
            if(row in matched_cells):
                if col not in matched_cells[row]:
                    matched_cells[row].append(col)
            else:
                matched_cells[row]=[col]
    for match in column_matches:
        for (row, col) in match:
            game_grid[row][col] = 0
            if(row in matched_cells):
                if col not in matched_cells[row]:
                    matched_cells[row].append(col)
            else:
                matched_cells[row]=[col]
    print("Matched tiles removed :")
    print(game_grid)
    matched_cells = collections.OrderedDict(sorted(matched_cells.items()))

    for matched_cell in matched_cells:
        for cell in matched_cells.get(matched_cell):
            for i in range(matched_cell, -1, -1):
                if (i == 0):
                    game_grid[i][cell] = 0
                else:
                    game_grid[i][cell] = game_grid[i - 1][cell]

    print("Tiles above removed tiles moved down : \n")
    print(game_grid)

def validate_move(coord1, coord2):
    if ([coord1[0], coord1[1]], [coord2[0], coord2[1]]) or ([coord2[0], coord2[1]], [coord1[0], coord1[1]]) in possible_move_positions:
        return True

if __name__ == "__main__":
    init_board()