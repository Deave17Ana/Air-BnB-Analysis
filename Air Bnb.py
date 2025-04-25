#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ###**Loading Data**

# In[6]:


data = pd.read_csv('/Users/devanshverma/Desktop/Air/datasets.csv')


# In[7]:


data.head(5)


# **Understanding Data**

# In[8]:


data.info()


# In[9]:


data.dtypes


# In[10]:


data.shape


# In[15]:


data.describe()


# **Data Cleaning**

# In[16]:


data.isnull().sum()


# In[17]:


data.dropna(inplace = True)
data.isnull().sum()


# In[19]:


data.shape


# In[22]:


data.duplicated().sum()


# In[25]:


data[data.duplicated()]
data.drop_duplicates(inplace= True)


# In[26]:


data[data.duplicated()]


# In[27]:


data.dtypes


# In[29]:


data['id']=data['id'].astype(object)
data['host_id']=data['host_id'].astype(object)


#  **Data Analysis**

# EDA

# In[30]:


sns.boxplot(data=data, x='price')


# In[34]:


df= data[data['price']< 1500]


# In[35]:


sns.boxplot(data=df, x='price')


# In[45]:


plt.figure(figsize=(8,5))
sns.histplot(data=df, x='price',bins=100)
plt.title('Price Dis')
plt.show()


# In[44]:


df.dtypes


# In[47]:


plt.figure(figsize=(8,5))
sns.histplot(data=df, x='availability_365')
plt.title('Avaiability')
plt.show()


# In[48]:


data.dtypes 


# In[49]:


df.groupby(by='neighbourhood_group')['price'].mean()


# In[52]:


df['Price p bead'] = df['price']/df['beds']
df.head(5)


# In[53]:


df.groupby(by='neighbourhood_group')['Price p bead'].mean()


# In[54]:


df.columns


# In[56]:


sns.barplot(data=df, x='neighbourhood_group', y='price',hue='room_type')


# In[57]:


sns.scatterplot(data=df, x='number_of_reviews',y='price',hue='neighbourhood_group')


# In[60]:


sns.pairplot(data=df,vars=['price','minimum_nights','number_of_reviews','availability_365'],hue='room_type')


# In[61]:


sns.scatterplot(data=df, y='latitude',x='longitude',hue='room_type')


# In[63]:


df.dtypes


# In[71]:


corr = df[['latitude','longitude','price','minimum_nights','number_of_reviews','reviews_per_month','availability_365','beds']].corr()


# In[72]:


corr


# In[73]:


sns.heatmap(data=corr, annot=True)


# In[ ]:




