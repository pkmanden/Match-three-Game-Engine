import csv
import os

import gym
from sb3_contrib.common.wrappers import ActionMasker
from sb3_contrib.ppo_mask import MaskablePPO

# Create environment
import m3_gym_env
from m3_globals import *
from m3_gym_env import BOARD_SIZE, COLOR_END
from gameplay_heatmap import GameplayHeatmap

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def mask_fn(env: gym.Env) -> np.ndarray:
    # env has a helpful method we can rely on.
    return env.get_action_mask()

rollout_len = NUM_OF_MOVES_PER_GAME
env = m3_gym_env.MatchThreeEnv(rollout_len)
env = ActionMasker(env, mask_fn)
model = MaskablePPO.load("ppo_m3_5X5_tunin.zip", use_masking=True)


boards = np.load('starting_boards.npz')
env.reset()
edges_gh = GameplayHeatmap()
for i in range(len(boards)):
    ind = 'arr_%s'% i
    board = boards[ind]
    repeat = EXP_SAME_BOARD_REPEAT
    while repeat > 0:
        obs = board
        moves_to_end = NUM_OF_MOVES_PER_GAME
        while moves_to_end > 0:
            env.render()
            action, _states = model.predict(obs, action_masks=env.get_action_mask())
            obs, reward, done, info = env.step(action)
            edges_gh.add_move_to_graph(env.game_actions[action], "rl_agent")
            # total_score += env.game.get_move_score()
            if done:
                print('Done trajectory')
                file_exists = os.path.isfile("exp_rl_agent_result.csv")
                with open('exp_rl_agent_result.csv', 'a+', newline='') as csv_file:
                    fieldnames = ['Agent',
                                  'Grid Size',
                                  'Number of Colors',
                                  'Total score per Game Setting']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                    if not file_exists:
                        print("File does not exist")
                        writer.writeheader()

                    writer.writerow({
                        'Agent': 'RL Agent(PPO)',
                        'Grid Size': BOARD_SIZE,
                        'Number of Colors': COLOR_END,
                        'Total score per Game Setting': reward
                    })
                # obs = env.reset()
                break
            moves_to_end -= 1
        repeat -= 1
edges_gh.draw_map("rl_agent")