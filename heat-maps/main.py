import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("tips.csv", "r") as csvfile:
  tips = pd.read_csv(csvfile, delimiter=",")

tips_pivoted = tips.pivot_table(
    values="tip", index=["size"], columns=["time"]
)

fig = sns.heatmap(tips_pivoted, annot=True, cmap="coolwarm")

fig.set_ylim(0,6)

plt.xlabel("Time")
plt.ylabel("Size")
plt.title("Avg Tip Amount($) According to Time & Party Size")
plt.savefig("tips_heatmap.png")