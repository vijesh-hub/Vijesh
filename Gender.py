#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


get_ipython().run_line_magic('cd', 'documents\\\\python')


# In[3]:


female=pd.read_csv('Indian-Female-Names.csv',sep=",")


# In[4]:


male=pd.read_csv('Indian-Male-Names.csv',sep=",")


# In[5]:


male['name'].describe()


# In[6]:


female['name'].describe()


# In[7]:


female['name']=female['name'].drop_duplicates(keep='first')


# In[8]:


female=female.dropna()


# In[10]:


male['name']=male['name'].drop_duplicates(keep='first')


# In[11]:


male=male.dropna()


# In[12]:


male.info()


# In[13]:


female.info()


# In[14]:


B=[]
for word in male['name']:   
    if word[-1] =='i' or word[-1] =='a'or word[-1]=='y':
        continue
    else:
        B.append(word)
      
print("possible percentage of male is")
(len(B)/8519)*100


# In[15]:


B=[]
for word in female['name']:   
    if word[-1]=='i' or word[-1]=='a'or word[-1]=='y':  
        B.append(word)
      
print("possible percentage of female is")
(len(B)/6773)*100


# In[ ]:




