'''In this module we will compare Europe and Americas life expectancy in 1997. '''

from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('module3/countries.csv')
print(data.head())

#print(set(data.continent)) gives {'Asia', 'Africa', 'Oceania', 'Americas', 'Europe'}

data_1997 = data[data.year == 1997]
europe_1997 = data_1997[data_1997.continent == 'Europe']
americas_1997 = data_1997[data_1997.continent == 'Americas']

europe_1997_life_expectancy = europe_1997.lifeExpectancy
americas_1997_life_expectancy = americas_1997.lifeExpectancy

plt.subplot(2,1,1)
plt.title('Europe and Americas life expectancy in 1997.')
plt.hist(europe_1997_life_expectancy, 20, range = (56, 81), edgecolor = 'black')
plt.ylabel('Europe')
plt.subplot(2,1,2)
plt.hist(americas_1997_life_expectancy, 20, range = (56, 81), edgecolor = 'black')
plt.ylabel('Americas')
plt.show()

#once seen the histograms we might want to find out which countries in america are the
#outliers with low life expectancy. to check this can do:
print(americas_1997[americas_1997.lifeExpectancy < 65])
