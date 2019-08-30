#!/usr/bin/env python3
import sys
import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy

df = pd.read_csv(sys.argv[1], sep = "\t", index_col="t_name")
df2 = pd.read_csv(sys.argv[2], sep = "\t", index_col=0, header =None)
df3 =pd.read_csv(sys.argv[3], sep = "\t", index_col=0, header =None)
df4 =pd.read_csv(sys.argv[4], sep = "\t", index_col=0, header =None)



histone_data= {"FPKM": df.loc[:,"FPKM"],
               "H3K4me1": df2.iloc[:,-1],
               "H3K4me3": df3.iloc[:,-1],
               "H3K9me3": df4.iloc[:,-1]}

histone_df = pd.DataFrame(histone_data)

model = sm.formula.ols(formula= "FPKM ~ H3K4me1 + H3K4me3 + H3K9me3", data= histone_df)

ols_result =  model.fit()
# print (ols_result.summary())
print (ols_result.resid)
fig, ax = plt.subplots()
ax.hist(ols_result.resid, bins = 1000, range=(-100,100))
ax.set_xlim((-100,100))
plt.title('Residuals from Linear Regression')
plt.xlabel('residuals')
plt.ylabel('frequency')
fig.savefig("residuals.png")
plt.close(fig)