#!/usr/bin/env python
# coding: utf-8

# 

# In[99]:


#importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')

#using pandas to read the database stored in the same folder
train_data=pd.read_csv('mnist_train.csv')


# In[100]:


#viewing column heads
train_data.head()


# In[101]:


#extracting data from the dataset and viewing them up close
a = train_data.iloc[2,1:].values


# In[102]:


#reshaping the extracted data into a reasonable size
a = a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[103]:


#preparing the data
#separating labels and dara values
df_x = train_data.iloc[:,1:]
df_y = train_data.iloc[:,0]


# In[104]:


#creating test and train sizes/batches
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state=4)


# In[105]:


#check data
x_train.head()


# In[106]:


#call rf classifier
rf = RandomForestClassifier(n_estimators=100)


# In[108]:


#class rf classifier
rf.fit(x_train, y_train)


# In[109]:


# Predictions on the test set
y_pred = rf.predict(x_test)

# Evaluate the model
accuracy = rf.score(x_test, y_test)
print(f"Accuracy on the test set: {accuracy}")


# In[110]:


#check prediction accuracy
s = y_test.values

#calculate number of correctly predicted values
count = 0
for i in range(len(pred)):
    if pred[i] == s[i]:
        count = count+1


# In[111]:


count


# In[112]:


#total values that te prediction code was run on
len(pred)


# In[113]:


#accuracy values
8090/8400

