import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv("agents_eval.csv")
random_scores = data[data['Agent'] == 'random_agent']['Mean'].round(2).tolist()
print(random_scores)
bottom_scores = data[data['Agent'] == 'bottom_agent']['Mean'].round(2).tolist()
print(bottom_scores)
rl_scores = data[data['Agent'] == 'RL Agent(PPO)']['Mean'].round(2).tolist()
print(rl_scores)
index = ["5x5 Grid", "10x10 Grid", "15x15 Grid"]
df = pd.DataFrame({'random agent': random_scores,
                   'bottom agent': bottom_scores,
                   'RL agent': rl_scores}, index=index)
print(df)
ax = df.plot.bar(rot=0, width=0.25)
ax.set_ylabel("Mean score")
plot.show()
