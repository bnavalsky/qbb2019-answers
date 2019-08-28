#!/usr/bin/env python3

"""
Match kmers from FASTA files  
"""

from fasta import FASTAReader
import sys

reader = FASTAReader(open(sys.argv[1]))
reader2 = FASTAReader(open(sys.argv[2]))

k = int(sys.argv[3])
target_kmers = {}


for ident, sequence in reader:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k +1):
        kmer = sequence[i:i+k]
        if kmer in target_kmers:
            target_kmers[kmer].append((ident, i))#(start, sequence name)
        else:
            target_kmers[kmer] = [(ident, i)]
 
     
for ident, sequence in reader2:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k +1):
        query_kmer = sequence[i:i+k]
        if query_kmer in target_kmers:
            for tident, ti in target_kmers[query_kmer]: 
                print (tident, ti, i, query_kmer, sep="\t")




    
    #turn kmer counter into kmer matcher
    #build hashtable
    #find matches
    #find smallest and extend, don't extend from both ends
