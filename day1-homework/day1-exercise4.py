#!/usr/bin/env python3

import sys
f = sys.stdin

count = 0
for line in f:
    fields = line.split("\t")
    if fields[2] != "*":
        if count <= 10: 
            count += 1
            print (fields[2])
        