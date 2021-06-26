from itertools import product

import gym
from gym import spaces
import m3_game
from m3_globals import *
import numpy as np


class MatchThreeEnv(gym.Env):
    # Custom Environment that follows gym interface
    metadata = {'render.modes': None}
    game = m3_game.Game(BOARD_SIZE, COLOR_END)

    def points_generator(self):
        # iterates over points on the board
        (rows, cols) = BOARD_SIZE
        points = [(i, j) for i, j in product(range(rows), range(cols))]
        for point in points:
            yield point

    def get_legal_actions(self, board):
        actions = list()
        rows = len(board)
        cols = len(board[0])
        for point in self.points_generator():
            (a, b) = point
            neighbors = [(i, j) for i, j in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)) if
                         0 <= i < rows and 0 <= j < cols]
            for n in neighbors:
                actions.append([point, n])
        for action in actions:
            [coord1, coord2] = action
            if [coord2, coord1] and [coord1, coord2] in actions:
                actions.remove([coord2, coord1])
        action_num = [i for i in range(len(actions))]
        action_dict = dict(zip(action_num, actions))
        return action_dict

    def __init__(self, rollout_len=NUM_OF_MOVES_PER_GAME):
        super(MatchThreeEnv, self).__init__()
        self.rollout_len = rollout_len
        self.episode_counter = 0
        self.possible_actions = list()
        self.reset()
        board = self.game.get_board()
        # Define action and observation space
        # setting action space
        self.game_actions = self.get_legal_actions(board)
        self.action_space = spaces.Discrete(len(self.game_actions))
        # setting observation space
        self.observation_space = spaces.Box(
            low=1,
            high=COLOR_END,
            shape=BOARD_SIZE,
            dtype=np.int)

    def __get_action(self, index):
        return self.game_actions[index]

    def get_valid_actions(self):
        return self.game.move_helper()

    def get_action_mask(self):
        valid_actions = self.game.move_helper()
        masked_actions_keys = [k for k, v in self.game_actions.items() if v in valid_actions]
        mask = np.zeros(len(self.game_actions))
        for i in masked_actions_keys:
            mask[i] = 1
        return mask

    def get_score(self):
        return self.game.get_score()

    def step(self, action):
        self.game.input_tiles(self.__get_action(action))
        # change counter even action wasn't successful
        self.episode_counter += 1
        if self.episode_counter >= self.rollout_len:
            done = True
            self.episode_counter = 0
            reward = self.game.get_score()
            observation = self.reset()
        else:
            done = False
            reward = 0
            observation = self.game.get_board()
        return observation, reward, done, {}

    def reset(self):
        self.game.init_board()
        self.game.find_moves()
        self.game.game_stats.stat_game_score = 0
        self.possible_actions = self.game.move_helper()
        observation = self.game.get_board()
        return observation  # reward, done, info can't be included

    def render(self, mode=None):
        print(self.game.get_board())

    def close(self):
        pass
