# Visualization displaying relationship between columns from the dataset. The number of pages of each book and each book’s average rating. 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("books.csv","r") as datafile:
    data = pd.read_csv(datafile,delimiter=",")

sns.scatterplot(x="average_rating", y="# num_pages", size="# num_pages", sizes=(20, 180), data=data)

plt.xlabel("Average Rating")
plt.ylabel("Number of Pages")
plt.title("Average Rating and Number of Pages")
plt.savefig("Ratings-and-Pages.png")