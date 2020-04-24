#!/usr/bin/env python3

from __future__ import division
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
matplotlib.rcParams.update({"axes.formatter.limits": (-3,3)})
plotStyles={"markersize":10,"markeredgewidth":2.0,"linewidth":2.0}
stepStyles={"markersize":12,"markeredgewidth":3.0,"linewidth":3.0,"where":"post"}

import numpy.random as rnd

k1=0.15
k2=0.07
ts=[0.0]   # a list of the times when a state change has occurred
states=[0] # state 0 is unfolded, state 1 is folded
tf=10000  # the final time of the simulation
time_unfolded = []
time_folded = []
unfolded = []
folded = []

while (ts[-1]<tf):
    
    # If we are in the unfolded state, figure out when the molecule transitions to the folded state.
    if states[-1] == 0:
        ts.append(ts[-1]+rnd.exponential(1/k1))
        states.append(1)
        time_unfolded.append(ts[-2])
        time_unfolded.append(ts[-1])

        
    # If we are in the folded state, figure out when the molecule transitions to the unfolded state.
    else:
        ts.append(ts[-1]+rnd.exponential(1/k2))
        states.append(0)
        time_folded.append(ts[-2])
        time_folded.append(ts[-1])


unfolded_wait_times = [ts[i]-ts[i-1] for i in range(1, len(ts), 2)]
folded_wait_times = [ts[i]-ts[i-1] for i in range(2, len(ts), 2)]

hist1, bins = np.histogram(unfolded_wait_times, bins=20)
width = (bins[1] - bins[0])
center1 = (bins[:-1] + bins[1:]) / 2
plt.bar(center1, hist1, align='center', width=width)
plt.title('Unfolded')
plt.xlabel('time (s)')
plt.ylabel('counts')
plt.show()

counts_unfold, bin_edges = np.histogram(unfolded_wait_times, bins=20)
sum_unfold = np.sum(counts_unfold)
unfold_width = bin_edges[1] - bin_edges[0]
div_unfold = sum_unfold*unfold_width
pdf_unfold = [x /div_unfold  for x in counts_unfold]
hist2, bins = np.histogram(folded_wait_times, bins=20)
width = (bins[1] - bins[0])
center2 = (bins[:-1] + bins[1:]) / 2
plt.bar(center2, hist2, align='center', width=width)
plt.title('Folded')
plt.xlabel('time (s)')
plt.ylabel('counts')
plt.show()

#Part2
counts_fol, bin_edges = np.histogram(folded_wait_times, bins=20)
sum_folded = np.sum(counts_fol)
fol_width = bin_edges[1] - bin_edges[0]
div_folded = sum_folded*fol_width
pdf_fol2 = [x /div_folded  for x in counts_fol]
time = np.arange(0, 50)
pdf_val = hist2/sum_folded/width
plt.bar(center2, hist2/sum_folded/width, align='center')
yvalue2 = k1 * np.exp(-k2*time)
plt.plot(time, yvalue2)
plt.title('Folded')
plt.xlabel('time (s)')
plt.ylabel('counts')
plt.show()

hist1, bins = np.histogram(unfolded_wait_times, bins=20)
pdf_val1 = hist1/sum_unfold/width
plt.bar(center1, hist1/sum_unfold/width, align='center')
yvalue1= k1 * np.exp(-k1*time)
plt.plot(time, yvalue1)
plt.title('Unfolded')
plt.xlabel('time (s)')
plt.ylabel('counts')
plt.show()

#Part 3
from scipy.optimize import curve_fit
def function(t, k):
    return -k * t + np.log(k +0.00001)


out1, out2 = curve_fit(function, center2, hist2/sum_folded/width)
k2_est= out1[0]

out3, out4 =curve_fit(function, center1, hist1/sum_folded/width)
k1_est = out3[0]

rel_error_k1 = np.absolute((k1_est-k1)/k1)
rel_error_k2 = np.absolute((k1_est-k1)/k1)

plt.bar(center2, hist2/sum_folded/width, align='center')
y_value2= k2_est * np.exp(-k2_est*time)
plt.plot(time, y_value2, label = rel_error_k2)
plt.title('Folded')
plt.legend()
plt.xlabel('time (s)')
plt.ylabel('counts')
plt.show()

plt.bar(center1, hist1/sum_unfold/width, align='center')
y_value1= k1_est * np.exp(-k1_est*time)
plt.plot(time, y_value1, label = rel_error_k1)
plt.title('Unfolded')
plt.legend()
plt.xlabel('time (s)')
plt.ylabel('counts')
plt.show()












