#!/usr/bin/env python3

"""
create all.csv with FPKMs
"""
import sys
import pandas as pd
import os

metadata= sys.argv[1] #qbb_data/sample.csv
ctab_dir = sys.argv[2] #results/stringtie

fpkms = {}
column_name = {}
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    col = line.rstrip("\n").split(",")
    srr_id = col [0]
    new_name = col[1]+ "_" + col[2]
    print(new_name)
    
   
    ctab_path = os.path.join(ctab_dir, srr_id, "t_data.ctab")
    print(ctab_path)
    
    df = pd.read_csv (ctab_path, sep="\t", index_col="t_name")
    fpkms["gene_name"] = df.loc[:,"gene_name"]
    fpkms[new_name] = df.loc[:,"FPKM"]
    
    
    
        
    
    

df_fpkms = pd.DataFrame(fpkms)
# print (df_fpkms)q
# print (df_fpkms.describe()) print stats

pd.DataFrame.to_csv(df_fpkms, "renamed_all.csv")

