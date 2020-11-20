#!/usr/bin/env python
# coding: utf-8

# # Covid-19 Data Analysis Using Pandas
# 

# #### Project Done By - SYED ABDUR RAHMAN UDDIN,  " Copyright - rahmansyed862@gmail.com "

# #### Dataset used in this project is till April 2020. Downloaded from Kaggle. [ Small Dataset ]

# In[3]:


#importing libraries


# In[13]:


import pandas as pd


# In[14]:


import seaborn as sns


# In[15]:


import matplotlib.pyplot as plt


# In[16]:


#Assigning the Covid-19 dataset csv file to Data Object ( Any name for Data Object can be used )


# In[17]:


data = pd.read_csv(r"C:\Users\ROB\Downloads\4. covid_19_data.csv")


# In[103]:


data


# In[19]:


data.count()


# In[10]:


data.isnull()


# In[88]:


sns.set(color_codes=True)


# In[20]:


sns.heatmap(data.isnull())


# In[89]:


sns.distplot(data['Confirmed'])


# In[90]:


sns.distplot(data['Recovered'])


# In[91]:


sns.distplot(data['Deaths'])


# In[92]:


sns.jointplot(data['Confirmed'], data['Recovered'])


# In[93]:


sns.countplot(data['Deaths'])


# In[94]:


sns.lmplot(x='Confirmed', y='Deaths', data=data)


# In[95]:


sns.lmplot(x='Confirmed', y='Recovered', data=data)


# In[21]:


data.head(3)


# ### Q) Show Number of Confirmed, Deaths and Recovered Records.

# In[23]:


data.groupby('Region').sum()


# ### Q) Show total Number of Confirmed Cases in all Regions.

# In[25]:


data.groupby('Region')['Confirmed'].sum()


# ### Q) Show total Number of Death Cases in all Regions.

# In[27]:


data.groupby('Region')['Deaths'].sum()


# ### Q) Show total Number of Recovered Cases in all Regions.

# In[28]:


data.groupby('Region')['Recovered'].sum()


# ### Confirmed Cases in Descending Order.

# In[31]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False)


# ### Death Cases in Descending Order.

# In[32]:


data.groupby('Region')['Deaths'].sum().sort_values(ascending = False)


# ### Recovered Cases in Descending Order.

# In[33]:


data.groupby('Region')['Recovered'].sum().sort_values(ascending = False)


# ### Q ) Remove all the records where Confirmed Cases is Less than 10

# In[35]:


data.Confirmed<10


# In[36]:


data[data.Confirmed<10]


# In[37]:


data[~(data.Confirmed<10)]


# In[38]:


data=data[~(data.Confirmed<10)]


# In[39]:


data


# ### Q ) In which Region, Maximum number of Death Cases were recorded ?

# In[40]:


data.groupby('Region').Deaths.sum().sort_values(ascending=False)


# In[ ]:




