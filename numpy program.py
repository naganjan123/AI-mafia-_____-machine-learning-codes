#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("hello world")


# In[1]:


get_ipython().system('pip3 install numpy')


# # WE ARE GOING TO LEARN NUMPY

# In[2]:


import numpy as np


# In[4]:


arr=np.array([[1,2,3],[4,2,5]])


# In[5]:


type(arr)


# In[6]:


arr.shape


# In[9]:


np.ones((3,4))


# In[10]:


np.eye(3)


# In[13]:


arr=np.arr([[1,2,3,4],[5,6,7,8],[3,4,6,3]])
arr=arr.reshape(2,2,3)


# In[4]:


import numpy as np


# In[6]:


arr=np.array([[-1 , 2 ,0 , 4 ],
   [4  ,-0.5 , 6 , 0 ],
   [2.4 , 42 , 23 , 3],
   [3 , -3.4 , 34, 33]])


# In[7]:


arr


# In[9]:


arr[1:, :3:2]


# In[13]:


a=np.array([[1,3],[7,6]])
b=np.array([[4,6],[7,0]])


# In[14]:


print("\vertical stacking\n",np.vstack((a,b)))


# In[ ]:




