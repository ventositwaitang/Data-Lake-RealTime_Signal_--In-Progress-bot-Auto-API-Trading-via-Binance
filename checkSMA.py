#!/usr/bin/env python
# coding: utf-8

# # Run 'Streaming_SQL_for_Signal_Streamlit.ipynb' a while first, let it run in background

# In[5]:


#get_ipython().system('pip install ipykernel>=4.1.2')
#get_ipython().system('pip install pydeck')
#get_ipython().system('pip install streamlit')
#get_ipython().system('pip install pyngrok')
import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np


# In[6]:


from sqlalchemy import create_engine
engine = create_engine('sqlite:///C:/Users/User/Desktop/CryptoDB.db')
#engine = create_engine('sqlite:///CryptoDB.db')
#path = "/content/drive/MyDrive/Colab_Notebooks/"


# In[7]:


symbols = pd.read_sql('SELECT name FROM sqlite_master WHERE type="table"',
            engine).name.to_list()
symbols


# # No need to run Cells start with 'st.', they will be run in the last command together.

# In[ ]:


#streamlit run C:/Users/User/anaconda3/Lib/site-packages/ipykernel_launcher.py [ARGUMENTS]
st.title('Welcome to the live Trading App platform')
#DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)


# In[8]:


def applyTechnicals(df):
  df['SMA_7'] = df.c.rolling(7).mean() # binance's existing two indicators
  df['SMA_25'] = df.c.rolling(25).mean()
  df.dropna(inplace=True)


# In[9]:


def qry(symbol): 
  now = dt.datetime.utcnow()
  before = now - dt.timedelta(minutes=30)
  qry_str = f"""SELECT E,c FROM '{symbol}' WHERE E>='{before}'"""
  df = pd.read_sql(qry_str,engine)
  df.E = pd.to_datetime(df.E)
  df = df.set_index('E')
  df = df.resample('1min').last() #-- Or even resample("1ms")/('1min') depends on hardware --#
  df.dropna(inplace=True)     #-- Drop Missing data --#
  applyTechnicals(df)
  df['position'] = np.where(df['SMA_7']>df['SMA_25'], 1, 0)
  return df


# In[10]:


qry('BTCUSDT')


# ### Recall backtesting

# In[11]:


#if df['SMA_7']>df['SMA_25']: 
#  print('SELL',qry('BTCUSDT').position.diff()[-4])
#elif df['SMA_7']<df['SMA_25']:
#  print('BUY')
#test = qry('BTCUSDT')
#test['position'] = np.where(test['SMA_7']<test['SMA_25'], test['position']+1, test['position'])
#test['position'] = np.where(test['SMA_7']>test['SMA_25'], test['position']-1, test['position'])
#test


# In[12]:


def checkCorssSignal():  #backtesting
  for symbol in symbols:
    if len(qry(symbol).position) > 1: # at least two rows
       if qry(symbol).position[-1] and qry(symbol).position.diff()[-1]: #most recent cross detect
          st.write(symbol)


# ### No need to run↓

# In[ ]:


st.button('Get live SMA cross', on_click = checkCorssSignal())


# ### 1. Downloaded this file as raw Python file .py for Dashboard display.
# ### 2. Named it to checkSMA.py, later We can edit this .py AND save, to change The Web-dashboard App display
# ### 3. Put it in my current Folder
# # 4.***Open checkSMA.py file, comment'#'  ALL lines starting with 'get_ipython()'and '!', then save***
# ### 5. continue run below's command in .ipynb, The Web-dashboard App pop-up

# In[ ]:


#get_ipython().system('streamlit run checkSMA.py')


# 
