from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('module3/countries.csv')

data_2007 = data[data.year == 2007]

# plt.scatter(data_2007.gdpPerCapita, data_2007.lifeExpectancy, 5) #3rd argument is size of dot
# plt.title('GDP per Capita against life expectancy in 2007')
# plt.xlabel('GDP per Capita')
# plt.ylabel('Life expectancy')
# plt.show()
#print(data_2007.gdpPerCapita.corr(data_2007.lifeExpectancy)) gives a correlation of 0.67 between the two

#However data is not linearly correlated so could use the log function:

# plt.scatter(np.log10(data_2007.gdpPerCapita), data_2007.lifeExpectancy, 5) #3rd argument is size of dot
# plt.title('Log of GDP per Capita against life expectancy in 2007')
# plt.xlabel('GDP per Capita')
# plt.ylabel('Life expectancy')
# plt.show()
#print(np.log10(data_2007.gdpPerCapita).corr(data_2007.lifeExpectancy)) #gives 0.80 correlation

years_sorted = sorted(set(data.year))

for given_year in years_sorted:
    data_year = data[data.year == given_year]
    plt.scatter(data_year.gdpPerCapita, data_year.lifeExpectancy, 5)
    plt.title(given_year)
    plt.xlim(0, 60000)
    plt.ylim(25, 85)
    plt.xlabel('GDP per Capita')
    plt.ylabel('Life expectancy')
    plt.show()
    #To save:
    #plt.savefig(str(given_year), dpi = 200) #first argument is the name, dpi = dots per inch
    #plt.clf() #Need to clear current plot before drawing the next one

    #could again do this with log scale instead
