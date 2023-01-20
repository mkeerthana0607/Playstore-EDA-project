#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[5]:


app_data = pd.read_csv("C:/Users/mkeer/Downloads/playstoreliveproj Drive FIle/playstoreliveproj/playstore_apps.csv")


# In[ ]:


# understanding the data


# In[9]:


app_data.head()


# In[10]:


app_data.tail()


# In[11]:


app_data.shape


# In[27]:


app_data.describe()


# In[ ]:


app_data.columns


# In[ ]:


app_data.nunique()


# In[ ]:


app_data['Category'].unique()


# In[ ]:


# cleaning the data  ---- finding & removing null values, dropping redundant data, checking for outliers. 
# (removing duplicate rows, remove irrelevant values from each column, export the cleaned file)


# In[28]:


app_data.isnull().sum()


# In[31]:


app_data.dropna(axis = 0, inplace = True)


# In[ ]:


correlation = app_data.corr()


# In[ ]:


sns.heatmap(correlation, xticklabels = correlation.columns, yticklabels = correlation.columns, annot = True)


# In[ ]:


sns.pairplot(app_data)


# In[ ]:


sns.relplot(x = 'Category', y = 'Installs', hue = 'Type', dataset = app_data)


# In[ ]:


sns.distplot(app_data['Category'])


# In[32]:


app_data.to_csv("D:/Playstore project/cleaned_app_data.csv")


# In[30]:


app_data.shape


# In[33]:


# app_review data


# In[34]:


review_data = pd.read_csv("C:/Users/mkeer/Downloads/playstoreliveproj Drive FIle/playstoreliveproj/playstore_reviews.csv")


# In[35]:


review_data.head()


# In[36]:


review_data.tail()


# In[37]:


review_data.describe()


# In[38]:


review_data.shape


# In[39]:


review_data.columns


# In[41]:


review_data.nunique()


# In[43]:


review_data['Sentiment'].unique()


# In[44]:


review_data.isnull().sum()


# In[45]:


review_data.dropna(axis = 0, inplace = True)


# In[46]:


review_data.to_csv("D:/Playstore project/cleaned_review_data.csv")


# In[ ]:




