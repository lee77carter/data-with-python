import csv
import numpy as np

# ADD CODE: Convert titanic1.csv
with open("titanic1.csv", "r") as file:
    data = csv.reader(file,delimiter=",")
    headers = next(data)
    data_list = list(data)
    titanic_data1 = np.array(data_list)
    
# ADD CODE: Convert titanic2.csv     
with open("titanic2.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data2 = np.array(data_list)
  
# ADD CODE: Merge two datasets  
combined_data = np.concatenate((titanic_data1, titanic_data2), axis=0)

# ADD CODE: Print out shape and number of dimensions of merged dataset
print(combined_data.shape)
print(combined_data.ndim)

listify = combined_data.tolist()

titanic_lists_to_string = []
for titanic_lists in listify:
  titanic_string = (",").join(titanic_lists)
  titanic_lists_to_string.append(titanic_string)
complete_titanic = ("\n").join(titanic_lists_to_string)

# Write to new file
with open("titanic.csv", "w") as file:
  file.write("Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare\n")
  file.write(complete_titanic)
