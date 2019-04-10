#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib
import matplotlib.pyplot as plt


age=[17.5,22,29.5,44.5,64.5,80]
deaths=[38,36,24,20,18,28]

plt.plot(age,deaths,"b.")
plt.xlabel("age")
plt.ylabel("Number of deaths")
plt.show()


# In[3]:


import numpy as np

mean_age = np.mean(age)
mean_deaths = np.mean(deaths)

def least_squares(age,mean_age,deaths,mean_deaths):
    ls_age = 0
    ls_deaths = 0
    for i in range(len(age)):
        ls_age += (age[i] - mean_age)*(deaths[i] - mean_deaths)
        ls_deaths += (age[i] - mean_age)**2 
    
    m = ls_age / ls_deaths
    c = mean_deaths - m*mean_age
    
    return m,c


# In[4]:


slope,intercept = least_squares(age,mean_age,deaths,mean_deaths)

plt.scatter(age, deaths)
axes=plt.gca()
x_intercept = np.array(axes.get_xlim())
y_intercept = intercept + slope * x_intercept


plt.plot(x_intercept, y_intercept, '--')
plt.show()


# In[5]:


pred =slope*40 + intercept
print("number of deaths for ages 40 = ",pred)

pred=slope*60 + intercept
print("number of deaths for ages 60 = ",pred)


# In[6]:


from scipy.stats import pearsonr
r,p=pearsonr(age,deaths)
r,p


# In[7]:


print("Since the coefficient is negative,there is a slight negative linear relationship between the taken age and corresponding deaths values")


# In[ ]:




