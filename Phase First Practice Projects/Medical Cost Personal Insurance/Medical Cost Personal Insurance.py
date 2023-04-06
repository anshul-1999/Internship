#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import preprocessing
from scipy import stats


# In[2]:


df=pd.read_csv('insurance.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[8]:


corr=df.corr()
corr


# In[10]:


sns.heatmap(corr,annot=True)


# In[11]:


df.head(100)


# In[12]:


sns.countplot(df['children'])


# In[14]:


sns.countplot(df['sex'])


# In[17]:


sns.pairplot(df)


# In[18]:


df.head()


# In[22]:


sns.distplot(df['charges'])


# In[23]:


stats.probplot(np.log(df['bmi']),plot=plt)


# In[72]:


stats.probplot(np.log(df['age']),plot=plt)


# In[26]:


df.select_dtypes(include=['object'])


# In[28]:


sns.countplot(df['sex'],hue=df['children'])


# In[37]:


from sklearn.preprocessing import LabelEncoder
# instantiate labelencoder object
so = preprocessing.LabelEncoder()
so.fit(df['sex'])
df['sex']=so.transform(df['sex'])

so.fit(df['smoker'])
df['smoker']=so.transform(df['smoker'])

so.fit(df['region'])
df['region']=so.transform(df['region'])


# In[42]:


df['region'].head()


# In[43]:


df.head()


# In[61]:


X=df.iloc[:,:-1]
y=df.iloc[:,-1]
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)


# In[62]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)


# In[63]:


from sklearn.metrics import accuracy_score
regressor.score(X_train,y_train)


# In[75]:



from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

polynomial_features= PolynomialFeatures(degree=7)
x_poly = polynomial_features.fit_transform(X)

model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
r2 = r2_score(y,y_poly_pred)
print(rmse)
print(r2)


# In[65]:


from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X, y)


# In[66]:


from sklearn.model_selection import train_test_split
train_features, test_features, train_labels, test_labels = train_test_split(X, y, test_size = 0.25, random_state = 42)


# In[67]:


from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 100, random_state = 42)
rf.fit(train_features, train_labels);


# In[68]:


predictions = rf.predict(test_features)
errors = abs(predictions - test_labels)
mape = 100 * (errors / test_labels)


# In[69]:


accuracy = 100 - np.mean(mape)
print(accuracy)


# In[70]:


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)


# In[59]:


from sklearn.model_selection import cross_val_score


# In[60]:


score = regressor.score(X_test, y_test)
print(score)


# In[ ]:




