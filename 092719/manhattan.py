#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import os
import numpy as np

colors = ['#42D4F4', '#911EB4']

for file_name in os.listdir(os.getcwd()):
    if file_name.endswith("qassoc"):
        quassoc_file = open(file_name)
        manhattan = {}
        for i, line in enumerate(quassoc_file):
            if i == 0:
                continue
            col = line.rstrip('\n').split()
            chromosome = col[0]
            p_value = col[-1]
            if p_value == "NA":
                continue
            manhattan.setdefault(chromosome, [])
            manhattan[chromosome].append(-1*np.log10(float(p_value)))
        previous_points = 0
        fig, ax = plt.subplots()  
        for i, chromosome in enumerate(manhattan):
            ax.scatter([x + previous_points for x in range(len(manhattan[chromosome]))], manhattan[chromosome], color = colors[i%2])
            x_vals = [x + previous_points for x in range(len(manhattan[chromosome]))]
            previous_points += len(manhattan[chromosome])
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False)
        plt.xlabel("Chromosomes")
        plt.ylabel("log-10(p-values)")
        plt.title (file_name)
        fig.savefig(file_name + ".png")
        plt.close(fig)
    
             
                