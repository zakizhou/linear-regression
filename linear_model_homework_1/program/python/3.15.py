# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:04:21 2016

@author: Windows98
"""
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import boxcox
from sklearn import preprocessing


dataframe = np.loadtxt("C:/linear_model/data/3.15.txt").T
dataframe = sm.add_constant(dataframe)
dataframe[:3]


# split target variable and information matrix
X = dataframe[:,:2]
y = dataframe[:,2]
regressor = sm.OLS(y, X).fit()
# fit our ols model
print(regressor.summary())


prediction = regressor.predict()
residual = regressor.resid
fig,ax = plt.subplots(figsize=(10,10))
ax.scatter(prediction, residual , s=120, c="r")
ax.set_xlabel(u"$\hat{y}$",fontsize=30)
ax.set_ylabel(u"$\hat{e}$",fontsize=30)
ax.set_title(u"$\hat{e}-\hat{y}$",fontsize=30)


u = np.sqrt(y)
regressor_u = sm.OLS(u, X).fit()
print(regressor_u.summary())


prediction = regressor_u.predict()
residual = regressor_u.resid
fig,ax = plt.subplots(figsize=(10,10))
ax.scatter(prediction, residual , s=120, c="b")
ax.set_xlabel(u"$\hat{u}$",fontsize=30)
ax.set_ylabel(u"$\hat{e}$",fontsize=30)
ax.set_title(u"$\hat{e}-\hat{u}$",fontsize=30)


scaler = preprocessing.StandardScaler()
X[:,1] = scaler.fit_transform(X[:,1])
lmbdas = np.linspace(-1, 1, num=20)
rsses = []
for lmbda in lmbdas:
    boxcox_y = boxcox(y, lmbda=lmbda)
    regressor = sm.OLS(boxcox_y, X).fit()
    rss = np.square(regressor.resid).sum()
    rsses.append(rss)
    
fig,ax = plt.subplots(figsize=(10,10))
ax.scatter(lmbdas, rsses , s=120, c="g")
ax.set_xlabel(u"$\lambda$",fontsize=30)
ax.set_ylabel(u"$RSS$",fontsize=30)
ax.set_title(u"$RSS-\lambda$",fontsize=30)