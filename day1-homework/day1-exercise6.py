#!/usr/bin/env python3
import sys
f = sys.stdin

count = 0
for line in f:
    fields = line.split("\t")
    if fields[2] == "2L":
        if 20000 >= int(fields[3]) >= 10000:
            count += 1
            
print(count)
