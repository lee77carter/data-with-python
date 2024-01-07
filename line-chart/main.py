import matplotlib.pyplot as plt

month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

temp = [28,32,31,40,45,55,60,65,54,43,34,30]

# variables and line color
plt.plot(month,temp,color="#9370DB")

# x-axis label with a font size of 16.
plt.xlabel("Month", fontsize=16)

# y-axis label with a font size of 16.
plt.ylabel("Temp in Fahrenheit", fontsize=16)

# chart title & creation
plt.title("Avg Temperatures for 2018 in North Pole, Alaska")
 
plt.savefig("north_pole_temps.png")