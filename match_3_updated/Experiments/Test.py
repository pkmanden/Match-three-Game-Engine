import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.stats import spearmanr

df = pd.read_csv('exp_2_data_2.csv')
# sns.set(style="whitegrid")

fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

x = df['Actual colors']
y = df['Max colors']
z = df['Mean non-deterministic score']

plt.xlabel("Actual colors")
plt.ylabel("Mean non-deterministic score")
# plt.set_zlabel("Mean non-deterministic score")

plt.plot(x, z)
plt.locator_params(integer=True)
# ===========================================================
# data = sns.load_dataset("exp_2_data_2.csv")
# x = df['Actual colors']
# y = df['Max colors']
# z = df['Mean non-deterministic score']
# print(np.mean(z))
# print(np.std(z))

corr, _ = spearmanr(x, z)
print('Spearmans correlation: %.3f' % corr)

# sns.relplot(x="Actual colors", y="Mean non-deterministic score", data=df)

plt.show()

# ===============================================

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# data = pd.read_csv('exp_2_data_2.csv', usecols=["Max colors", "Actual colors", "Mean non-deterministic score"])
#
# corr = data.corr()
# fig = plt.figure()
# ax = fig.add_subplot(111)
# cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
# fig.colorbar(cax)
# ticks = np.arange(0,len(data.columns),1)
# ax.set_xticks(ticks)
# plt.xticks(rotation=90)
# ax.set_yticks(ticks)
# ax.set_xticklabels(data.columns)
# ax.set_yticklabels(data.columns)
# plt.show()
