import numpy as np

# game_grid = np.array([[0, 1, 0, 2, 1], [1, 2, 0, 1, 2], [2, 1, 2, 0, 0], [0, 0, 1, 2, 2], [1, 0, 1, 0, 2]])

# game_grid = `np.array([[1, 2, 3, 4], [1, 2, 1, 4], [3, 4, 1, 2]])


def generate_board():
    board = np.random.randint(4, size=(5, 5))
    # check whether the board contains any 3-matches
    if check_matches(game_grid):
        board = generate_board()
    else:
        print(board)
        return board
    return board

def init_board():
    # game_grid = generate_board()
    global game_grid
    game_grid = np.array([[0, 1, 0, 2, 1], [1, 2, 0, 1, 2], [2, 1, 2, 0, 0], [0, 0, 1, 2, 2], [1, 0, 1, 0, 2]])
    print(game_grid)
    global possible_move_positions 
    possible_move_positions = find_moves(game_grid)
    print(possible_move_positions)
    if not possible_move_positions:
        print("No more moves possible")
        game_grid = generate_board()
    else:
        print("Valid board")
        input_tiles()

        
def input_tiles():
    print("Take the swap input")

    # TODO: Take the move from user / agent

    row_1, col_1, row_2, col_2 = 1, 0, 1, 1 #hardcoded swap co-ordinates
    print("row_1, col_1, row_2, col_2: ", row_1, col_1, row_2, col_2)
    is_valid_move = validate_move(row_1, col_1, row_2, col_2)
    if is_valid_move:
        print("Valid Move!")
        swap_tiles(row_1, col_1, row_2, col_2)
    else:
        print("Invalid move!!")


def find_moves(board):
    # function for checking if there is any possible move in the board

    co_ords = []

    # vertical swap and check for matches
    for i in range(len(board) - 1):
        for j in range(len(board[0])):
            board_copy = board.copy()
            board_copy[i][j], board_copy[i+1][j] = board_copy[i+1][j], board_copy[i][j]
            match = check_matches(board_copy)
            if match:
                co_ords.append(([i, j], [i+1, j]))
    # horizontal swap and check for matches
    for i in range(len(board)):
        for j in range(len(board[0]) - 1):
            board_copy = board.copy()
            board_copy[i][j], board_copy[i][j+1] = board_copy[i][j+1], board_copy[i][j]
            match = check_matches(board_copy)
            if match:
                co_ords.append(([i, j], [i, j+1]))
    return co_ords
def check_matches(board):
    # function for checking all the matches in the board

    for j in range(len(board[0])):
        count = 1
        for i in range(len(board) - 1):
            if (board[i][j] == board[i + 1][j]):
                count += 1
            else:
                count = 1
            if (count >= 3):
                return True
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

def swap_tiles(row_1, col_1, row_2, col_2):
    game_grid[row_1][col_1], game_grid[row_2][col_2] = game_grid[row_2][col_2], game_grid[row_1][col_1]
    print(game_grid)
    if col_1 == col_2:
        if row_1 > row_2:
            row_1, row_2 = row_2, row_1
        
        count = 1
        for i in range(len(game_grid) - 1):
            # print("same column")
            
            j = col_1
            if (game_grid[i][j] == game_grid[i+1][j]):
                count += 1
            else:
                count = 1
            if count >= 3:
                print("Match found vertically1111!")

        for i in range(row_1, row_2+1):
            count = 1
            for j in range(len(game_grid[0])-1):
                if (game_grid[i][j] == game_grid[i][j+1]):
                    count += 1
                else:
                    count = 1
                if count >= 3:
                    print("Match found horizontally1111!")

    if row_1 == row_2:
        if col_1 > col_2:
            col_1, col_2 = col_2, col_1
        
        count = 1
        for j in range(len(game_grid[0]) - 1):
            # print("same column")
            
            i = row_1
            if (game_grid[i][j] == game_grid[i][j+1]):
                count += 1
            else:
                count = 1
            if count >= 3:
                print("Match found horizontally2222!")

        for j in range(col_1, col_2+1):
            count = 1
            for i in range(len(game_grid)-1):
                if (game_grid[i][j] == game_grid[i+1][j]):
                    count += 1
                else:
                    count = 1
                if count >= 3:
                    print("Match found vertically2222!")

def validate_move(row_1, col_1, row_2, col_2):
    print("moves : ", possible_move_positions[0][0])
    if ([row_1, col_1], [row_2, col_2]) or ([row_2, col_2], [row_1, col_1]) in possible_move_positions:
        return True

if __name__ == "__main__":
    init_board()