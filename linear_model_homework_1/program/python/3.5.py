# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:25:41 2016

@author: Windows98
"""

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


dataframe = np.loadtxt("C:/linear_model/data/3.5.txt").T
dataframe = sm.add_constant(dataframe)
dataframe[:3]


X = dataframe[:,:2]
y = dataframe[:,2]
regressor = sm.OLS(y, X).fit()
print(regressor.summary())

fig,ax = plt.subplots(figsize=(10,10))
ax.scatter(X[:,1], y , s=120, c="r")
ax.set_xlabel(u"$X$",fontsize=30)
ax.set_ylabel(u"$y$",fontsize=30)
ax.set_title(u"$y-X$",fontsize=30)

ploter = sns.JointGrid(x=X[:,1], y=y)
img = ploter.plot_joint(plt.scatter, s=60, color="g")
regressor.predict([1., 15.3])