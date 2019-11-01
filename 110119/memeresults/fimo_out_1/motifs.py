#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np
import seaborn as sns

f = open(sys.argv[1])

locations = []

for line in f:
    if line.startswith("motif_id"):
        continue
    col = line.strip().split()
    if col != []:
        locations.append(col[3])

locations = locations[:-3]
locations = [int(x) for x in locations]

fig, ax = plt.subplots ()
ax = sns.distplot(a =locations, bins = 10)

fig.savefig("motifs.png")
plt.close(fig)