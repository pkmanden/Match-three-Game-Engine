import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv("agents_eval.csv")

top_scores = data[data['Agent'] == 'top_agent']['Score Mean'].round(2).tolist()
random_scores = data[data['Agent'] == 'random_agent']['Score Mean'].round(2).tolist()
bottom_scores = data[data['Agent'] == 'bottom_agent']['Score Mean'].round(2).tolist()
rl_scores = data[data['Agent'] == 'RL Agent(PPO)']['Score Mean'].round(2).tolist()
# ================================================================================
top_avalanche_score = data[data['Agent'] == 'top_agent']['Avalanche score Mean'].round(2).tolist()
random_avalanche_score = data[data['Agent'] == 'random_agent']['Avalanche score Mean'].round(2).tolist()
bottom_avalanche_score = data[data['Agent'] == 'bottom_agent']['Avalanche score Mean'].round(2).tolist()
rl_avalanche_score = data[data['Agent'] == 'RL Agent(PPO)']['Avalanche score Mean'].round(2).tolist()
index = ["5x5 Grid", "10x10 Grid", "15x15 Grid"]
df = pd.DataFrame({'RBA1': top_scores,
                   'random agent': random_scores,
                   'RBA2': bottom_scores,
                   'RL agent': rl_scores}, index=index)

ax = df.plot.bar(rot=0, width=0.25)
ax.set_ylabel("Mean score")
plot.show()
# ====================================
df = pd.DataFrame({'RBA1': top_avalanche_score,
                   'random agent': random_avalanche_score,
                   'RBA2': bottom_avalanche_score,
                   'RL agent': rl_avalanche_score}, index=index)

ax = df.plot.bar(rot=0, width=0.25)
ax.set_ylabel("Mean non-deterministic score")
plot.show()
plot.close()
# ====================================
df = pd.DataFrame({'RBA1': data[data['Agent'] == 'top_agent']['Deterministic score Mean'].tolist(),
                   'random agent': data[data['Agent'] == 'random_agent']['Deterministic score Mean'].tolist(),
                   'RBA2': data[data['Agent'] == 'bottom_agent']['Deterministic score Mean'].tolist(),
                   'RL agent': data[data['Agent'] == 'RL Agent(PPO)']['Deterministic score Mean'].tolist()}, index=index)

ax = df.plot.bar(rot=0, width=0.25)

plot.legend(loc='lower left')
ax.set_ylabel("Mean deterministic score")
plot.show()
