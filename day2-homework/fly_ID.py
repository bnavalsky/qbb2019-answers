#!/usr/bin/env python3
import sys


for line in (sys.stdin):
    if "DROME" and "FBgn" not in line:
        continue
    
    col = line.rstrip("\n").split()
    
    
    fly_ac = col[-1]#last col
    ac= col[-2]#2nd to last col
          
    print (fly_ac, "\t", ac)  
        #fix tab