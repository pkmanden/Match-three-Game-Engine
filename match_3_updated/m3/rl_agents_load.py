from stable_baselines3 import DQN, A2C
from stable_baselines3.common.evaluation import evaluate_policy

# Create environment
import m3_gym_env

env = m3_gym_env.MatchThreeEnv(100)

# Load the trained agent
# model = DQN.load("dqn_m3", env=env)
model = A2C.load("a2c_m3")
# Evaluate the agent
# NOTE: If you use wrappers with your environment that modify rewards,
#       this will be reflected here. To evaluate with original rewards,
#       wrap environment in a "Monitor" wrapper before other wrappers.
# mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

# Enjoy trained agent
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()

# model = A2C.load("a2c_m3")

# obs = env.reset()
# while True:
#     action, _states = model.predict(obs)
#     obs, rewards, dones, info = env.step(action)
#     env.render()