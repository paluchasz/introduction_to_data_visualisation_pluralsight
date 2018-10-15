from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('module3/countries.csv')

us = data[data.country == 'United States']
china = data[data.country == 'China']

# For absolute population growth
# plt.plot(us.year, us.population)
# plt.plot(china.year, china.population)
# plt.xlabel('years')
# plt.ylabel('population')
# plt.title('Population growth')
# plt.legend(['US', 'China'])
# plt.show()

#For relative population growth
us_growth = us.population / us.population.iloc[0] * 100
china_growth = china.population / china.population.iloc[0] * 100

plt.plot(us.year, us_growth)
plt.plot(china.year, china_growth)
plt.xlabel('years')
plt.ylabel('population')
plt.title('Population growth (100 in first year)')
plt.legend(['US', 'China'])
plt.show()
