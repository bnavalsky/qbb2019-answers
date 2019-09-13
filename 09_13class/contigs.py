#!/usr/bin/env python3

import sys
from fasta import FASTAReader

f = sys.stdin 
reader = FASTAReader(f)

contigs = []
for ident, sequence in reader:
    contigs.append(sequence)

sequence_length = []
for sequence in contigs:
    sequence_length.append(len(sequence))

print (min(sequence_length))
print (max(sequence_length))
print (sum(sequence_length)/len(contigs))

#N50 23,358.0

lengths_sorted = sorted(sequence_length, reverse= True)
contigs_sorted = sorted(contigs, reverse = True)

count = 0
for i, item in enumerate(lengths_sorted):
    count += item
    if count >= (sum(sequence_length)/2):
        break
print (i) #N50 contig
print (lengths_sorted[i]) #length of N50 contig


#time
# real    0m0.051s
# user    0m0.026s
# sys    0m0.010s



    
