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


female['name']=female['name'].drop_duplicates(keep='first')    #drops all the duplicate entries and keeps the first entry


# In[8]:


female=female.dropna()                                     # drops all the null and missing values


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
    if word[-1] =='i' or word[-1] =='a'or word[-1]=='y':     #checks whelther the last letter of the name is 'i' or 'a' or 'y'
        continue
    else:
        B.append(word)                                        # if the condition is not satisfied , names are stored in a list
      
print("possible percentage of male is")
(len(B)/len(male))*100                                         # 75.12 % of the male name passes the model


# In[15]:


B=[]
for word in female['name']:   
    if word[-1]=='i' or word[-1]=='a'or word[-1]=='y':      #checks whelther the last letter of the name is 'i' or 'a' or 'y'
        B.append(word)                                       #if the condition is satisfied , names are stored in a list
      
print("possible percentage of female is")
(len(B)/len(female))*100                                     #62.70% of the female names passes the model


# In[ ]:




