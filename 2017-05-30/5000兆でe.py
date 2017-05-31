
# coding: utf-8

# # n=5000兆でヤコブ・ベルヌーイのeの定義は使えるか？

# https://twitter.com/nrmti/status/868980739047530496
# の検証

# In[1]:

import decimal


# In[2]:

decimal.Context()


# **5000兆円欲しい**

# In[3]:

want = decimal.Decimal(5000 * 10 ** 12)


# In[4]:

want


# 不要かもだけど

# In[5]:

one = decimal.Decimal('1')


# In[6]:

one


# [wikipediaの収束数列による定義を参照](https://ja.wikipedia.org/wiki/%E3%83%8D%E3%82%A4%E3%83%94%E3%82%A2%E6%95%B0)

# In[7]:

e = (one + one / want) ** want


# In[8]:

e


# In[9]:

import math


# In[10]:

math.e


# うーん、まあまあか

# ## おまけ: doubleでやると

# In[11]:

double_want = 5000 * 10 ** 12


# In[12]:

e = (1 + 1 / double_want) ** double_want


# In[13]:

e


# ダメダメですね
