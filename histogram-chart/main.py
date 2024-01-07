import matplotlib.pyplot as plt

movie_year = [2019,2019,2018,2018,2017,2016,2016,2016,2015,2015,2014,2014,2014,2013,2012,2012,2011,2010,2010,2009,2009,2008,2008,2007,2007,2007,2007,2006,2006,2006,2006,2005,2004,2004,2003,2003,2003,2002,2002,2001,1999,1999,1998,1998,1997,1996,1996,1995,1994,1993,1992,1991,1990,1989,1988,1987,1986,1985,1985,1984,1983,1982,1982,1982,1981,1979,1979,1979,1978,1978,1977,1977]

bins = 10

plt.hist(movie_year, bins, histtype="bar", color="#f5428d")

plt.xlabel("Year")

plt.ylabel("Number of Movies")

plt.title("Meryl Streep's Movie Career")

# tick marks
plt.xticks(range(1976, 2020, 4))
plt.yticks(range(0, 10, 2))
plt.savefig("meryl_streep_career.png")