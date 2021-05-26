from itertools import product

import gym
from gym import spaces
import match_3_game
import numpy as np

BOARD_NDIM = 2
BOARD_SIZE = (5, 5)
COLOR_RANGE = 6


class OutOfBoardError(IndexError):
    pass

class MatchThreeEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': None}
    game = match_3_game.Game()

    def points_generator(self):
        """ iterates over points on the board """
        (rows, cols) = BOARD_SIZE
        # coord = tuple()
        points = [(i, j) for i, j in product(range(rows), range(cols))]
        # points = [Point(i, j) for i, j in product(range(rows), range(cols))]
        for point in points:
            yield point

    def get_legal_actions(self, board):
        actions = list()
        rows = len(board)
        cols = len(board[0])
        for point in self.points_generator():
            (a, b) = point
            neighbors = [(i,j) for i,j in ((a-1,b), (a+1,b), (a,b-1), (a,b+1)) if 0<=i<rows and 0<=j<cols]
            for n in neighbors:
                actions.append([point, n])
        for action in actions:
            [coord1, coord2] = action
            if [coord2, coord1] and [coord1, coord2] in actions:
                actions.remove([coord2, coord1])
        action_num = [i for i in range(len(actions))]
        action_dict = dict(zip(action_num, actions))
        # print(f'legal actions : {actions} \nlen : {len(actions)}')
        return action_dict

    def __init__(self, rollout_len=100):
        super(MatchThreeEnv, self).__init__()
        self.rollout_len = rollout_len
        self.episode_counter = 0
        self.reset()
        board = self.game.get_current_board()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        # setting actions space
        self.game_actions = self.get_legal_actions(board)
        self.action_space = spaces.Discrete(len(self.game_actions))
        # self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        self.observation_space = spaces.Box(
            low=1,
            high=COLOR_RANGE,
            shape=BOARD_SIZE,
            dtype=np.int)
        print(self.observation_space)

    def step(self, action):
        valid_move = self.game.input_tiles(self.game_actions[action])
        if valid_move:
            reward = 1
        else:
            reward = 0

        # change counter even action wasn't successful
        self.episode_counter += 1
        if self.episode_counter >= self.rollout_len:
            done = True
            self.episode_counter = 0
            observation = self.reset()
        else:
            done = False
            observation = self.game.get_current_board()
        return observation, reward, done, {}

    def reset(self):
        init_status = self.game.init_board(BOARD_SIZE, COLOR_RANGE)
        observation = self.game.get_current_board()
        return observation  # reward, done, info can't be included

    def render(self, mode=None):
        print(self.game.get_current_board())

    def close(self):
        pass