import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv("agents_eval.csv")
color_list = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

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

# ax = df.plot.bar(rot=0, width=0.5)
ax = df.plot(kind="bar", rot=0, width=0.5, yerr=[data[data['Agent'] == 'top_agent']['Score Std'],
                                                  data[data['Agent'] == 'random_agent']['Score Std'],
                                                  data[data['Agent'] == 'bottom_agent']['Score Std'],
                                                  data[data['Agent'] == 'RL Agent(PPO)']['Score Std']],
             color=color_list, capsize=2, error_kw=dict(ecolor='darkslategray'))
ax.yaxis.grid()
ax.set_axisbelow(True)
ax.figure.set_size_inches(8, 5)
# ax.figure.update_layout(barmode='group', bargap=0.15,)
ax.set_ylabel("Score")
plot.show()
plot.close()
# ====================================
df = pd.DataFrame({'RBA1': top_avalanche_score,
                   'random agent': random_avalanche_score,
                   'RBA2': bottom_avalanche_score,
                   'RL agent': rl_avalanche_score}, index=index)

# ax = df.plot.bar(rot=0, width=0.5)
ax = df.plot(kind="bar", rot=0, width=0.5, yerr=[data[data['Agent'] == 'top_agent']['Avalanche score Std'],
                                                  data[data['Agent'] == 'random_agent']['Avalanche score Std'],
                                                  data[data['Agent'] == 'bottom_agent']['Avalanche score Std'],
                                                  data[data['Agent'] == 'RL Agent(PPO)']['Avalanche score Std']],
             color=color_list, capsize=2, error_kw=dict(ecolor='darkslategray'))
ax.yaxis.grid()
ax.set_axisbelow(True)
ax.figure.set_size_inches(8, 5)
ax.set_ylabel("Non-deterministic score")
plot.show()
plot.close()
# ====================================
df = pd.DataFrame({'RBA1': data[data['Agent'] == 'top_agent']['Deterministic score Mean'].tolist(),
                   'random agent': data[data['Agent'] == 'random_agent']['Deterministic score Mean'].tolist(),
                   'RBA2': data[data['Agent'] == 'bottom_agent']['Deterministic score Mean'].tolist(),
                   'RL agent': data[data['Agent'] == 'RL Agent(PPO)']['Deterministic score Mean'].tolist()}, index=index)

ax = df.plot(kind="bar", rot=0, width=0.5, yerr=[data[data['Agent'] == 'top_agent']['Deterministic score Std'],
                                                  data[data['Agent'] == 'random_agent']['Deterministic score Std'],
                                                  data[data['Agent'] == 'bottom_agent']['Deterministic score Std'],
                                                  data[data['Agent'] == 'RL Agent(PPO)']['Deterministic score Std']],
             color=color_list, capsize=2, error_kw=dict(ecolor='darkslategray'))
ax.yaxis.grid()
ax.set_axisbelow(True)
ax.figure.set_size_inches(8, 5)
plot.legend(loc='lower left')
ax.set_ylabel("Deterministic score")
plot.show()
