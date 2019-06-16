# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:28:55 2019

@author: Czarek
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

dataset = pd.read_csv('C:\\Users\\Czarek\\Desktop\\raport\\as.csv', sep=';')

corr = dataset.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)
plt.imshow(corr,cmap='hot',interpolation='nearest')



#korelacja miedzy CO(GT) a PT08.S1(CO)
x = dataset["CO(GT)"]
y = dataset["PT08.S1(CO)"]

stats = linregress(x, y)

m = stats.slope
b = stats.intercept

plt.scatter(x, y)
plt.plot(x, m * x + b, color="red")  

from sklearn.linear_model import LogisticRegression
from sklearn.datasets.samples_generator import make_blobs
# generate 2d classification dataset
X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)
# fit final model
model = LogisticRegression()
model.fit(X, y)