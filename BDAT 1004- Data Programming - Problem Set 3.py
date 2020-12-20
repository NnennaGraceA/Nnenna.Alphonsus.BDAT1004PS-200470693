#!/usr/bin/env python
# coding: utf-8

# # Question 1 C#

# # Question 2 C#

# # Question 3 Python
# Housing
# Step 1. Import the necessary libraries
# Step 2. Create 3 differents Series, each of length 100, as follows:
# • The first a random number from 1 to 4
# • The second a random number from 1 to 3
# • The third a random number from 10,000 to 30,000
# Step 3. Create a DataFrame by joinning the Series by column
# Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter
# Step 5. Create a one column DataFrame with the values of the 3 Series and assign it
# to 'bigcolumn'
# Step 6. Ops it seems it is going only until index 99. Is it true?
# Step 7. Reindex the DataFrame so it goes from 0 to 299

# In[61]:


# Step 1. Import the necessary libraries
import pandas as pd
import random


# In[ ]:





# In[62]:


# Step 2. Create 3 differents Series, each of length 100:
   #First create 3 empty series

Series1 = []
Series2 = []
Series3 = []

# using the randint () Method in Python
for lenght in range(100):
    RandomSeries1 = random.randint(1, 4)
    RandomSeries2 = random.randint(1, 3)
    RandomSeries3 = random.randint(10000, 30000)
    
    Series1.append(RandomSeries1)
    Series2.append(RandomSeries2)
    Series3.append(RandomSeries3)


# In[63]:


Series1


# In[64]:


Series2


# In[65]:


Series3


# In[67]:


# using python print() function to print out the lenght and confirm it matches with the length specified

print (len(Series1))
print (len(Series2))
print (len(Series3))


# In[ ]:





# In[79]:


# Step 3. Create a DataFrame by joining the Series by column



#using function df = pd.DataFrame (zip()) to join the 3 series by column
df = pd.DataFrame(zip(Series1, Series2, Series3))
df


# In[75]:





# In[80]:


# Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter

df = df.rename(columns={0: "bedrs", 1:"bathrs", 2: "price_sqr_meter" })


# In[81]:


df


# In[ ]:





# In[89]:


# Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'

df["bigcolumn"] = Series1 + Series2 + Series3


# In[90]:


df


# In[ ]:





# In[102]:


# Step 6. Ops it seems it is going only until index 99. Is it true?


# In[ ]:





# In[ ]:


# Step 7. Reindex the DataFrame so it goes from 0 to 299


# In[ ]:





# In[ ]:





# # Question 4 Python
# Wind Statistics
# The data have been modified to contain some missing values, identified by NaN.
# Using pandas should make this exercise easier, in particular for the bonus question.
# You should be able to perform all of these operations without using a for loop or
# other looping construct.
# The data in 'wind.data' has the following format:
# Yr Mo Dy RPT VAL ROS KIL SHA BIR DUB CLA MUL CLO BEL
# MAL
# 61 1 1 15.04 14.96 13.17 9.29 NaN 9.87 13.67 10.25 10.83 12.58 18.50 15.04
# 61 1 2 14.71 NaN 10.83 6.50 12.62 7.67 11.50 10.04 9.79 9.67 17.54 13.83
# 61 1 3 18.50 16.88 12.33 10.13 11.17 6.17 11.25 NaN 8.50 7.67 12.75 12.71
# The first three columns are year, month, and day. The remaining 12 columns are
# average windspeeds in knots at 12 locations in Ireland on that day.

# In[74]:


# Step 1. Import the necessary libraries
import datetime
import pandas as pd
import numpy as np


# In[28]:


# Step 2. Import the dataset from this address

WindData_link = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data"
df = pd.read_csv(WindData_link)


# In[29]:


df.head()


# In[30]:


# Format the data
df = pd.read_csv(WindData_link, sep="\s+")


# In[31]:


df.head()


# In[32]:


# Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.

#Combining the Yr, Mo and Dy  so as to gate a datetime value

def to_datetime(Yr, Mo, Dy):
    dt = f"19{int(Yr)}-{int(Mo)}-{int(Dy)}"
    return dt


# In[33]:


df["datetime"] = df.apply(lambda x: to_datetime(x['Yr'], x['Mo'], x['Dy']), axis=1)


df.drop(["Yr","Mo", "Dy"], axis = 1, inplace = True)


# In[34]:


df.head()


# In[17]:


# Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.


# In[ ]:





# In[35]:


# Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].

# reference: https://stackoverflow.com/questions/29206612/difference-between-data-type-datetime64ns-and-m8ns

print(df["datetime"].dtypes)
df.set_index('datetime', inplace=True)


# In[36]:


df.head()


# In[37]:


# Step 6. Compute how many values are missing for each location over the entire record.They should be ignored in all calculations below.

MissingValues = df.isnull().sum()
MissingValues


# In[39]:


# Step 7. Compute how many non-missing values there are in total.


NonMissingValues = df.notnull().sum().sum()
NonMissingValues


# In[ ]:





# In[40]:


#Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
         # A single number for the entire dataset.
    
df.mean().mean()


# In[ ]:





# In[41]:


# Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
          # A different set of numbers for each location.

loc_stats = df.describe()
loc_stats


# In[ ]:





# In[42]:


# Step 10. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
           # A different set of numbers for each day
    
# Get the statistical record of the data  
day_stats = df.apply(pd.DataFrame.describe, axis=1)
day_stats.head()


# In[ ]:





# In[72]:


for i, month in enumerate(pd.Series(df.index).map(lambda x:pd._libs.tslibs.timestamps.Timestamp(x)).dt.month_name().unique(), 3):

    x = (pd.Series(pd.Series(df.index).map(lambda x:pd._libs.tslibs.timestamps.Timestamp(x)).dt.month == (i+1))).astype(int)
    x.index = df.index
    df[month]=x
df


# In[ ]:





# In[ ]:





# # Question 5 Python

# In[83]:


# Step 1. Import the necessary libraries


import datetime
import pandas as pd
import numpy as np


# In[84]:


# Step 2. Import the dataset from this address.

Link = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"


# In[86]:


# Step 3. Assign it to a variable called chipo.

chipo = pd.read_csv(Link, sep='\t')


# In[87]:


# Step 4. See the first 10 entries

chipo.head(10)


# In[ ]:





# In[90]:


# Step 5. What is the number of observations in the dataset?

NoOfObservations = chipo.shape[0]
print (NoOfObservations)


# In[ ]:





# In[91]:


# Step 6. What is the number of columns in the dataset?
NoOfColumns = chipo.shape[1]
print (NoOfColumns)


# In[ ]:





# In[92]:


# Step 7. Print the name of all the columns.

print(chipo.columns.values)


# In[ ]:





# In[95]:


# Step 8. How is the dataset indexed?

data = pd.Series(['order_id', 'quantity', 'item_name', 'choice_description', 'item_price'],
                 index=['N', 'G', 'A', 'L', 'P'])
data


# In[ ]:





# In[96]:


# Step 9. Which was the most-ordered item?

order_qty = chipo.groupby(['item_name'])[['item_name','quantity']].sum()
order_qty


# In[98]:





# In[99]:


# Step 10. For the most-ordered item, how many items were ordered?

most_ordered = order_qty[order_qty.quantity == order_qty.quantity.max()]
most_ordered


# In[ ]:





# In[100]:


# Step 11. What was the most ordered item in the choice_description column?

order_qty = chipo.groupby(['choice_description'])[['choice_description','quantity']].sum()
order_qty


# In[101]:


most_ordered = order_qty[order_qty.quantity == order_qty.quantity.max()]
most_ordered


# In[ ]:





# In[102]:


# Step 12. How many items were orderd in total?

order_qty['quantity'].sum()


# In[ ]:





# #  Step 13.
#       • Turn the item price into a float
#       • Check the item price type
#       • Create a lambda function and change the type of item price
#       • Check the item price type

# In[103]:


#  • Check the item price type

print(chipo['item_price'].dtypes)


# In[104]:


# • Turn the item price into a float

def turn_to_float(dollar_value):
    price = dollar_value[1:]
    price_float = float(price)
    return price_float

res = turn_to_float("$4.05")
res


# In[105]:


#  • Create a lambda function and change the type of item price

chipo['item_price'] = chipo.apply(lambda x: 
                                  turn_to_float(x['item_price']), axis=1)
chipo.head()


# In[106]:


#  • Check the item price type

print(chipo['item_price'].dtypes)


# In[ ]:





# In[107]:


# Step 14. How much was the revenue for the period in the dataset?

revenue = (chipo['quantity']*chipo['item_price']).sum()
revenue


# In[ ]:





# In[108]:


# Step 15. How many orders were made in the period?

no_of_orders = chipo['quantity'].sum()
no_of_orders


# In[ ]:





# In[110]:


# Step 16. What is the average revenue amount per order?


avg_rev_per_ord = (revenue/no_of_orders)
avg_rev_per_ord


# In[ ]:





# In[112]:


# Step 17. How many different items are sold?

chipo['item_name'].nunique()


# In[ ]:





# In[113]:


# Listing the 50 different items sold

chipo['item_name'].value_counts()


# In[ ]:





# In[ ]:





# # Question 6 Python
# Create a line plot showing the number of marriages and divorces per capita in the U.S. between 1867 and 2014. Label both lines and show the legend.
# Don't forget to label your axes!

# In[ ]:





# In[148]:


import pandas as pd
print(pd.__version__)
import matplotlib.pyplot as plt
from matplotlib.axis import Axis 
import numpy as np


# In[121]:





# In[163]:


# Import and define data

USMarriageLink = "C:/Users/HP/Downloads/us-marriages-divorces-1867-2014.csv"
df = pd.read_csv(USMarriageLink)
df.set_index('Year', inplace=True)


# In[187]:


ax = df.plot(lw=3, colormap='viridis', figsize =(15,8), marker='.', markersize=5, title= "NUMBER OF MARRIAGES & DIVORCES PER CAPITA IN THE U.S")
ax.set_xlabel("Year")
ax.set_ylabel("Divorce and Marriage per capita")


# In[ ]:





# In[ ]:





# # Question 7 Python
# Create a vertical bar chart comparing the number of marriages and divorces per capita in the U.S. between 1900, 1950, and 2000.
# Don't forget to label your axes!

# In[171]:


new_df = marriage_df[marriage_df.index.isin([1900, 1950,2000])]
new_df


# In[209]:


new_df[["Marriages_per_1000", "Divorces_per_1000"]].plot(kind='bar', colormap='plasma', figsize =(15,8))
ax.set_xlabel("Year")
ax.set_ylabel("Divorce and Marriage per capita")


# In[ ]:





# In[ ]:





# # Question 8 Python
# Create a horizontal bar chart that compares the deadliest actors in Hollywood. Sort
# the actors by their kill count and label each bar with the corresponding actor's name.
# Don't forget to label your axes!

# In[233]:


# Import and define data

ActorsLink = "C:/Users/HP/Downloads/actor_kill_counts.csv"
df = pd.read_csv(ActorsLink)
df


# In[234]:


import random
get_ipython().run_line_magic('matplotlib', 'inline')


# In[235]:


df.plot(kind='barh', colormap='autumn', figsize =(15,8))

#tried to label x and y axes and I got an error that rectangle object has no property xlabel and ylabel


# In[ ]:





# In[ ]:





# # Question 9 Python
# Create a pie chart showing the fraction of all Roman Emperors that were
# assassinated.
# Make sure that the pie chart is an even circle, labels the categories, and shows the
# percentage breakdown of the categories.

# In[261]:


# Import csv file and define data

RomanEmperors = "C:/Users/HP/Downloads/roman-emperor-reigns.csv"
df = pd.read_csv(RomanEmperors)
df.head()


# In[242]:


import matplotlib.pyplot as plotter


# In[294]:


values_count = df["Cause_of_Death"].value_counts()
values_count.plot(kind='pie', colormap = 'hot', autopct='%1.0f%%', figsize =(15,8))


# In[ ]:





# In[ ]:





# # Question 10 Python
# Create a scatter plot showing the relationship between the total revenue earned by
# arcades and the number of Computer Science PhDs awarded in the U.S. between
# 2000 and 2009.
# Don't forget to label your axes!
# Color each dot according to its year.

# In[306]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
Arcade= "C:/Users/HP/Downloads/arcade-revenue-vs-cs-doctorates.csv"
df = pd.read_csv(Arcade)


# In[307]:


df


# In[316]:


df.columns =['Years', 'Total_Arcade_Revenue', 'Computer_Science_PhDs_Awarded']


# In[317]:


df


# In[358]:


get_ipython().run_line_magic('matplotlib', 'inline')
x1='Years'
y1='Total_Arcade_Revenue'
x2='Years'
y2='Computer_Science_PhDs_Awarded'
figsize =(10,10)


# In[359]:


#g =sns.scatterplot(x='Total_Arcade_Revenue', y = 'Computer_Science_PhDs_Awarded')
plt.scatter(x1, y1, color = 'red')
plt.scatter(x2, y2, color = 'blue')
plt.title('Relationship Between Total Revenue Earned by Arcades And # of Computer Science PhDs awarded in the U.S')


# In[ ]:





# In[ ]:





# In[360]:


get_ipython().run_line_magic('matplotlib', 'inline')

df.plot(kind='scatter',x='Years',y='Total_Arcade_Revenue', legend='Years', colormap = 'hot', figsize =(10,10)) # scatter plot
df.plot(kind='scatter',x='Years',y='Computer_Science_PhDs_Awarded', legend='Years', colormap = 'hot', figsize =(10,10)) # scatter plot
plt.legend('Years')
plt.title('Relationship Between Total Revenue Earned by Arcades And # of Computer Science PhDs awarded in the U.S')


# In[ ]:





# In[365]:


get_ipython().run_line_magic('matplotlib', 'inline')

df.plot(kind='scatter', x='Total_Arcade_Revenue', y='Computer_Science_PhDs_Awarded', legend='Years', colormap = 'autumn', figsize =(10,10) )
plt.legend('Years')
plt.title('Relationship Between Total Revenue Earned by Arcades And # of Computer Science PhDs awarded in the U.S')


# In[ ]:





# In[ ]:




