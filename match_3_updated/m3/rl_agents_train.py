from stable_baselines3 import DQN, PPO, A2C
from stable_baselines3.common.evaluation import evaluate_policy

# Create environment
import m3_gym_env
env = m3_gym_env.MatchThreeEnv(100)

# # Instantiate the agent
# model = DQN('MlpPolicy', env, verbose=1)
# # Train the agent
# model.learn(total_timesteps=int(2e5))
# # Save the agent
# model.save("dqn_m3")
# del model  # delete trained model to demonstrate loading

# model = PPO("MlpPolicy", env, verbose=1)
# model.learn(total_timesteps=25000)
# model.save("ppo_m3")
# del model # remove to demonstrate saving and loading
#
# model = PPO.load("ppo_m3")
#
# obs = env.reset()
# while True:
#     action, _states = model.predict(obs)
#     obs, rewards, dones, info = env.step(action)
#     # env.render()

model = A2C("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=25000)
model.save("a2c_m3")

del model # remove to demonstrate saving and loading
