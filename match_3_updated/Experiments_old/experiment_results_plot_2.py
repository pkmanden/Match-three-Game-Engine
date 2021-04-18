import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Take data from grid sizes
dataframe = pd.read_csv("plots_2/exp_game_results_1.csv")
df1 = dataframe[dataframe['Grid Size'] == "(5, 5)"]
df11 = df1.groupby('Actual Colors', as_index=False).mean()
df3 = dataframe[dataframe['Grid Size'] == "(10, 10)"]
df33 = df3.groupby('Actual Colors', as_index=False).mean()
df4 = dataframe[dataframe['Grid Size'] == "(15, 15)"]
df44 = df4.groupby('Actual Colors', as_index=False).mean()
df5 = dataframe[dataframe['Grid Size'] == "(20, 20)"]
df55 = df5.groupby('Actual Colors', as_index=False).mean()

# create figure and axis objects with subplots()
fig, ax = plt.subplots()

# ----------------------------Grid Size 5X5
x = df11['Actual Colors']

y1 = df11['Avg No. of Regenerations until valid board generation']
y2 = df11['Avg No. of Times Matches Occurred during init']
y3 = df11['Avg No. of Deadlocks during init']
y4 = df11['Avg No. of Shuffles/Deadlocks Occurred per move']
# y5 = df11['Avg No. of Shuffles/Deadlocks Occurred']
y6 = df11['Avg No. of Moves until Shuffle occurs per game setting']
y7 = df11['Avg score per Game Setting']
y8 = df11['Avg Valid Moves Made']
y9 = df11['Avg No. of Possible/Playable Moves per configuration']
y10 = df11['Avg No. of Avalanche Matches']
y11 = df11['Probability that the game will start']


plt.plot(x, y11)
labels = ["Probability that the game will start"]
plt.xlabel("Actual Number of Colors")
# plt.xticks(np.arange(0, 25, 5))
plt.title("Grid Size 5 X 5")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/5_5_9.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
labels = ["Avg No. of Regenerations until valid board generation",
          "Avg No. of Times Matches Occurred during init",
          "Avg No. of Deadlocks during init"]
plt.xlabel("Actual Number of Colors")
# plt.xticks(np.arange(0, 25, 5))
plt.yscale('symlog')
plt.title("Grid Size 5 X 5")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/5_5_1.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()

plt.plot(x, y4)
plt.plot(x, y6)
labels = ["Avg No. of Shuffles/Deadlocks Occurred per move",
          "Avg No. of Moves until Shuffle occurs per game setting"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 5 X 5")

lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/5_5_2.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()

plt.plot(x, y8)
plt.plot(x, y7)
labels = ["Avg Valid Moves Made",
          "Avg score per Game Setting"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 5 X 5")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/5_5_3.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()


ax.plot(x, y8)
ax.set_xlabel("Actual Number of Colors")
ax.set_ylabel("Avg Valid Moves Made")
ax2=ax.twinx()
ax2.plot(x, y7)
ax2.set_ylabel("Avg score per Game Setting")
fig.savefig('5_5_4.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

plt.plot(x, y9)
labels = ["Avg No. of Possible/Playable Moves per configuration"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 5 X 5")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/5_5_5.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()

plt.plot(x, y10)
labels = ["Avg No. of Avalanche Matches"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 5 X 5")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/5_5_6.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()


# # --------------------------Grid Size 10X10-----------------------------------
#
x = df33['Actual Colors']

y1 = df33['Avg No. of Regenerations until valid board generation']
y2 = df33['Avg No. of Times Matches Occurred during init']
y3 = df33['Avg No. of Deadlocks during init']
y4 = df33['Avg No. of Shuffles/Deadlocks Occurred per move']
# y5 = df33['Avg No. of Shuffles/Deadlocks Occurred']
y6 = df33['Avg No. of Moves until Shuffle occurs per game setting']
y7 = df33['Avg score per Game Setting']
y8 = df33['Avg Valid Moves Made']
y9 = df33['Avg No. of Possible/Playable Moves per configuration']
y10 = df33['Avg No. of Avalanche Matches']
y11 = df33['Probability that the game will start']

plt.plot(x, y11)
labels = ["Probability that the game will start"]
plt.xlabel("Actual Number of Colors")
# plt.xticks(np.arange(0, 25, 5))
plt.title("Grid Size 10 X 10")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/10_10_9.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()
# plt.xticks(np.arange(0, 100, 20))

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
labels = ["Avg No. of Regenerations until valid board generation",
          "Avg No. of Times Matches Occurred during init",
          "Avg No. of Deadlocks during init"]
plt.xlabel("Actual Number of Colors")
plt.yscale('symlog')
plt.title("Grid Size 10 X 10")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/10_10_1.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()  # clear plot

plt.plot(x, y4)
labels = ["Avg No. of Shuffles/Deadlocks Occurred per move"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 10 X 10")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/10_10_2.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()
# plt.plot(x, y5)
# labels = ["Avg No. of Shuffles/Deadlocks Occurred"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/10_10_3.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()

plt.plot(x, y6)
labels = ["Avg No. of Moves until Shuffle occurs per game setting"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 10 X 10")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/10_10_4.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()
plt.plot(x, y8)
labels = ["Avg Valid Moves Made"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 10 X 10")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/10_10_5.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()

plt.plot(x, y7)
labels = ["Avg score per Game Setting"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 10 X 10")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/10_10_6.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()

plt.plot(x, y9)
labels = ["Avg No. of Possible/Playable Moves per configuration"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 10 X 10")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/10_10_7.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()

plt.plot(x, y10)
labels = ["Avg No. of Avalanche Matches"]
plt.xlabel("Actual Number of Colors")
plt.title("Grid Size 10 X 10")
lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
plt.savefig('plots_2/10_10_8.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.clf()
#
# # # ---------------------Gride Size 15X15-----------------------
# x = df44['Actual Colors']
#
# y1 = df44['Avg No. of Regenerations until valid board generation']
# y2 = df44['Avg No. of Times Matches Occurred during init']
# y3 = df44['Avg No. of Deadlocks during init']
# y4 = df44['Avg No. of Shuffles/Deadlocks Occurred per move']
# # y5 = df44['Avg No. of Shuffles/Deadlocks Occurred']
# y6 = df44['Avg No. of Moves until Shuffle occurs per game setting']
# y7 = df44['Avg score per Game Setting']
# y8 = df44['Avg Valid Moves Made']
# y9 = df44['Avg No. of Possible/Playable Moves per configuration']
# y10 = df44['Avg No. of Avalanche Matches']
# y11 = df44['Probability that the game will start']
#
# plt.plot(x, y11)
# labels = ["Probability that the game will start"]
# plt.xlabel("Actual Number of Colors")
# # plt.xticks(np.arange(0, 25, 5))
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/15_15_9.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# labels = ["Avg No. of Regenerations until valid board generation",
#           "Avg No. of Times Matches Occurred during init",
#           "Avg No. of Deadlocks during init"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/15_15_1.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()  # clear plot
#
# plt.plot(x, y4)
# labels = ["Avg No. of Shuffles/Deadlocks Occurred per move"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/15_15_2.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# # plt.plot(x, y5)
# # labels = ["Avg No. of Shuffles/Deadlocks Occurred"]
# # plt.xlabel("Actual Number of Colors")
# # plt.title("Grid Size 15 X 15")
# # lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# # plt.savefig('plots_2/15_15_3.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
# #
# # plt.clf()
#
# plt.plot(x, y6)
# labels = ["Avg No. of Moves until Shuffle occurs per game setting"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/15_15_4.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y8)
# labels = ["Avg Valid Moves Made"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/15_15_5.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y7)
# labels = ["Avg score per Game Setting"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/15_15_6.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y9)
# labels = ["Avg No. of Possible/Playable Moves per configuration"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/15_15_7.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y10)
# labels = ["Avg No. of Avalanche Matches"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/15_15_8.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# # --------------------Grid Size 20X20--------------------------------
#
# x = df55['Actual Colors']
#
# y1 = df55['Avg No. of Regenerations until valid board generation']
# y2 = df55['Avg No. of Times Matches Occurred during init']
# y3 = df55['Avg No. of Deadlocks during init']
# y4 = df55['Avg No. of Shuffles/Deadlocks Occurred per move']
# # y5 = df55['Avg No. of Shuffles/Deadlocks Occurred']
# y6 = df55['Avg No. of Moves until Shuffle occurs per game setting']
# y7 = df55['Avg score per Game Setting']
# y8 = df55['Avg Valid Moves Made']
# y9 = df55['Avg No. of Possible/Playable Moves per configuration']
# y10 = df55['Avg No. of Avalanche Matches']
# y11 = df55['Probability that the game will start']
#
# plt.plot(x, y11)
# labels = ["Probability that the game will start"]
# plt.xlabel("Actual Number of Colors")
# # plt.xticks(np.arange(0, 25, 5))
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/20_20_9.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# labels = ["Avg No. of Regenerations until valid board generation",
#           "Avg No. of Times Matches Occurred during init",
#           "Avg No. of Deadlocks during init"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/20_20_1.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()  # clear plot
#
# plt.plot(x, y4)
# labels = ["Avg No. of Shuffles/Deadlocks Occurred per move"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/20_20_2.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# # plt.plot(x, y5)
# # labels = ["Avg No. of Shuffles/Deadlocks Occurred"]
# # plt.xlabel("Actual Number of Colors")
# # plt.title("Grid Size 20 X 20")
# # lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# # plt.savefig('plots_2/20_20_3.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
# #
# # plt.clf()
#
# plt.plot(x, y6)
# labels = ["Avg No. of Moves until Shuffle occurs per game setting"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/20_20_4.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y8)
# labels = ["Avg Valid Moves Made"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/20_20_5.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y7)
# labels = ["Avg score per Game Setting"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/20_20_6.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y9)
# labels = ["Avg No. of Possible/Playable Moves per configuration"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/20_20_7.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y10)
# labels = ["Avg No. of Avalanche Matches"]
# plt.xlabel("Actual Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_2/20_20_8.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
