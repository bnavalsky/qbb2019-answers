#!/usr/bin/env python3

"""
create an MA plot
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os 


name1 = sys.argv[1].split(os.sep)[-2] #takes only [-2] for column name
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name") #index_col adds tname
name2 = sys.argv[2].split(os.sep)[-2]                                      #to file
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkms = {name1: ctab1.loc[:,"FPKM"],
        name2: ctab2.loc[:, "FPKM"]}

df = pd.DataFrame(fpkms)
df += 1

r =df.loc[:,name2]
g =df.loc[:,name1]

m = np.log2(r/g)
a = .5 * np.log2(r*g)

fig, ax = plt.subplots()
ax.scatter(a, m, alpha = 0.2)
plt.title("SRR072893 and SRR072894")
plt.xlabel("A")
plt.ylabel("M")
fig.savefig("ma_plot.png")
plt.close(fig)