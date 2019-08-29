#!/usr/bin/env python3

"""
take in two ctab files and make a scatter plot
"""
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

list_of_files = sys.argv[1:]
fpkms = {}

for ctab_file in enumerate(list_of_files):
    name = ctab_file.split(os.sep)[-2]
    ctab = pd.read_csv(ctab_file, sep="\t", index_col="t_name")
    fpkms[name] = ctab.loc[:,"FPKM"]
     
    