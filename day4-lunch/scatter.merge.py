#!/usr/bin/env python3

"""
take in two ctab files and make a scatter plot
"""
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

# ctab= pd.read_csv(sys.argv[1], sep="\t")
# fpkm = ctab.loc[:,"num_exons"] #colon is all rows, num_exons is header
# fpkm1 = ctab.loc[:, "length"]

name1 = sys.argv[1].split(os.sep)[-2] #takes only [-2] for column name
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name") #index_col adds tname
name2 = sys.argv[2].split(os.sep)[-2]                                      #to file
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkms = {name1: ctab1.loc[:,"FPKM"],
        name2: ctab2.loc[:, "FPKM"]}

        
df = pd.DataFrame(fpkms)
df += 1
df1 = np.log2(df)

x= df1.loc[:,name1]
y = df1.loc[:, name2]


# print(poly)
# print(poly_line)



fig, ax = plt.subplots()

# m, b = poly.polyfit(x, y , 1) 
best_fit = poly.polyfit(x, y, 1)
b = best_fit[0]
m= best_fit[1]
y_new = m * x + b




ax.scatter(x, y, s= 3, alpha = 0.15)
ax.plot(x, y_new, color="red")
plt.title("FPKMs")
plt.xlabel("log2(SRR072893 FPKM)")
plt.ylabel("log2(SRR072894 FPKM)")
fig.savefig("merged_scatter.png")
plt.close(fig)


# print(df[:,name1])


        
# my_data = np.log2(fpkms)
#
# fig, ax = plt.subplots()
# ax.scatter(my_data, bins = 100, density=True)
# ax.scatter2()
# ax.plot(x, ynorm, color = "red")
# ax.plot(x, y, color= "black")
# plt.title('FPKMs')
# plt.xlabel('')
# plt.ylabel('')