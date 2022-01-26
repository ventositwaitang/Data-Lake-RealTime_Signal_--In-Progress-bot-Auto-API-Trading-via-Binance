#!/usr/bin/env python
# coding: utf-8

# In[37]:


get_ipython().system('pip install ipykernel>=5.1.2')
get_ipython().system('pip install pydeck')
get_ipython().system('pip install streamlit')
get_ipython().system('pip install pyngrok')
import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np


# In[2]:


from sqlalchemy import create_engine
engine = create_engine('sqlite:///C:/Users/User/Desktop/CryptoDB.db')
#engine = create_engine('sqlite:///CryptoDB.db')
#path = "/content/drive/MyDrive/Colab_Notebooks/"


# In[3]:


symbols = pd.read_sql('SELECT name FROM sqlite_master WHERE type="table"',
            engine).name.to_list()
symbols


# In[14]:


st.title('Welcome to the live TA platform')
#streamlit %run C:\Users\User\anaconda3\Lib\site-packages\ipykernel_launcher.py [ARGUMENTS]
#DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)


# In[15]:


def applyTechnicals(df):
  df['SMA_7'] = df.c.rolling(7).mean() # binance's existing two indicators
  df['SMA_25'] = df.c.rolling(25).mean()
  df.dropna(inplace=True)


# **#Uncommant ALL following '#' while Cyrpto.db is running by Streaming_SQL_for_Signal_Streamlit.ipynb in local directory, to implement updated streaming data**

# In[26]:


def qry(symbol): 
  now = dt.datetime.utcnow()
  before = now - dt.timedelta(minutes=30)
  qry_str = f"""SELECT E,c FROM '{symbol}' WHERE E>='{before}'"""
  df = pd.read_sql(qry_str,engine)
  df.E = pd.to_datetime(df.E)
  df = df.set_index('E')
  df = df.resample('1min').last() #-- Or even resample("1ms")/('1s') depends on hardware --#
  df.dropna(inplace=True)     #-- Drop Missing data --#
  applyTechnicals(df)
  df['position'] = np.where(df['SMA_7']>df['SMA_25'], 1, 0)
  return df


# In[27]:


qry('BTCUSDT')


# In[18]:


# recall backtesting


# In[19]:


'''if df['SMA_7']>df['SMA_25']: 
  print('SELL',qry('BTCUSDT').position.diff()[-4])
elif df['SMA_7']<df['SMA_25']:
  print('BUY')'''
#test = qry('BTCUSDT')
#test['position'] = np.where(test['SMA_7']<test['SMA_25'], test['position']+1, test['position'])
#test['position'] = np.where(test['SMA_7']>test['SMA_25'], test['position']-1, test['position'])
#test


# In[38]:


def checkCorssSignal():  #backtesting
  for symbol in symbols:
    if len(qry(symbol).position) > 1: # at least two rows
       if qry(symbol).position[-1] and qry(symbol).position.diff()[-1]: #most recent cross detect
          st.write(symbol)


# In[39]:


st.button('Get live SMA cross', on_click = checkCorssSignal())


# In[ ]:


# Downloaded this file as raw Python file .py
# Named it to checkSMA.py
# Put it in my current Folder


# In[ ]:




