# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:25:59 2016

@author: Windows98
"""

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import linear_model


dataframe = np.loadtxt("C:/linear_model/data/3.20.txt").T
dataframe = sm.add_constant(dataframe)
dataframe[:3]

X = dataframe[:,:-1]
y = dataframe[:,-1]
regressor = sm.OLS(y, X).fit()

print(regressor.summary())

X_center = X[:,1:] - X[:,1:].mean(axis=0)
standard = np.dot(X_center.T, X_center)
V, D = np.linalg.eig(standard)

Z = np.dot(X_center, D[:,[0, 3, 2]])
regressor = sm.OLS(y, sm.add_constant(Z)).fit()
print(regressor.summary())

params_center = np.dot(D[:,[0, 3, 2]],regressor.params[1:])
params_center

const = regressor.params[0] + np.dot(params_center, X[:,1:].mean(axis=0))
const