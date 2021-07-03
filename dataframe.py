#!/usr/bin/env python
# coding: utf-8

# # Pandas-DataFrame

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from numpy.random import randn


# In[4]:


np.random.seed(101)


# In[6]:


df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'],['W','X','Y','Z'])


# In[7]:


df


# In[ ]:




