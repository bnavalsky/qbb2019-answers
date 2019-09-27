#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

components = open(sys.argv[1])
fam_set= set()
fams = []
fam_colors = {}

for line in components:
    col = line.rstrip('\n').split(' ')
    x = float(col[2])
    y = float(col[3])
    fam = col[0]
    fams.append((fam, x, y))
    fam_set.add(fam)

fam_set = list(fam_set)
colors = ['#800000', '#9A6324', '#e6194B', '#808000', '#ffe119', '#469990', '#000075', '#000000', '#f032e6', '#aaffc3', '#a9a9a9']


for i in range(len(fam_set)):
    fam_colors[fam_set[i]] = colors[i]
 
 
fig, ax = plt.subplots()    
for point in fams:
    ax.scatter (point[1], point[2], color = fam_colors[point[0]])


plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.title("Principal Component Analysis")
fig.savefig( "component_plot.png" )
plt.close(fig)
