# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:07:42 2016

@author: Windows98
"""

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import linear_model


dataframe = np.loadtxt("C:/linear_model/data/3.19.txt").T
dataframe[:3]

X = dataframe[:,1:]
y = dataframe[:,0]
scaler = preprocessing.StandardScaler()
X_scaled = scaler.fit_transform(X)
standard = np.dot(X_scaled.T,X_scaled)
V, D = np.linalg.eig(standard)
condition_number = V.max() / V.min()
condition_number

X_center = X - X.mean(axis=0)
alphas = np.linspace(0, 0.1, num=100)
coeficients = []
for alpha in alphas:
    regressor = sm.OLS(y, sm.add_constant(X_center)).fit_regularized(L1_wt=0., alpha=alpha)
    coeficients.append(regressor.params[1:])
ks =  len(X) * np.array(alphas)
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(ks, np.array(zip(*coeficients)).T[:,0], "g*--", linewidth=2, markersize=10)
ax.plot(ks, np.array(zip(*coeficients)).T[:,1], "bh--", linewidth=2, markersize=7)
ax.set_xlabel(u"$k$", fontsize=30)
ax.set_ylabel(r"$\hat{\beta}$", fontsize=30)
ax.set_title(r"$\hat{\beta}-k$",fontsize=40)

print(regressor.summary())