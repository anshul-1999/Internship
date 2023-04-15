#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[7]:


sns.set_style('darkgrid')
plt.rcParams['font.size'] = 15
plt.rcParams['figure.figsize'] = (10,7)
plt.rcParams['figure.facecolor'] = '#FFE5B4'


# In[61]:


data = pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')
data


# In[62]:


data.head()


# In[63]:


data.tail()


# In[64]:


data.info()


# In[65]:


data.isnull().values.any()


# In[66]:


data.describe()


# In[67]:


import seaborn as sns; sns.set(style="ticks", color_codes=True)
g = sns.pairplot(data, kind="reg")


# In[68]:


corrmat = data.corr()
sns.heatmap(corrmat, vmax=.8, square=True)


# In[72]:


get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")

plt.figure(figsize=(16, 10))
for i, key in enumerate(['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity','Dystopia Residual']):
    plt.subplot(3, 3, i+1)
    plt.xlabel(key)
    plt.scatter(data[key], data['Happiness Score'], alpha=0.5)


# In[74]:


df = data.groupby(['Country'], sort=False)['Happiness Score'].max().head(10)
df

