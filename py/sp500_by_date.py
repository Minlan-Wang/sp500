#!/usr/bin/env python
# coding: utf-8

# # S&P 500 by date
# 
# Get snapshot of S&P 500 components at a given date

# In[1]:


from datetime import datetime
import os
import shutil
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
pd.set_option('display.max_rows', 600)

# -*- encoding: utf-8 -*-
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


get_ipython().run_cell_magic('javascript', '', 'IPython.OutputArea.prototype._should_scroll = function(lines) {\n    return false;\n}')


# In[3]:


# Date to use for snapshot of S&P 500 components.
snap_shot = '2009-10-01'


# In[4]:


def get_table(filename):

    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col='date')
        return df


# In[5]:


filename = 'S&P 500 Historical Components & Changes(12-30-2023).csv'
df = get_table(filename)
df.tail()


# In[6]:


# Convert ticker column from csv to list, then sort.
df['tickers'] = df['tickers'].apply(lambda x: sorted(x.split(',')))
df.tail()


# In[7]:


# Number of symbols in the first row.
l = list(df['tickers'].head(1))[0]
len(l)


# In[8]:


# Get the synbols on snap_shot date by filtering df by rows before or on the snap_shot date,
# then picking the last row.
df2 = df[df.index <= snap_shot]
last_row = df2.tail(1)
last_row


# In[12]:


past = last_row['tickers'].iloc[0]
print('*'*40, f'S&P 500 on {snap_shot}', '*'*40)
print(past)


# In[13]:


# Get current S&P500 list.
filename = 'sp500.csv'
current = pd.read_csv(filename)
current = sorted(list(current['Symbol']))
#print(current)


# In[14]:


# Show what's been added and removed since snap_shot date.

added = list(set(current) - set(past))
print('*'*40, f'ADDED since {snap_shot}', '*'*40)
print(added)
print()

removed = list(set(past) - set(current))
print('*'*40, f'REMOVED since {snap_shot}', '*'*40)
print(removed)


# In[ ]:




