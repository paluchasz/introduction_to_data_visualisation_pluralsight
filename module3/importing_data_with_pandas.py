from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('countries.csv')
print(data.head()) #prints the first 5 rows of data.

afghanistan = data[data.country == 'Afghanistan'] #only return the rows where the country column has Afghanistan
plt.plot(afghanistan.year, afghanistan.gdpPerCapita)
plt.title("Afghanistan's GDP per capita")
plt.show()
