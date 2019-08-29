#!/usr/bin/env python3

"""
hist.py; plot fkpm
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    col = line.rstrip("\n").split("\t")
    if float(col[11]) > 0:
        fpkms.append(float(col[11]))


my_data = np.log2(fpkms) #changes data to log 2 so that the grpah is more readable
mu = float(sys.argv[2]) #4.3 
sigma = float(sys.argv[3]) #1.9 

x = np.linspace(-15, 15, 100) #creates 100 x-values with linear spacing
y = stats.skewnorm.pdf (x, float(sys.argv[4]), loc=mu, scale=sigma) # a=-0.45
ynorm = stats.norm.pdf (x, mu, sigma)

fig, ax = plt.subplots()
ax.hist(my_data, bins = 100, density=True)
ax.plot(x, ynorm, color = "red")
ax.plot(x, y, color= "black")
plt.title('FPKMs')
plt.xlabel('log2(FPKM)')
plt.ylabel('log2(frequency)')
plt.text(-15, 0.15 , r'$\mu=4.3,\ \sigma=1.9,\ a=0.45$')
#add sigma values, etc to plot

fig.savefig("fpkms.png")
plt.close(fig)