import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("exp_mean_median_results.csv")

df1 = dataframe[(dataframe['Grid Size'] == "(5, 5)") & (dataframe['Agent'] == "top_agent")]
x = df1['Number of Colors']
y = df1['Mean score per Game Setting']
plt.xlabel('Number of Colors')
plt.ylabel('Mean Score per Game Setting')
plt.plot(x, y, color='r')
df2 = dataframe[(dataframe['Grid Size'] == "(5, 5)") & (dataframe['Agent'] == "bottom_agent")]
x = df2['Number of Colors']
y = df2['Mean score per Game Setting']
plt.plot(x, y, color='b')
plt.legend(["Top Agent", "Bottom Agent"])
plt.title("5X5 Grid")
plt.show()