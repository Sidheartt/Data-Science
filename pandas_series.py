#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


label = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}


# how to make a series ?
# 

# In[10]:


pd.Series(data = my_data, index = label)


# In[11]:


pd.Series(my_data, label)


# In[13]:


pd.Series(arr, label)


# In[14]:


pd.Series(d)


# In[ ]:




