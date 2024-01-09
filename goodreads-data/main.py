import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("books.csv","r") as datafile:
    data = pd.read_csv(datafile,delimiter=",")

sns.scatterplot(x="average_rating", y="# num_pages", size="# num_pages", sizes=(20, 180), data=data)