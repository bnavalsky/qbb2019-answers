#!/usr/bin/env python2

import hifive
import numpy as np
import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])

v = [0] * 7000
v2 = [0] * 7000


for i, line in enumerate(f1):
    if i == 0: 
        continue 
    fields = line.rstrip('\n').split('\t')
    if int(fields[1]) >= 5000000 and int(fields[1]) <= 40000000:
        index = (int(fields[1]) - 5000000) / 5000
        v[index] = float(fields[-2])
        
for i, line in enumerate(f2):
    if i == 0: 
        continue 
    fields = line.rstrip('\n').split('\t')
    if int(fields[1]) >= 5000000 and int(fields[1]) <= 40000000:
        index2 = (int(fields[1]) - 5000000) / 5000
        v2[index2] = float(fields[-2])


hic = hifive.HiC('project_file', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = np.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = np.log(data[:, :, 0] + 0.1)
data -= np.amin(data)

data_subset = data[np.where(v2 > 0), :]
sum_data_subset = np.sum(data_subset, axis=1)

R = np.corrcoef(sum_data_subset, v2)[0, 1]
# print(R)

# print(v2)





