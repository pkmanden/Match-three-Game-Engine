import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("exp_mean_median_results.csv")

df1 = dataframe[(dataframe['Grid Size'] == "(10, 10)") & (dataframe['Agent'] == "bottom_agent")]
x = df1['Number of Colors']
y = df1['Mean non-deterministic score after first move']
plt.xlabel('Number of Colors')
plt.ylabel('Mean non-deterministic score')
plt.plot(x, y)
plt.title("10X10 Grid")
plt.show()


