import time
import os
import gym
import numpy as np
from sb3_contrib.common.maskable.policies import MaskableActorCriticPolicy
from sb3_contrib.common.wrappers import ActionMasker
from sb3_contrib.ppo_mask import MaskablePPO
from m3_gym_env import MatchThreeEnv

os.environ['KMP_DUPLICATE_LIB_OK']='True'


def mask_fn(env: gym.Env) -> np.ndarray:
    # env has a helpful method we can rely on.
    return env.get_action_mask()


env = MatchThreeEnv(10)  # Initialize env
env = ActionMasker(env, mask_fn)  # Wrap to enable masking

# MaskablePPO behaves the same as SB3's PPO unless the env is wrapped
# with ActionMasker. If the wrapper is detected, the masks are automatically
# retrieved and used when learning.
model_params = {
    "n_steps": 512,
    "batch_size": 256,
    "gamma": 0.9999,
    "learning_rate": 9.780496175531937e-05,
    "ent_coef": 5.994868211837647e-08,
    "n_epochs": 20,
    "gae_lambda": 0.95,
    "max_grad_norm": 0.3,
    "vf_coef": 0.4415183431344316,
    "clip_range": 0.3
}
model = MaskablePPO(MaskableActorCriticPolicy, env, verbose=1,tensorboard_log="./ppo_m3_tensorboard/", **model_params)
start_time = time.time()
model.learn(total_timesteps=1000000)
end_time = time.time()
# save model
model.save("ppo_m3_5X5_tuning")