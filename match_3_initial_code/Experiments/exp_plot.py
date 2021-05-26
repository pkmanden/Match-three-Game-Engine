import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("Experiments_old/match_3_experiments_final.csv")
df1 = dataframe[dataframe['Grid Size'] == "(5, 5)"]
df2 = dataframe[dataframe['Grid Size'] == "(7, 7)"]
df3 = dataframe[dataframe['Grid Size'] == "(10, 10)"]
df4 = dataframe[dataframe['Grid Size'] == "(15, 15)"]
df5 = dataframe[dataframe['Grid Size'] == "(20, 20)"]



x1 = df1['Number of Colors']
y1 = df1['Average Number of Moves until Shuffle occurs']
x2 = df2['Number of Colors']
y2 = df2['Average Number of Moves until Shuffle occurs']
x3 = df3['Number of Colors']
y3 = df3['Average Number of Moves until Shuffle occurs']
x4 = df4['Number of Colors']
y4 = df4['Average Number of Moves until Shuffle occurs']
x5 = df5['Number of Colors']
y5 = df5['Average Number of Moves until Shuffle occurs']


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)



plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
# plt.title('')
plt.xlabel('Number of Colors')
plt.ylabel('Average Number of Moves until Shuffle occurs')
plt.savefig('Experiments_old/plot1.png')

plt.clf()

y1 = df1['Average Number of Times Deadlock Occurred']
y2 = df2['Average Number of Times Deadlock Occurred']
y3 = df3['Average Number of Times Deadlock Occurred']
y4 = df4['Average Number of Times Deadlock Occurred']
y5 = df5['Average Number of Times Deadlock Occurred']

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average Number of Times Deadlock Occurred')
plt.savefig('Experiments_old/plot2.png')

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
plt.savefig('Experiments_old/plot3.png')

plt.clf()

y1 = df1['Average Number of Possible Moves per Configuration']
y2 = df2['Average Number of Possible Moves per Configuration']
y3 = df3['Average Number of Possible Moves per Configuration']
y4 = df4['Average Number of Possible Moves per Configuration']
y5 = df5['Average Number of Possible Moves per Configuration']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average Number of Possible Moves per Configuration')
plt.savefig('Experiments_old/plot4.png')

plt.clf()

y1 = df1['Average Number of Avalanche matches occurred']
y2 = df2['Average Number of Avalanche matches occurred']
y3 = df3['Average Number of Avalanche matches occurred']
y4 = df4['Average Number of Avalanche matches occurred']
y5 = df5['Average Number of Avalanche matches occurred']
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.legend(["Grid Size (5, 5)", "Grid Size (7, 7)", "Grid Size (10, 10)", "Grid Size (15, 15)", "Grid Size (20, 20)"])
plt.xlabel('Number of Colors')
plt.ylabel('Average Number of Avalanche matches occurred')
plt.savefig('Experiments_old/plot5.png')