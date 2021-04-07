import random


class Agent:
    possible_moves = []
    sorted_moves = []

    def __init__(self,agent_type):
        self.agent_type = agent_type

        if agent_type == "top_agent":
            self.agent = TopAgent()
        if agent_type == "bottom_agent":
            self.agent = BottomAgent()
        if agent_type == "random_agent":
            self.agent = RandomAgent()
        if agent_type == "human":
            self.agent = HumanAgent()

    def select_move(self, config):
        selected_move = self.agent.select_move(config)
        return selected_move

    def give_help(self, current_available_moves):
        global possible_moves
        possible_moves = current_available_moves

    def get_type(self):
        return self.agent_type

    def find_row_moves(self, possible_moves):
        row_moves = []
        global sorted_moves
        sorted_moves = []
        for move in possible_moves:
            [(r1, c1), (r2, c2)] = move
            if r1 == r2:
                row_moves.append(move)
        if not row_moves:
            sorted_moves = possible_moves
        else:
            sorted_moves = row_moves
        sorted_moves.sort()


class TopAgent():
    def select_move(self, config):
        global sorted_mo
        return sorted_moves[0]


class BottomAgent():
    def select_move(self, config):
        return sorted_moves[-1]


class RandomAgent():
    def select_move(self, config):
        move = random.choice(possible_moves)
        return move


class HumanAgent():
    def select_move(self, config):
        print('Current Board Input is')
        print(config)

        tile1 = input('Enter the first tile co_ordinates (E.g. 0,0): ')
        tile2 = input('Enter the second tile co_ordinates (E.g. 0,0): ')

        tile1_cord = tile1.split(',')
        tile2_cord = tile2.split(',')

        move = [(int(tile1_cord[0]),int(tile1_cord[1])),(int(tile2_cord[0]),int(tile2_cord[1]))]
        print(move)

        return move
