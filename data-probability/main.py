import csv
import numpy as np

with open("titanic.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  headers = next(data)
  data = list(data)
  data = np.array(data)
  

survived = np.array(data[:,[0]], dtype=int).flatten()
fare = np.array(data[:,[7]], dtype=float).flatten()

#empty lists to hold data from  the for loop
fare_survived = []
fare_not_survived = []

#ADD CODE: for loop and if/else statements
for index in range(0, len(fare)):
  if survived[index] == 1:
    fare_survived.append(fare[index])
  else:
    fare_not_survived.append(fare[index])

#ADD CODE: print lists
print(fare_survived)
print(fare_not_survived)