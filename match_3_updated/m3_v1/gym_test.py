from stable_baselines3.common.env_checker import check_env
import match_3_gym_env
env = match_3_gym_env.MatchThreeEnv(100)
# It will check your custom environment and output additional warnings if needed
check_env(env)