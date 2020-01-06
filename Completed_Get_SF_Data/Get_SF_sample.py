#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# In[2]:


with open('../Data/SF_Dict.json') as f:
    SF_Dict = json.load(f)

with open('../Data/SF_Features.json') as f:
    SF_Features = json.load(f)

with open('../Data/SF_ID.json') as f:
    SF_ID = json.load(f)


# In[3]:


file_name = "../Data/san_francisco-censustracts-2019-3-All-HourlyAggregate.csv"
df = pd.read_csv(file_name, 
                     usecols=['sourceid', 
                              'dstid', 
                              'hod', 
                              'mean_travel_time', 
                              'standard_deviation_travel_time'],
                     )


# In[4]:


# df.head()


# In[10]:


df_1 = df[0:1]
# df_1


# In[28]:


for start_id1 in SF_ID:
    df_rows1 = df["sourceid"] == start_id1
    for start_id2 in SF_ID:
        df_rows2 = (df[df_rows1])["dstid"] == start_id2
#     df_needed = df[df_rows2]
#     df_1 = pd.concat([df_1, df_rows2], axis = 1)

# print(df_needed)
    
    
    


# In[20]:


print(df_rows1)


# In[27]:


print(df_rows2)


# In[18]:


# df_needed = df[df_rows2]
# df_needed


# # In[ ]:


# df = pd.DataFrame(data=df_1)
# df


# # In[ ]:


# df_id = df.loc[df["sourceid"] == Get_SF_Features.id_list[0]]
# df_id.head()

