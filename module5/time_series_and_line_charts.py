from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('module3/countries.csv')

us = data[data.country == 'United States']
china = data[data.country == 'China']

# plt.plot(us.year, us.gdpPerCapita)
# plt.plot(china.year, china.gdpPerCapita)
# plt.xlabel('year')
# plt.ylabel('GDP per capita')
# plt.legend(['US', 'China'])
# plt.show()
#Using the above it hard to see the capita growth due to the large difference in magnitue
#Instead we want to have both Gdps starting at 100 say and see how they increase
#To do this we divide each GDP value by the first GDP value and multiply by 100,
#and we do this for us and china seperately.

#iloc stands for integer location, this gives the first value of the panda series
us_growth = us.gdpPerCapita / us.gdpPerCapita.iloc[0] * 100
china_growth = china.gdpPerCapita / china.gdpPerCapita.iloc[0] * 100

plt.plot(us.year, us_growth)
plt.plot(china.year, china_growth)
plt.xlabel('year')
plt.ylabel('GDP per capita')
plt.legend(['US', 'China'])
plt.title('GDP per capita growth (first year = 100)')
plt.show()
