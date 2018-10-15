from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('module3/countries.csv')
#the headings of data are: country continent  year  lifeExpectancy  population  gdpPerCapita

#Let's say we want GDP data for Europe and Asia in 2007
#set(data.continents) would give us a set {} of the possible continents
data_2007 = data[data.year == 2007]
asia_2007 = data_2007[data_2007.continent == 'Asia']
europe_2007 = data_2007[data_2007.continent == 'Europe']

#just to check:
#print(asia_2007.head())
#print(europe_2007.head())

#To find the number of countries in our asia_2007 and europe_2007:
asia_2007_number = len(set(asia_2007.country))
europe_2007_number = len(set(europe_2007.country))
print(asia_2007_number, europe_2007_number)

#Mean and median GDP per capita:
asia_2007_gdp_mean = asia_2007.gdpPerCapita.mean()
asia_2007_gdp_median = asia_2007.gdpPerCapita.median()
europe_2007_gdp_mean = europe_2007.gdpPerCapita.mean()
europe_2007_gdp_median = europe_2007.gdpPerCapita.median()
print("Mean gdp in asia in 2007: ", asia_2007_gdp_mean)
print("Mean gdp in europe in 2007: ", europe_2007_gdp_mean)
print("Median gdp in asia in 2007: ", asia_2007_gdp_median)
print("Median gdp in europe in 2007: ", europe_2007_gdp_median)

#You can see that the numbers a higher in asia but this doesn't tell us much.
#Let's use a histogram
plt.subplot(2,1,1)
plt.title('Distribution of GDP per capita')
plt.hist(asia_2007.gdpPerCapita, 20, range = (0, 50000), edgecolor = 'black')
#the larger the 2n argument called bins the thiner the histograms become
plt.ylabel('Asia')
plt.subplot(2,1,2)
plt.hist(europe_2007.gdpPerCapita, 20, range = (0, 50000), edgecolor = 'black')
plt.ylabel('Europe')
plt.show()
