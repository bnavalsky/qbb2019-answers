#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def fixation (pop_size, allele_freq):
    count = 0
    while True:
        end_freq = (np.random.binomial((2* pop_size), allele_freq)/(2*pop_size))
        count += 1
        if end_freq == 0 or end_freq == 1:
            return (count)
        else: 
            allele_freq = end_freq
            
fixation_times = []
for i in range(1000):
    fixation_times.append(fixation(100, 0.5))

pop_sizes = [100, 1000, 10000]
fixation_times2 = {}
for pop_size in pop_sizes:
    fixation_times2[pop_size] = []
    for i in range(5):
        fixation_times2[pop_size].append(fixation(pop_size, 0.5))


mean2 = []
std_dev2 = []
for pop_size in pop_sizes:
    mean2.append(np.mean(fixation_times2[pop_size]))
    std_dev2.append(np.std(fixation_times2[pop_size]))

fixation_times3 = {}
allele_freqs = [0.2, 0.4, 0.6, 0.8]
for allele_freq in allele_freqs:
    fixation_times3[allele_freq] = []
    for i in range(100):
        fixation_times3[allele_freq].append(fixation(100, allele_freq))

mean3 = []
std_dev3 = []
for allele_freq in allele_freqs:
    mean3.append(np.mean(fixation_times3[allele_freq]))
    std_dev3.append(np.std(fixation_times3[allele_freq]))



fig, ax = plt.subplots()
plt.hist(fixation_times, bins = 100)
ax.set_xlabel("Generation Time to Fixation")
ax.set_ylabel("Frequency")
plt.title("Plot 1")
fig.savefig("timetofixation.png")
plt.close

fig,ax = plt.subplots()
ax.bar([x for x in range(1,len(pop_sizes)+1)], mean2, yerr = std_dev2)
ax.set_xlabel("Population Size")
ax.set_xticks([x for x in range(1,len(pop_sizes)+1)])
ax.set_xticklabels(["100", "1000", "10000"])
ax.set_ylabel("Generations to Fixation")
plt.title("Plot 2")
fig.savefig("varyingpopsize.png")
plt.close

fig,ax = plt.subplots()
ax.bar([x for x in range(1,len(allele_freqs)+1)], mean3, yerr= std_dev3)
ax.set_xlabel("Starting Allele Frequency")
ax.set_xticks([x for x in range(1,len(allele_freqs)+1)])
ax.set_xticklabels(["0.2", "0.4", "0.6", "0.8"])
ax.set_ylabel("Generations to Fixation")
plt.title("Plot 3")
fig.savefig("varyingallelefreq.png")
plt.close

def selection (pop_size, allele_freq, selection_coeff):
    count = 0
    while True:
        allele_count = allele_freq * (2*pop_size)
        prob = (allele_count*(1+selection_coeff))/((2*pop_size - allele_count) + (allele_count*(1+selection_coeff)))
        end_freq = (np.random.binomial((2* pop_size), prob)/(2*pop_size))
        count += 1
        if end_freq == 0 or end_freq == 1:
            return (count)
        else: 
            allele_freq = end_freq

selection_coeffs = [0, 0.2, 0.4, 0.6, 0.8, 1]
fixation_times4 = {}
for selection_coeff in selection_coeffs:
    fixation_times4[selection_coeff] = []
    for i in range(100):
        fixation_times4[selection_coeff].append(selection(100, 0.5, selection_coeff))


mean4 = []
std_dev4 = []
for selection_coeff in selection_coeffs:
    mean4.append(np.mean(fixation_times4[selection_coeff]))
    std_dev4.append(np.std(fixation_times4[selection_coeff]))

fig,ax = plt.subplots()
ax.bar([x for x in range(1,len(selection_coeffs)+1)], mean4, yerr= std_dev4)
ax.set_xlabel("Selection Coefficient")
ax.set_xticks([x for x in range(1,len(selection_coeffs)+1)])
ax.set_xticklabels(["0", "0.2", "0.4", "0.6", "0.8", "1"])
ax.set_ylabel("Generations to Fixation")
plt.title("Plot 4")
fig.savefig("varyingselctioncoefficient.png")
plt.close

