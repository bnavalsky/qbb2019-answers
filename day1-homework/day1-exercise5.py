#!/usr/bin/env python3

import sys
f = sys.stdin
#bring in as string, change to float so we get decimal 

total = 0
count = 0
for line in f:
    fields = line.split("\t")
    field4 = float(fields[4])
    if fields[2] != "*": 
        total += field4
        count += 1
        
print (total/count)

    

