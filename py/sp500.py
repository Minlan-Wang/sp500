#!/usr/bin/env python
# coding: utf-8

# # List of S&P 500 companies
# 
# Retreive from https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
# 
# output: 'sp500.csv'

# In[1]:


from datetime import datetime
import io
import os
import re
import shutil

import numpy as np
import pandas as pd
import wikipedia as wp

pd.options.mode.chained_assignment = None  # default='warn'
pd.set_option('display.max_rows', 600)

# -*- encoding: utf-8 -*-
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


get_ipython().run_cell_magic('javascript', '', 'IPython.OutputArea.prototype._should_scroll = function(lines) {\n    return false;\n}')


# In[3]:


def get_table(title, filename, match, use_cache=False):

    if use_cache and os.path.isfile(filename):
        pass
    else:
        html = wp.page(title).html()
        df = pd.read_html(io.StringIO(html), header=0, match=match)[0]
        
        df.to_csv(filename, header=True, index=False, encoding='utf-8')
            
    df = pd.read_csv(filename)
    return df


# In[4]:


title = 'List of S&P 500 companies'
filename = 'sp500.csv'
sp500 = get_table(title, filename, match='Symbol')

# dd/mm/YY H:M:S
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print('{} (retrieved {})'.format(title, dt_string))
sp500


# In[ ]:




