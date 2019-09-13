#!/usr/bin/env python3

import sys
from fasta import FASTAReader

f = sys.stdin 
reader = FASTAReader(f)

contigs = []
for ident, sequence in reader:
    contigs.append(sequence)
contigs_sorted = sorted(contigs, key = len)


sequence_length = []
for sequence in contigs:
    sequence_length.append(len(sequence))
    
lengths_sorted = sorted(sequence_length, reverse= True)



print (min(sequence_length))
print (max(sequence_length))
print (sum(sequence_length)/len(contigs))



count = 0
for i, item in enumerate(lengths_sorted):
    count += item
    if count >= (sum(sequence_length)/2):
        break
print (i) #N50 contig
print (lengths_sorted[i])