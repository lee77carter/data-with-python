import matplotlib.pyplot as plt

snack_scores = [45, 80, 2]

slice_labels = ["Almond Hersheys", "Ritz Crackers", "Pork Skins"]

colors = ["#8B4513", "#F4A460", "#D2B48C"]

plt.pie(snack_scores, labels=slice_labels, colors=colors)

plt.title("Nancy's Snack Chart")

fontsize=22

plt.savefig("snack_chart.png")