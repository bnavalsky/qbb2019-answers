#!/usr/bin/env python3

import sys
f = sys.stdin

count = 0
for line in f:
    fields = line.split("\t")
    for col in fields[11:]:
        if "NM:i:0" in col:
            count += 1

print (count)
