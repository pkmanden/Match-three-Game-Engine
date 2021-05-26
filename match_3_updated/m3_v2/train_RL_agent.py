import time
import os

import gym
import numpy as np

from sb3_contrib.common.maskable.policies import MaskableActorCriticPolicy
from sb3_contrib.common.wrappers import ActionMasker
from sb3_contrib.ppo_mask import MaskablePPO

import m3_gym_env

os.environ['KMP_DUPLICATE_LIB_OK']='True'


def mask_fn(env: gym.Env) -> np.ndarray:
    # Do whatever you'd like in this function to return the action mask
    # for the current env. In this example, we assume the env has a
    # helpful method we can rely on.
    return env.get_action_mask()


env = m3_gym_env.MatchThreeEnv(10)  # Initialize env
env = ActionMasker(env, mask_fn)  # Wrap to enable masking

# MaskablePPO behaves the same as SB3's PPO unless the env is wrapped
# with ActionMasker. If the wrapper is detected, the masks are automatically
# retrieved and used when learning. Note that MaskablePPO does not accept
# a new action_mask_fn kwarg, as it did in an earlier draft.
model = MaskablePPO(MaskableActorCriticPolicy, env, verbose=1)
start_time = time.time()
model.learn(total_timesteps=500000)
end_time = time.time()
# save model
model.save("ppo_m3_10X10_15")
print(f'Trained for {end_time-start_time} seconds')

# Note that use of masks is manual and optional outside of learning,
# so masking can be "removed" at testing time
# observation = env.reset()
# model.predict(observation, action_masks=env.get_action_mask())
