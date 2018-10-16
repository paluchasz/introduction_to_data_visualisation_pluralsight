from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('module3/countries.csv')

#Finding the 10 most populated countries in 2007
data_2007 = data[data.year == 2007]
top10 = data_2007.sort_values('population', ascending = False).head(10)

x = range(10)

plt.bar(x, top10.population / 10**6)
plt.xticks(x, top10.country, rotation = 'vertical')
plt.ylabel('population in millions')
plt.title('Top 10 most populated countries in 2007')
plt.show()
