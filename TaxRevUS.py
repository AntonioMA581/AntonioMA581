#!/usr/bin/env python
# coding: utf-8

# In[1]:


import statsmodels as sm
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.filters.hp_filter import hpfilter


# In[ ]:





# In[ ]:





# In[17]:


df = pd.read_excel('Tax_Revenue_US.xlsx', sheet_name="MTS_RcptOutlyDfctSur_20180701_2")
df = df.drop(['Current Month Gross Receipts Amount', 'Current Month Gross Outlay Amount'], axis=1)
df


# In[16]:


FY18 = df[0:12]
FY19 = df[12:24]
FY20 = df[24:36]
FY21 = df[36:48]
FY22 = df[48:60]
FY23 = df[60:]


# In[18]:


series = df['Current Month Deficit Surplus Amount']


# In[24]:


ciclo_defsur, tend_defsur = hpfilter(series, lamb=14400)


plt.style.use('seaborn')

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot( tend_defsur, label='Trend')
ax.plot( series, label='Current Month Deficit Surplus Amount')


ax.set_xlabel('Date')
ax.set_ylabel('Deficit Surplus Amount')
ax.set_title('Trend Deficit Surplus Amount')
ax.legend(loc='upper left')
plt.show()


# In[ ]:




