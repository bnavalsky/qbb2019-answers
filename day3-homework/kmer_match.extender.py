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

target_sequences = {}

for ident, sequence in reader:
    sequence = sequence.upper()
    target_sequences[ident] = sequence
    for i in range(0, len(sequence) - k +1):
        kmer = sequence[i:i+k]
        if kmer in target_kmers:
            target_kmers[kmer].append((ident, i))#(start, sequence name)
        else:
            target_kmers[kmer] = [(ident, i)]
 
 # TAGTAGCATGCATACGTACGACTACGTCAGACTGACTGGT
 #        |           |
 #        i   :   end
     
elongated_seq = []
     
for ident, sequence in reader2:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k +1):
        query_kmer = sequence[i:i+k]
        if query_kmer in target_kmers:
            variable = target_kmers[query_kmer]
            for tident, ti in variable:
                tsequence = target_sequences[tident] 
                end = ti+k -1 
                end1 = i+k -1
                newtsequence = query_kmer
                while True:
                    if len(tsequence)-1 == end:
                        break
                    newtseq = tsequence[end + 1]
                    newseq = sequence[end1 + 1]
                    if newtseq == newseq:
                        end += 1
                        end1 += 1
                        newtsequence += tsequence[end]
                    else:
                        elongated_seq.append(newtsequence)
                        break
                
for item in sorted(elongated_seq, key= len, reverse = True):
    print(item)
    
    
            




    
    #turn kmer counter into kmer matcher
    #build hashtable
    #find matches
    #find smallest and extend, don't extend from both ends
