import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("exp_game_results_old.csv")
df1 = dataframe[dataframe['Grid Size'] == "(5, 5)"]
df2 = dataframe[dataframe['Grid Size'] == "(7, 7)"]
df3 = dataframe[dataframe['Grid Size'] == "(10, 10)"]
df4 = dataframe[dataframe['Grid Size'] == "(15, 15)"]
df5 = dataframe[dataframe['Grid Size'] == "(20, 20)"]


x1 = df1['Number of Colors']
# x1 = (x1 - min(x1)) / (max(x1) - min(x1))
x2 = df2['Number of Colors']
# x2 = (x2 - min(x2)) / (max(x2) - min(x2))
x3 = df3['Number of Colors']
# x3 = (x3 - min(x3)) / (max(x3) - min(x3))
x4 = df4['Number of Colors']
# x4 = (x4 - min(x4)) / (max(x4) - min(x4))
x5 = df5['Number of Colors']
# x5 = (x5 - min(x5)) / (max(x5) - min(x5))

x1 = x1/ max(x1)
x2 = x2/ max(x2)
x3 = x3/ max(x3)
x4 = x4/ max(x4)
x5 = x5/ max(x5)
# plt.xlim([0, 100])
# plt.xticks(np.arange(0, 100, 10))


y1 = df1['Average No. of Regenerations until valid board generation per game setting']
y2 = df2['Average No. of Regenerations until valid board generation per game setting']
y3 = df3['Average No. of Regenerations until valid board generation per game setting']
y4 = df4['Average No. of Regenerations until valid board generation per game setting']
y5 = df5['Average No. of Regenerations until valid board generation per game setting']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)

plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
# plt.title('')
plt.xlabel('Number of Colors')
plt.ylabel('Avg No. of Regenerations until valid board generation per game setting')
plt.savefig('plots/plot1.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Average No. of Times Matches Occurred during init per game setting']
y2 = df2['Average No. of Times Matches Occurred during init per game setting']
y3 = df3['Average No. of Times Matches Occurred during init per game setting']
y4 = df4['Average No. of Times Matches Occurred during init per game setting']
y5 = df5['Average No. of Times Matches Occurred during init per game setting']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Times Matches Occurred during init per game setting')
plt.savefig('plots/plot2.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Average No. of Deadlocks during init per game setting']
y2 = df2['Average No. of Deadlocks during init per game setting']
y3 = df3['Average No. of Deadlocks during init per game setting']
y4 = df4['Average No. of Deadlocks during init per game setting']
y5 = df5['Average No. of Deadlocks during init per game setting']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Deadlocks during init per game setting')
plt.savefig('plots/plot3.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Average No. of Shuffles/Deadlocks Occurred per game setting']
y2 = df2['Average No. of Shuffles/Deadlocks Occurred per game setting']
y3 = df3['Average No. of Shuffles/Deadlocks Occurred per game setting']
y4 = df4['Average No. of Shuffles/Deadlocks Occurred per game setting']
y5 = df5['Average No. of Shuffles/Deadlocks Occurred per game setting']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Shuffles/Deadlocks Occurred per game setting')
plt.savefig('plots/plot4.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Average No. of Moves until Shuffle occurs per game setting']
y2 = df2['Average No. of Moves until Shuffle occurs per game setting']
y3 = df3['Average No. of Moves until Shuffle occurs per game setting']
y4 = df4['Average No. of Moves until Shuffle occurs per game setting']
y5 = df5['Average No. of Moves until Shuffle occurs per game setting']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Moves until Shuffle occurs per game setting')
plt.savefig('plots/plot5.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Average Score per game setting']
y2 = df2['Average Score per game setting']
y3 = df3['Average Score per game setting']
y4 = df4['Average Score per game setting']
y5 = df5['Average Score per game setting']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average Score per game setting')
plt.savefig('plots/plot6.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Average Score per Move']
y2 = df2['Average Score per Move']
y3 = df3['Average Score per Move']
y4 = df4['Average Score per Move']
y5 = df5['Average Score per Move']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average Score per Move')
plt.savefig('plots/plot7.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Average No. of Valid Moves made per game setting']
y2 = df2['Average No. of Valid Moves made per game setting']
y3 = df3['Average No. of Valid Moves made per game setting']
y4 = df4['Average No. of Valid Moves made per game setting']
y5 = df5['Average No. of Valid Moves made per game setting']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Valid Moves made per game setting')
plt.savefig('plots/plot8.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Average No. of Possible Moves per Configuration']
y2 = df2['Average No. of Possible Moves per Configuration']
y3 = df3['Average No. of Possible Moves per Configuration']
y4 = df4['Average No. of Possible Moves per Configuration']
y5 = df5['Average No. of Possible Moves per Configuration']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Possible Moves per Configuration')
plt.savefig('plots/plot9.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Average No. of Avalanche matches per game setting']
y2 = df2['Average No. of Avalanche matches per game setting']
y3 = df3['Average No. of Avalanche matches per game setting']
y4 = df4['Average No. of Avalanche matches per game setting']
y5 = df5['Average No. of Avalanche matches per game setting']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Avalanche matches per game setting')
plt.savefig('plots/plot10.png')

plt.clf()
# ---------------------------------------------------------
y1 = df1['Probability that a deadlock will occur in the given game setting']
y2 = df2['Probability that a deadlock will occur in the given game setting']
y3 = df3['Probability that a deadlock will occur in the given game setting']
y4 = df4['Probability that a deadlock will occur in the given game setting']
y5 = df5['Probability that a deadlock will occur in the given game setting']

y1 = (y1 - min(y1)) / (max(y1) - min(y1))
y2 = (y2 - min(y2)) / (max(y2) - min(y2))
y3 = (y3 - min(y3)) / (max(y3) - min(y3))
y4 = (y4 - min(y4)) / (max(y4) - min(y4))
y5 = (y5 - min(y5)) / (max(y5) - min(y5))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Probability that a deadlock will occur in the given game setting')
plt.savefig('plots/plot11.png')

plt.clf()
# ---------------------------------------------------------
