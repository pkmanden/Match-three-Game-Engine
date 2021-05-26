from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy


# Create environment
from match_3_updated.m3_v1 import match_3_gym_env

env = match_3_gym_env.MatchThreeEnv(100)

# Instantiate the agent
model = DQN('MlpPolicy', env, verbose=1)
# Train the agent
model.learn(total_timesteps=int(10000))
# Save the agent
model.save("dqn_match3")
del model  # delete trained model to demonstrate loading

# Load the trained agent
model = DQN.load("dqn_match3", env=env)

# Evaluate the agent
# NOTE: If you use wrappers with your environment that modify rewards,
#       this will be reflected here. To evaluate with original rewards,
#       wrap environment in a "Monitor" wrapper before other wrappers.
mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

# Enjoy trained agent
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    env.render()