import random


class Agent:
    moves = []
    game_board = []

    current_solution = []

    def prepare_agent(self, solution):
        self.current_solution = solution

    def select_move(self, config):
        move = random.choice(self.current_solution)
        return move

