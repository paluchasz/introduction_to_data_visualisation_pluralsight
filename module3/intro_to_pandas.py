from matplotlib import pyplot as plt
import pandas as pd

data = {'year':[2008,2012,2016], 'attendees':[112,321,700], 'average age':[20,25,21]}
df = pd.DataFrame(data)
print(df) #this gives a table
print(df['year']) #this selects the year column, we call this a panda series

earlier_than_2013 = df['year'] < 2013 #this returns true when less than 2013 or false when greater than
print(df[earlier_than_2013]) #only prints the results which are true - we call this boolean indexing

plt.plot(df['year'], df['attendees']) #first argument gives points on x axis, 2nd on y axis
plt.plot(df['year'], df['average age'])
plt.legend(['attendees', 'average age'])
plt.show()
#To save as an imgage use plt.save('name') instead
