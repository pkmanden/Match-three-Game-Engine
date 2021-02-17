from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
import matplotlib.pyplot as plt
import pandas as pd

# Take data from grid sizes
dataframe = pd.read_csv("exp_game_results_1.csv")
df1 = dataframe[dataframe['Grid Size'] == "(5, 5)"]
df11 = df1.groupby('Actual Colors', as_index=False).mean()
df2 = dataframe[dataframe['Grid Size'] == "(10, 10)"]
df22 = df2.groupby('Actual Colors', as_index=False).mean()
df3 = dataframe[dataframe['Grid Size'] == "(15, 15)"]
df33 = df3.groupby('Actual Colors', as_index=False).mean()
df4 = dataframe[dataframe['Grid Size'] == "(20, 20)"]
df44 = df4.groupby('Actual Colors', as_index=False).mean()


# ----------------------------Grid Size 5X5
x = df11['Actual Colors']

y1 = df11['Avg No. of Regenerations until valid board generation']
y2 = df11['Avg No. of Times Matches Occurred during init']
y3 = df11['Avg No. of Deadlocks during init']
y4 = df11['Avg No. of Shuffles/Deadlocks Occurred per move']
y5 = df11['Avg No. of Moves until Shuffle occurs per game setting']
y6 = df11['Avg score per Game Setting']
y7 = df11['Avg Valid Moves Made']
y8 = df11['Avg No. of Possible/Playable Moves per configuration']
y9 = df11['Avg No. of Avalanche Matches']
y10 = df11['Probability that the game will start']

fig = plt.figure()

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharex=host)
par2 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.parasites.append(par2)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

fig.add_axes(host)

p1, = host.plot(x, y1, label="Avg no. of regenerations until valid board generation")
p2, = par1.plot(x, y2, label="Avg no. of times matches occurred during init")
p3, = par2.plot(x, y3, label="Avg no. of deadlocks during init")

# host.set_xlim(0, 2)
# host.set_ylim(0, 2)
# par1.set_ylim(0, 4)
# par2.set_ylim(1, 65)

host.set_yscale('symlog')
par1.set_yscale('symlog')
par2.set_yscale('symlog')
host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of regenerations")
par1.set_ylabel("Avg no. of times matches occurred during init")
par2.set_ylabel("Avg no. of deadlocks during init")

host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())

# plt.show()
plt.title("5 X 5 Grid")
plt.savefig('5_5_1.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# -----------------
host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharex=host)
par2 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.parasites.append(par2)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

fig.add_axes(host)

p1, = host.plot(x, y7, label="Avg valid moves made per game setting")
p2, = par1.plot(x, y6, label="Avg score per game setting")
p3, = par2.plot(x, y9, label="Avg no. of avalanche matches per game setting")


host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg valid moves made")
par1.set_ylabel("Avg score per game setting")
par2.set_ylabel("Avg no. of avalanche matches")

host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())

# plt.show()
plt.title("5 X 5 Grid")
plt.savefig('5_5_2.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()
# ---------------
host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y4, label="Avg no. of shuffles/deadlocks occurred per move")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of shuffles/deadlocks occurred")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("5 X 5 Grid")
plt.savefig('5_5_3.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# --------

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y8, label="Avg no. of possible/playable moves per configuration")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of possible/playable moves")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("5 X 5 Grid")
plt.savefig('5_5_4.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# --------

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y10, label="Probability that the game will start")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Probability that the game will start")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("5 X 5 Grid")
plt.savefig('5_5_5.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()


# ----------------------------Grid Size 10X10
x = df22['Actual Colors']

y1 = df22['Avg No. of Regenerations until valid board generation']
y2 = df22['Avg No. of Times Matches Occurred during init']
y3 = df22['Avg No. of Deadlocks during init']
y4 = df22['Avg No. of Shuffles/Deadlocks Occurred per move']
y5 = df22['Avg No. of Moves until Shuffle occurs per game setting']
y6 = df22['Avg score per Game Setting']
y7 = df22['Avg Valid Moves Made']
y8 = df22['Avg No. of Possible/Playable Moves per configuration']
y9 = df22['Avg No. of Avalanche Matches']
y10 = df22['Probability that the game will start']

fig = plt.figure()

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharex=host)
par2 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.parasites.append(par2)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

fig.add_axes(host)

p1, = host.plot(x, y1, label="Avg no. of regenerations until valid board generation")
p2, = par1.plot(x, y2, label="Avg no. of times matches occurred during init")
p3, = par2.plot(x, y3, label="Avg no. of deadlocks during init")

# host.set_xlim(0, 2)
# host.set_ylim(0, 2)
# par1.set_ylim(0, 4)
# par2.set_ylim(1, 65)
host.set_yscale('symlog')
par1.set_yscale('symlog')
par2.set_yscale('symlog')
host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of regenerations")
par1.set_ylabel("Avg no. of times matches occurred during init")
par2.set_ylabel("Avg no. of deadlocks during init")

host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())

# plt.show()
plt.title("10 X 10 Grid")
plt.savefig('10_10_1.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# -----------------
host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharex=host)
par2 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.parasites.append(par2)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

fig.add_axes(host)

p1, = host.plot(x, y7, label="Avg valid moves made per game setting")
p2, = par1.plot(x, y6, label="Avg score per game setting")
p3, = par2.plot(x, y9, label="Avg no. of avalanche matches per game setting")


host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg valid moves made")
par1.set_ylabel("Avg score per game setting")
par2.set_ylabel("Avg no. of avalanche matches")

host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())

# plt.show()
plt.title("10 X 10 Grid")
plt.savefig('10_10_2.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()
# ---------------
host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y4, label="Avg no. of shuffles/deadlocks occurred per move")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of shuffles/deadlocks occurred")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("10 X 10 Grid")
plt.savefig('10_10_3.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# --------

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y8, label="Avg no. of possible/playable moves per configuration")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of possible/playable moves")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("10 X 10 Grid")
plt.savefig('10_10_4.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# --------

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y10, label="Probability that the game will start")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Probability that the game will start")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("10 X 10 Grid")
plt.savefig('10_10_5.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# ----------------------------Grid Size 15X15
x = df33['Actual Colors']

y1 = df33['Avg No. of Regenerations until valid board generation']
y2 = df33['Avg No. of Times Matches Occurred during init']
y3 = df33['Avg No. of Deadlocks during init']
y4 = df33['Avg No. of Shuffles/Deadlocks Occurred per move']
y5 = df33['Avg No. of Moves until Shuffle occurs per game setting']
y6 = df33['Avg score per Game Setting']
y7 = df33['Avg Valid Moves Made']
y8 = df33['Avg No. of Possible/Playable Moves per configuration']
y9 = df33['Avg No. of Avalanche Matches']
y10 = df33['Probability that the game will start']

fig = plt.figure()

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharex=host)
par2 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.parasites.append(par2)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

fig.add_axes(host)

p1, = host.plot(x, y1, label="Avg no. of regenerations until valid board generation")
p2, = par1.plot(x, y2, label="Avg no. of times matches occurred during init")
p3, = par2.plot(x, y3, label="Avg no. of deadlocks during init")

# host.set_xlim(0, 2)
# host.set_ylim(0, 2)
# par1.set_ylim(0, 4)
# par2.set_ylim(1, 65)
host.set_yscale('symlog')
par1.set_yscale('symlog')
par2.set_yscale('symlog')
host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of regenerations")
par1.set_ylabel("Avg no. of times matches occurred during init")
par2.set_ylabel("Avg no. of deadlocks during init")

host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())

# plt.show()
plt.title("15 X 15 Grid")
plt.savefig('15_15_1.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# -----------------
host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharex=host)
par2 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.parasites.append(par2)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

fig.add_axes(host)

p1, = host.plot(x, y7, label="Avg valid moves made per game setting")
p2, = par1.plot(x, y6, label="Avg score per game setting")
p3, = par2.plot(x, y9, label="Avg no. of avalanche matches per game setting")


host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg valid moves made")
par1.set_ylabel("Avg score per game setting")
par2.set_ylabel("Avg no. of avalanche matches")

host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())

# plt.show()
plt.title("15 X 15 Grid")
plt.savefig('15_15_2.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()
# ---------------
host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y4, label="Avg no. of shuffles/deadlocks occurred per move")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of shuffles/deadlocks occurred")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("15 X 15 Grid")
plt.savefig('15_15_3.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# --------

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y8, label="Avg no. of possible/playable moves per configuration")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of possible/playable moves")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("15 X 15 Grid")
plt.savefig('15_15_4.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# --------

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y10, label="Probability that the game will start")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Probability that the game will start")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("15 X 15 Grid")
plt.savefig('15_15_5.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# ----------------------------Grid Size 20X20
x = df44['Actual Colors']

y1 = df44['Avg No. of Regenerations until valid board generation']
y2 = df44['Avg No. of Times Matches Occurred during init']
y3 = df44['Avg No. of Deadlocks during init']
y4 = df44['Avg No. of Shuffles/Deadlocks Occurred per move']
y5 = df44['Avg No. of Moves until Shuffle occurs per game setting']
y6 = df44['Avg score per Game Setting']
y7 = df44['Avg Valid Moves Made']
y8 = df44['Avg No. of Possible/Playable Moves per configuration']
y9 = df44['Avg No. of Avalanche Matches']
y10 = df44['Probability that the game will start']

fig = plt.figure()

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharex=host)
par2 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.parasites.append(par2)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

fig.add_axes(host)

p1, = host.plot(x, y1, label="Avg no. of regenerations until valid board generation")
p2, = par1.plot(x, y2, label="Avg no. of times matches occurred during init")
p3, = par2.plot(x, y3, label="Avg no. of deadlocks during init")

# host.set_xlim(0, 2)
# host.set_ylim(0, 2)
# par1.set_ylim(0, 4)
# par2.set_ylim(1, 65)
host.set_yscale('symlog')
par1.set_yscale('symlog')
par2.set_yscale('symlog')
host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of regenerations")
par1.set_ylabel("Avg no. of times matches occurred during init")
par2.set_ylabel("Avg no. of deadlocks during init")

host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())

# plt.show()
plt.title("20 X 20 Grid")
plt.savefig('20_20_1.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# -----------------
host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharex=host)
par2 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.parasites.append(par2)

host.axis["right"].set_visible(False)

par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

fig.add_axes(host)

p1, = host.plot(x, y7, label="Avg valid moves made per game setting")
p2, = par1.plot(x, y6, label="Avg score per game setting")
p3, = par2.plot(x, y9, label="Avg no. of avalanche matches per game setting")


host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg valid moves made")
par1.set_ylabel("Avg score per game setting")
par2.set_ylabel("Avg no. of avalanche matches")

host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())

# plt.show()
plt.title("20 X 20 Grid")
plt.savefig('20_20_2.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()
# ---------------
host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y4, label="Avg no. of shuffles/deadlocks occurred per move")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of shuffles/deadlocks occurred")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("20 X 20 Grid")
plt.savefig('20_20_3.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# --------

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y8, label="Avg no. of possible/playable moves per configuration")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Avg no. of possible/playable moves")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("20 X 20 Grid")
plt.savefig('20_20_4.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()

# --------

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
fig.add_axes(host)
p1, = host.plot(x, y10, label="Probability that the game will start")

host.set_xlabel("Actual number of colors")
host.set_ylabel("Probability that the game will start")
host.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), borderaxespad=0.)
host.axis["left"].label.set_color(p1.get_color())

# plt.show()
plt.title("20 X 20 Grid")
plt.savefig('20_20_5.jpg', format='jpeg', dpi=100, bbox_inches='tight')

plt.clf()



