#!/usr/bin/env python3

"""
create all.csv with FPKMs
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1] #Sxl
fpkm_file = sys.argv[2] #renamed_all.csv


df = pd.read_csv(fpkm_file, index_col="t_name")
goi = df.loc[:,"gene_name"] == gene_name

fpkms = df.drop(columns= "gene_name")
# print (fpkms.loc[goi,:])

male = fpkms.iloc[:,:8]
female =fpkms.iloc[:,8:]

fig, ax = plt.subplots(2)
ax[0].boxplot(male.loc[goi,:].T)
ax[1].boxplot(female.loc[goi,:].T)

#get list of column names 
column_names = fpkms.columns

ax[0].set_xticklabels(column_names[:8], rotation=30)
ax[1].set_xticklabels(column_names[8:], rotation=30)

# plt.title("FPKMs")
ax[0].set_ylabel("FPKMs")
ax[1].set_ylabel("FPKMs")
ax[0].set_xlabel("Sample Name")
ax[1].set_xlabel("Sample Name")
plt.title("Male and Female FPKMs")
plt.tight_layout()


fig.savefig("transcriptboxplot.png")
plt.close(fig)
