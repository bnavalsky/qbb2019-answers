#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Andrew Gordus
April, 2020
Quantitative Biology and Biophysics (AS.020.674/250.644)	Spring 2020
Gordus Lab #1
"""
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

file_path = '/Users/cmdb/qbb2019-answers/20200424/'
fname  = 'bob_pairing.xlsx'
fname = file_path + fname

data_df = pd.read_excel(fname)

#convert dataframe to numpy array
data_n = data_df.to_numpy()
data_n = pd.to_numeric(data_n[:,0])
data_n.resize(18,100)
data_n = np.transpose(data_n)

# Set up the matplotlib figure
f, axes = plt.subplots(2, 2, figsize=(7, 7))
sns.despine(left=True)
sns.set(style="whitegrid")


sns.swarmplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[0, 0])

sns.violinplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[0, 1])

sns.boxplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[1, 0])

sns.barplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[1, 1])
#
# plt.show()
#Gaussian

x=data_n
mu = np.nanmean(x)
sigma = np.nanstd(x)
#print(mu, sigma)

def gauss_fun(x,mu,sigma):
    p= (1/(np.sqrt(2 * np.pi * np.square(sigma)))) * np.exp(-(np.square(x-mu))/(2*np.square(sigma)))
    return p
#print(gauss_fun(data_n, mu, sigma))

# Gaussian logL
def gausslogl(x):
    logL= np.log(gauss_fun(x, mu, sigma))
    likely_sum= np.sum(logL)
    return likely_sum
#print(gausslogl(x))

# Double Gaussian LogL
# NOTE: It returns the NEGATIVE of the logL
def dgausslogl(params,x):
    mu1 = params[0]
    mu2 = params[1]
    sigma1 = params[2]
    sigma2 = params[3]
    w = params[4]
    
    if mu1 < np.nanmin(x):
        mu1 = np.nanmin(x)
    elif mu1 > np.nanmax(x):
        mu1 = np.nanmax(x)
    if mu2 < np.nanmin(x):
        mu2 = np.nanmin(x)
    elif mu2 > np.nanmax(x):
        mu2 = np.nanmax(x)
    if sigma1 <= 0:
        sigma1 = 0.0001
    if sigma2 <= 0:
        sigma2 = 0.0001
    if w <= 0:
        w = 0.0001
    elif w > 1:
        w = 1 - 0.0001
    
    dp = w * np.exp((-(x-mu1)**2) / (2 * sigma1**2)) / (2 * np.pi * sigma1**2)**(1/2) +\
        (1-w) * np.exp((-(x-mu2)**2) / (2 * sigma2**2)) / (2 * np.pi * sigma2**2)**(1/2)
    dlnl = np.sum(np.log(dp))
    return dlnl


# Find most probable values for double gaussian
params0 = [mu-sigma,mu+sigma,sigma,sigma,0.6]
result = minimize(dgausslogl, params0, args=data_n, method='Nelder-Mead')
print(result)

#BIC: Best model has LOWEST BIC
k = [2,5]
logL1 = gausslogl(x)
logL2 = -dgausslogl(result.x,x)

def bic_calc(n,k,logL1,logL2):
    b=k*np.log(n) - 2*np.log(result.x)
    return b

print(bic_calc(100,k[0],logL1,logL2))
# print(-dgausslogl(result.x,x))

BIC = (bic_calc(100,k[0],logL1,logL2))
print(BIC[0], BIC[1])
