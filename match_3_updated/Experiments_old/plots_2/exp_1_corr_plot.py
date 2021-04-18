
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('exp_game_results_1.csv', usecols=["Grid Size", "Max Colors", "Actual Colors", "Avg No. of Regenerations until valid board generation", "Avg No. of Times Matches Occurred during init", "Avg No. of Deadlocks during init", "Avg No. of Times Game Started", "Avg No. of Shuffles/Deadlocks Occurred", "Average No. of Moves until Shuffle occurs per game setting", "Avg score per Game Setting", "Avg Valid Moves Made", "Avg No. of Possible/Playable Moves", "Avg No. of Avalanche Matches"])
# df1 = data[data['Grid Size'] == "(5, 5)"]
# df2 = data[data['Grid Size'] == "(7, 7)"]
# df3 = data[data['Grid Size'] == "(10, 10)"]
# df4 = data[data['Grid Size'] == "(15, 15)"]

corr = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)
plt.show()