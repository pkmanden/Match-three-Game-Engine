import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# sns.set_theme(color_codes=True)

# fig = plt.figure()

# Take data from grid sizes
dataframe = pd.read_csv("plots_1/exp_game_results_new.csv")
df1 = dataframe[dataframe['Grid Size'] == "(5, 5)"]
df2 = dataframe[dataframe['Grid Size'] == "(7, 7)"]
df3 = dataframe[dataframe['Grid Size'] == "(10, 10)"]
df4 = dataframe[dataframe['Grid Size'] == "(15, 15)"]
# df5 = dataframe[dataframe['Grid Size'] == "(20, 20)"]

# sns.kdeplot(data=df1, x="Number of Colors", hue="Avg No. of Regenerations until valid board generation per game setting")
# sns.relplot(x="Number of Colors", y="Avg No. of Regenerations until valid board generation per game setting", hue="Grid Size", data=dataframe, kind="line")
# sns.regplot(x="Number of Colors", y="Avg No. of Regenerations until valid board generation per game setting", order=1, data=df1)
sns.relplot(x='Number of Colors', y='Avg No. of Regenerations until valid board generation per game setting', data=dataframe,
              hue='Grid Size', kind="line")
plt.savefig('plots_1/1.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Avg No. of Times Matches Occurred during init per game setting', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/2.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Avg No. of Deadlocks during init per game setting', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/3.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Avg No. of Shuffles/Deadlocks Occurred per game setting', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/4.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Average No. of Moves until Shuffle occurs per game setting', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/5.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Avg score per Game Setting', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/6.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Avg No. of Valid Moves Made', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/7.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Avg Score per Move', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/8.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Avg No. of Possible/Playable Moves per configuration', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/9.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Avg No. of Avalanche Matches per game setting', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/10.png', bbox_inches='tight')
plt.clf()
sns.relplot(x='Number of Colors', y='Probability that the game will not start', data=dataframe,
            hue='Grid Size', kind="line")
plt.savefig('plots_1/11.png', bbox_inches='tight')
plt.clf()
# sns.regplot(x="Number of Colors", y="Avg No. of Times Matches Occurred during init per game setting", order=1, data=df1)
# plt.savefig('plots_1/2.png', bbox_inches='tight')
# plt.clf()
# sns.regplot(x="Number of Colors", y="Avg No. of Deadlocks during init per game setting", order=1, data=df1)
# plt.savefig('plots_1/3.png', bbox_inches='tight')
# sns.regplot(x="Number of Colors", y="Avg No. of Shuffles/Deadlocks Occurred per game setting", order=1, data=df1)
# plt.savefig('plots_1/4.png', bbox_inches='tight')
# ----------------------------Grid Size 5X5
# x = df1['Number of Colors']
#
# y1 = df1['Avg No. of Regenerations until valid board generation per game setting']
# y2 = df1['Avg No. of Times Matches Occurred during init per game setting']
# y3 = df1['Avg No. of Deadlocks during init per game setting']
# y4 = df1['Avg No. of Shuffles/Deadlocks Occurred per game setting']
# y5 = df1['Average No. of Moves until Shuffle occurs per game setting']
# y6 = df1['Avg score per Game Setting']
# y7 = df1['Avg Score per Move']
# y8 = df1['Avg No. of Valid Moves Made']
# y9 = df1['Avg No. of Possible/Playable Moves per configuration']
# y10 = df1['Avg No. of Avalanche Matches per game setting']
# y11 = df1['Probability that the game will not start']
#
#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# labels = ["Avg No. of Regenerations until valid board generation per game setting",
#           "Avg No. of Times Matches Occurred during init per game setting",
#           "Avg No. of Deadlocks during init per game setting"]
# plt.xlabel("Number of Colors")
# plt.xticks(np.arange(0, 25, 5))
# plt.title("Grid Size 5 X 5")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/5_5_1.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y4)
# labels = ["Avg No. of Shuffles/Deadlocks Occurred per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 5 X 5")
#
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/5_5_2.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y5)
# labels = ["Average No. of Moves until Shuffle occurs per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 5 X 5")
#
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/5_5_3.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y6)
# labels = ["Avg score per Game Setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 5 X 5")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/5_5_4.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y8)
# labels = ["Avg No. of Valid Moves Made"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 5 X 5")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/5_5_5.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y7)
# labels = ["Avg Score per Move"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 5 X 5")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/5_5_6.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y9)
# labels = ["Avg No. of Possible/Playable Moves per configuration"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 5 X 5")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/5_5_7.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y10)
# labels = ["Avg No. of Avalanche Matches per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 5 X 5")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/5_5_8.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y11)
# labels = ["Probability that the game will not start"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 5 X 5")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/5_5_9.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
# # sns.regplot(x="Number of Colors", y="Avg No. of Regenerations until valid board generation per game setting", data=df1)
# # plt.show()
# plt.clf()
#
# # # -------------------------Grid Size 7X7------------------------------
# x = df2['Number of Colors']
#
# y1 = df2['Avg No. of Regenerations until valid board generation per game setting']
# y2 = df2['Avg No. of Times Matches Occurred during init per game setting']
# y3 = df2['Avg No. of Deadlocks during init per game setting']
# y4 = df2['Avg No. of Shuffles/Deadlocks Occurred per game setting']
# y5 = df2['Average No. of Moves until Shuffle occurs per game setting']
# y6 = df2['Avg score per Game Setting']
# y7 = df2['Avg Score per Move']
# y8 = df2['Avg No. of Valid Moves Made']
# y9 = df2['Avg No. of Possible/Playable Moves per configuration']
# y10 = df2['Avg No. of Avalanche Matches per game setting']
# y11 = df2['Probability that the game will not start']
#
# plt.xticks(np.arange(0, 50, 10))
#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# labels = ["Avg No. of Regenerations until valid board generation per game setting",
#           "Avg No. of Times Matches Occurred during init per game setting",
#           "Avg No. of Deadlocks during init per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 7 X 7")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/7_7_1.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()  # clear plot
#
# plt.plot(x, y4)
# labels = ["Avg No. of Shuffles/Deadlocks Occurred per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 7 X 7")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/7_7_2.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y5)
# labels = ["Average No. of Moves until Shuffle occurs per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 7 X 7")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/7_7_3.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y6)
# labels = ["Avg score per Game Setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 7 X 7")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/7_7_4.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y8)
# labels = ["Avg No. of Valid Moves Made"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 7 X 7")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/7_7_5.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y7)
# labels = ["Avg Score per Move"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 7 X 7")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/7_7_6.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y9)
# labels = ["Avg No. of Possible/Playable Moves per configuration"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 7 X 7")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/7_7_7.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y10)
# labels = ["Avg No. of Avalanche Matches per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 7 X 7")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/7_7_8.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y11)
# labels = ["Probability that the game will not start"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 7 X 7")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/7_7_9.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
#
# plt.clf()
#
# # # --------------------------Grid Size 10X10-----------------------------------
# #
# x = df3['Number of Colors']
#
# y1 = df3['Avg No. of Regenerations until valid board generation per game setting']
# y2 = df3['Avg No. of Times Matches Occurred during init per game setting']
# y3 = df3['Avg No. of Deadlocks during init per game setting']
# y4 = df3['Avg No. of Shuffles/Deadlocks Occurred per game setting']
# y5 = df3['Average No. of Moves until Shuffle occurs per game setting']
# y6 = df3['Avg score per Game Setting']
# y7 = df3['Avg Score per Move']
# y8 = df3['Avg No. of Valid Moves Made']
# y9 = df3['Avg No. of Possible/Playable Moves per configuration']
# y10 = df3['Avg No. of Avalanche Matches per game setting']
# y11 = df3['Probability that the game will not start']
#
# plt.xticks(np.arange(0, 100, 20))
#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# labels = ["Avg No. of Regenerations until valid board generation per game setting",
#           "Avg No. of Times Matches Occurred during init per game setting",
#           "Avg No. of Deadlocks during init per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/10_10_1.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()  # clear plot
#
# plt.plot(x, y4)
# labels = ["Avg No. of Shuffles/Deadlocks Occurred per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/10_10_2.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y5)
# labels = ["Average No. of Moves until Shuffle occurs per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/10_10_3.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y6)
# labels = ["Avg score per Game Setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/10_10_4.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y8)
# labels = ["Avg No. of Valid Moves Made"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/10_10_5.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y7)
# labels = ["Avg Score per Move"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/10_10_6.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y9)
# labels = ["Avg No. of Possible/Playable Moves per configuration"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/10_10_7.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y10)
# labels = ["Avg No. of Avalanche Matches per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/10_10_8.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y11)
# labels = ["Probability that the game will not start"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 10 X 10")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/10_10_9.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
#
# plt.clf()
# #
# # # ---------------------Gride Size 15X15-----------------------
# x = df4['Number of Colors']
#
# y1 = df4['Avg No. of Regenerations until valid board generation per game setting']
# y2 = df4['Avg No. of Times Matches Occurred during init per game setting']
# y3 = df4['Avg No. of Deadlocks during init per game setting']
# y4 = df4['Avg No. of Shuffles/Deadlocks Occurred per game setting']
# y5 = df4['Average No. of Moves until Shuffle occurs per game setting']
# y6 = df4['Avg score per Game Setting']
# y7 = df4['Avg Score per Move']
# y8 = df4['Avg No. of Valid Moves Made']
# y9 = df4['Avg No. of Possible/Playable Moves per configuration']
# y10 = df4['Avg No. of Avalanche Matches per game setting']
# y11 = df4['Probability that the game will not start']
#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# labels = ["Avg No. of Regenerations until valid board generation per game setting",
#           "Avg No. of Times Matches Occurred during init per game setting",
#           "Avg No. of Deadlocks during init per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/15_15_1.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()  # clear plot
#
# plt.plot(x, y4)
# labels = ["Avg No. of Shuffles/Deadlocks Occurred per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/15_15_2.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y5)
# labels = ["Average No. of Moves until Shuffle occurs per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/15_15_3.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y6)
# labels = ["Avg score per Game Setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/15_15_4.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y8)
# labels = ["Avg No. of Valid Moves Made"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/15_15_5.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y7)
# labels = ["Avg Score per Move"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/15_15_6.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y9)
# labels = ["Avg No. of Possible/Playable Moves per configuration"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/15_15_7.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y10)
# labels = ["Avg No. of Avalanche Matches per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/15_15_8.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y11)
# labels = ["Probability that the game will not start"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 15 X 15")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/15_15_9.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# # # --------------------Grid Size 20X20--------------------------------
# #
# x = df5['Number of Colors']
#
# y1 = df5['Avg No. of Regenerations until valid board generation per game setting']
# y2 = df5['Avg No. of Times Matches Occurred during init per game setting']
# y3 = df5['Avg No. of Deadlocks during init per game setting']
# y4 = df5['Avg No. of Shuffles/Deadlocks Occurred per game setting']
# y5 = df5['Average No. of Moves until Shuffle occurs per game setting']
# y6 = df5['Avg score per Game Setting']
# y7 = df5['Avg Score per Move']
# y8 = df5['Avg No. of Valid Moves Made']
# y9 = df5['Avg No. of Possible/Playable Moves per configuration']
# y10 = df5['Avg No. of Avalanche Matches per game setting']
# y11 = df5['Probability that the game will not start']
#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# labels = ["Avg No. of Regenerations until valid board generation per game setting",
#           "Avg No. of Times Matches Occurred during init per game setting",
#           "Avg No. of Deadlocks during init per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/20_20_1.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()  # clear plot
#
# plt.plot(x, y4)
# labels = ["Avg No. of Shuffles/Deadlocks Occurred per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/20_20_2.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y5)
# labels = ["Average No. of Moves until Shuffle occurs per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/20_20_3.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y6)
# labels = ["Avg score per Game Setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/20_20_4.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
# plt.plot(x, y8)
# labels = ["Avg No. of Valid Moves Made"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/20_20_5.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y7)
# labels = ["Avg Score per Move"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/20_20_6.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y9)
# labels = ["Avg No. of Possible/Playable Moves per configuration"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/20_20_7.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y10)
# labels = ["Avg No. of Avalanche Matches per game setting"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/20_20_8.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
#
# plt.clf()
#
# plt.plot(x, y11)
# labels = ["Probability that the game will not start"]
# plt.xlabel("Number of Colors")
# plt.title("Grid Size 20 X 20")
# lgd = plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
# plt.savefig('plots_1/20_20_9.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
