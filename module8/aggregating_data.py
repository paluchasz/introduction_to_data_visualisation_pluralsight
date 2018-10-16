from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('module8/obama.csv', parse_dates = ['year_month'])
#Due to 2nd argument pandas will interpret the first column as a series of time stamps
#and not as a series of strings

data_mean = data.groupby('year_month').mean() #groups data by the mean in each month
#print(data_mean)
data_median = data.groupby('year_month').median()
data_quarter = data.groupby('year_month').quantile(0.25)
data_top_quarter = data.groupby('year_month').quantile(0.75)

#.index gives the year_month column which is treated as an index in the data_mean frame
plt.plot(data_mean.index, data_mean.approve_percent, 'red')
plt.plot(data_median.index, data_median.approve_percent, 'orange')
plt.plot(data_quarter.index, data_quarter.approve_percent, 'green')
plt.plot(data_top_quarter.index, data_top_quarter.approve_percent, 'blue')

plt.legend(['mean', 'median', '25 percentile', '75 percentile'])

plt.plot(data.year_month, data.approve_percent, 'o', markersize = 2, alpha = 0.3)
#3rd argument ensures we only get points and no lines in between them

plt.xlabel('year and month')
plt.ylabel('approve_percent')
plt.title('Obamas approve percent')

plt.show()

#Another technique when data is too big is using random sampling. Can do
#dat.sample(frac = 0.1) to select a random 10% of data or use n=number to specify number of samples
