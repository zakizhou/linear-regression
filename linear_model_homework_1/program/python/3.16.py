# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 20:30:41 2016

@author: Windows98
"""

import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt


dataframe = np.loadtxt("C:/linear_model/data/3.16.txt").T
dataframe = sm.add_constant(dataframe)
dataframe[:3]

X = dataframe[:,[0, 2, 3]]
y = dataframe[:,1]
regressor = sm.OLS(y, X).fit()

print(regressor.summary())

prediction = regressor.predict()
residual = regressor.resid
fig,ax = plt.subplots(figsize=(10,10))
ax.scatter(prediction, residual , s=120, c="r")
ax.set_xlabel(u"$\hat{y}$",fontsize=30)
ax.set_ylabel(u"$\hat{e}$",fontsize=30)
ax.set_title(u"$\hat{e}-\hat{y}$",fontsize=30)