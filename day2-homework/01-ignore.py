#!/usr/bin/env python3

import sys
    
fly_ID = open(sys.argv[1])
c_tab = open(sys.argv[2])

all_info = {}



for line in fly_ID:
    col = line.rstrip("\n").split("\t")
    key = col[0].rstrip(" ")
    value = col[1]
    all_info[key] = value


for line in c_tab:
    col = line.rstrip("\n").split("\t")
    gene_id = col[8]
    if gene_id in all_info:
        value = all_info[gene_id]
        print(value + "\t" + line)
    elif sys.argv[3] == "p": #default_value.txt
        print("no match" + "\t" + line)
    else:    #ignore_nothing.txt
        continue
    
