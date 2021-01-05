import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("exp_game_results_2.csv")
df1 = dataframe[dataframe['Grid Size'] == "(5, 5)"]
df2 = dataframe[dataframe['Grid Size'] == "(7, 7)"]
df3 = dataframe[dataframe['Grid Size'] == "(10, 10)"]
df4 = dataframe[dataframe['Grid Size'] == "(15, 15)"]
df5 = dataframe[dataframe['Grid Size'] == "(20, 20)"]


x1 = df1['Number of Colors']
y1 = df1['Total No. of Regenerations until valid board generation']
x2 = df2['Number of Colors']
y2 = df2['Total No. of Regenerations until valid board generation']
x3 = df3['Number of Colors']
y3 = df3['Total No. of Regenerations until valid board generation']
x4 = df4['Number of Colors']
y4 = df4['Total No. of Regenerations until valid board generation']
x5 = df5['Number of Colors']
y5 = df5['Total No. of Regenerations until valid board generation']


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)

plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
# plt.title('')
plt.xlabel('Number of Colors')
plt.ylabel('Total No. of Regenerations until valid board generation')
plt.savefig('plots/plot1.png')

plt.clf()

y1 = df1['Total No. of Times Matches Occurred during init']
y2 = df2['Total No. of Times Matches Occurred during init']
y3 = df3['Total No. of Times Matches Occurred during init']
y4 = df4['Total No. of Times Matches Occurred during init']
y5 = df5['Total No. of Times Matches Occurred during init']

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Total No. of Times Matches Occurred during init')
plt.savefig('plots/plot2.png')

plt.clf()

y1 = df1['Total No. of Deadlocks during init']
y2 = df2['Total No. of Deadlocks during init']
y3 = df3['Total No. of Deadlocks during init']
y4 = df4['Total No. of Deadlocks during init']
y5 = df5['Total No. of Deadlocks during init']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Total No. of Deadlocks during init')
plt.savefig('plots/plot3.png')

plt.clf()

y1 = df1['Average No. of Regenerations until valid board generation']
y2 = df2['Average No. of Regenerations until valid board generation']
y3 = df3['Average No. of Regenerations until valid board generation']
y4 = df4['Average No. of Regenerations until valid board generation']
y5 = df5['Average No. of Regenerations until valid board generation']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Regenerations until valid board generation')
plt.savefig('plots/plot4.png')

plt.clf()

y1 = df1['Total No. of Shuffles/Deadlocks Occurred']
y2 = df2['Total No. of Shuffles/Deadlocks Occurred']
y3 = df3['Total No. of Shuffles/Deadlocks Occurred']
y4 = df4['Total No. of Shuffles/Deadlocks Occurred']
y5 = df5['Total No. of Shuffles/Deadlocks Occurred']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Total No. of Shuffles/Deadlocks Occurred')
plt.savefig('plots/plot5.png')

plt.clf()

y1 = df1['Average No. of Moves until Shuffle occurs']
y2 = df2['Average No. of Moves until Shuffle occurs']
y3 = df3['Average No. of Moves until Shuffle occurs']
y4 = df4['Average No. of Moves until Shuffle occurs']
y5 = df5['Average No. of Moves until Shuffle occurs']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Moves until Shuffle occurs')
plt.savefig('plots/plot6.png')

plt.clf()

y1 = df1['Average No. of Deadlocks Occurred']
y2 = df2['Average No. of Deadlocks Occurred']
y3 = df3['Average No. of Deadlocks Occurred']
y4 = df4['Average No. of Deadlocks Occurred']
y5 = df5['Average No. of Deadlocks Occurred']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Deadlocks Occurred')
plt.savefig('plots/plot7.png')

plt.clf()

y1 = df1['Total score per Game Setting']
y2 = df2['Total score per Game Setting']
y3 = df3['Total score per Game Setting']
y4 = df4['Total score per Game Setting']
y5 = df5['Total score per Game Setting']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Total score per Game Setting')
plt.savefig('plots/plot8.png')

plt.clf()

y1 = df1['Total Valid Moves Made']
y2 = df2['Total Valid Moves Made']
y3 = df3['Total Valid Moves Made']
y4 = df4['Total Valid Moves Made']
y5 = df5['Total Valid Moves Made']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Total Valid Moves Made')
plt.savefig('plots/plot9.png')

plt.clf()

y1 = df1['Average Score per Move']
y2 = df2['Average Score per Move']
y3 = df3['Average Score per Move']
y4 = df4['Average Score per Move']
y5 = df5['Average Score per Move']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average Score per Move')
plt.savefig('plots/plot10.png')

plt.clf()

y1 = df1['Total No. of Possible Moves']
y2 = df2['Total No. of Possible Moves']
y3 = df3['Total No. of Possible Moves']
y4 = df4['Total No. of Possible Moves']
y5 = df5['Total No. of Possible Moves']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Total No. of Possible Moves')
plt.savefig('plots/plot11.png')

plt.clf()

y1 = df1['Average No. of Possible Moves per Configuration']
y2 = df2['Average No. of Possible Moves per Configuration']
y3 = df3['Average No. of Possible Moves per Configuration']
y4 = df4['Average No. of Possible Moves per Configuration']
y5 = df5['Average No. of Possible Moves per Configuration']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Possible Moves per Configuration')
plt.savefig('plots/plot12.png')

plt.clf()

y1 = df1['Total No. of Avalanche Matches']
y2 = df2['Total No. of Avalanche Matches']
y3 = df3['Total No. of Avalanche Matches']
y4 = df4['Total No. of Avalanche Matches']
y5 = df5['Total No. of Avalanche Matches']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Total No. of Avalanche Matches')
plt.savefig('plots/plot13.png')

plt.clf()

y1 = df1['Average No. of Avalanche matches occurred']
y2 = df2['Average No. of Avalanche matches occurred']
y3 = df3['Average No. of Avalanche matches occurred']
y4 = df4['Average No. of Avalanche matches occurred']
y5 = df5['Average No. of Avalanche matches occurred']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average No. of Avalanche matches occurred')
plt.savefig('plots/plot14.png')