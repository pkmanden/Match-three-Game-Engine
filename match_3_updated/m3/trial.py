import gym
import m3_gym_env
env = m3_gym_env.MatchThreeEnv(100)
# env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()
