import random


class Agent:
    moves = []
    agent = ''
    board_config = []

    def __init__(self, agent_name):
        self.agent = agent_name

    def select_move(self, config, possible_moves):
        self.board_config = config
        available_moves = []
        # possible_moves = self.find_possible_moves(config)
        row_moves = self.find_row_moves(possible_moves)
        if not row_moves:
            available_moves = possible_moves
        else:
            available_moves = row_moves
        available_moves.sort()
        if self.agent == "random":
            move = random.choice(possible_moves)
            return move
        elif self.agent == "top-agent":
            return available_moves[0]
        elif self.agent == "bottom-agent":
            return available_moves[-1]

    def find_row_moves(self, possible_moves):
        row_moves = []
        for move in possible_moves:
            [(r1, c1), (r2, c2)] = move
            if r1 == r2:
                row_moves.append(move)
        return row_moves

    def find_possible_moves(self, config):
        # function for returning possible moves in the current board

        co_ords = []
        # vertical swap and check for matches
        for i in range(len(config) - 1):
            for j in range(len(config[0])):
                board_copy = config.copy()
                board_copy[i, j], board_copy[i + 1, j] = board_copy[i + 1, j], board_copy[i, j]
                match = self.check_matches(board_copy)
                if match:
                    co_ords.append([(i, j), (i + 1, j)])

        # horizontal swap and check for matches
        for i in range(len(config)):
            for j in range(len(config[0]) - 1):
                board_copy = config.copy()
                board_copy[i, j], board_copy[i, j + 1] = board_copy[i, j + 1], board_copy[i, j]
                match = self.check_matches(board_copy)
                if match:
                    co_ords.append([(i, j), (i, j + 1)])

        return co_ords

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
