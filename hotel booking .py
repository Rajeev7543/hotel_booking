#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
warnings.filterwarnings("ignore")


# # Loading the dataset

# In[2]:


df = pd.read_csv(r"C:\Users\DELL\Downloads\archive (2)\hotel_booking.csv")


# # Exploratory dataset 

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[9]:


df.describe(include = 'object')


# In[10]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[11]:


df.isnull().sum()


# In[12]:


df.drop(['company','agent'], axis =1, inplace = True)
df.dropna(inplace = True)


# In[13]:


df.isnull().sum()


# In[14]:


df.describe()


# In[15]:


df = df[df['adr']<5000]


# # Data Analysis and Visualization

# In[16]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)


plt.figure(figsize = (5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(), edgecolor = 'k', width = 0.7)
plt.show()


# In[17]:


plt.figure(figsize = (8,4))
ax1= sns.countplot(x = 'hotel',hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotel', size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.show()


# In[18]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[19]:


City_hotel = df[df['hotel'] == 'City Hotel']
City_hotel['is_canceled'].value_counts(normalize = True)


# In[20]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
City_hotel = City_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[21]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Resort Hotel',fontsize = 30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(City_hotel.index, City_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[22]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot(x = 'month', hue = 'is_canceled', data = df, palette = 'bright')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status per month', size = 20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# # orange = cancled

# In[37]:


import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size
plt.figure(figsize=(12, 6))

# Set the title of the plot
plt.title('ADR per Month', fontsize=20)

# Group by month and calculate the sum of ADR for canceled reservations
sum_adr_per_month = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index()

# Create a bar plot using seaborn
sns.barplot(x='month', y='adr', data=sum_adr_per_month)

# Show the plot
plt.show()


# In[35]:


import matplotlib.pyplot as plt

cancelled_data = df[df['is_canceled'] == 1]
top_8_country = cancelled_data['country'].value_counts()[:8]

plt.figure(figsize=(8, 8))
plt.title('Top 8 Countries with Reservations Canceled')
plt.pie(top_8_country, labels=top_8_country.index, autopct='%.2f%%')
plt.show()


# In[32]:


df['market_segment'].value_counts()


# In[33]:


df['market_segment'].value_counts(normalize = True)


# In[34]:


cancelled_data['market_segment'].value_counts(normalize = True)


# In[48]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date',inplace = True)

not_cancelled_data = df[df['is_canceled'] == 0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True)
not_cancelled_df_adr.sort_values('reservation_status_date',inplace = True)

plt.figure(figsize = (20,6))
plt.title("Average Daily Rate")
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend()


# In[51]:


cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016') & (cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016') & (not_cancelled_df_adr['reservation_status_date']<'2017-09')]                                     


# In[53]:


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate',fontsize = 30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend(fontsize = 20)

