#!/usr/bin/env python3

import numpy as np


s1 = "CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA"
s2 = "GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGCTGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCTCCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAGCTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCACCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACGGCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG"

test_s1= "GATTACA"
test_s2= "TAC"

gap = 300


# def sigma(s, t):
sigma = np.array([ [   91, -114,  -31, -123 ],
          [ -114,  100, -125,  -31 ],
          [  -31, -125,  100, -114 ],
          [ -123,  -31, -114,   91 ] ])
bases = { "A":0, "C":1, "G":2, "T":3 }

n = (len(s1)+1) 
m = (len(s2)+1)
scoring_matrix = np.zeros((n,m)) #seq 1 is vertical  
pathway_matrix = np.zeros(((n,m)), dtype = "str")


for j in range(m):
	scoring_matrix[0][j] = -(gap)*j
for i in range(n):
	scoring_matrix[i][0] = -(gap)*i	

for j in range(1,m):
	pathway_matrix[0][j] = "h"
for i in range(1, n):
	pathway_matrix[i][0] = "v"


for i in range(len(s1)):
	for j in range(len(s2)):
		all_scores = {
			'v' : scoring_matrix[(i, j+1)] - gap,
			'h': scoring_matrix[(i+1, j)] - gap,
			'd': scoring_matrix[i, j] + sigma[bases[s1[i]], bases[s2[j]]]
			}
		max_score = max(all_scores.values())
		scoring_matrix[i+1,j+1] = max_score

		score = None
		for direction in all_scores:
			if score == None or all_scores[direction] > all_scores[score]:
				score = direction
			elif all_scores[direction] == all_scores[score]:
				score = min(direction, score)
			pathway_matrix[i+1,j+1] = score

# print(scoring_matrix)
#print(pathway_matrix)
# print (scoring_matrix[len(s1), len(s2)])

i_count = (len(s1)-1)
j_count = (len(s2) -1)
seq1_align = ""
seq2_align = ""


while i_count != 0 or j_count!= 0:
	if pathway_matrix[i_count,j_count] == "d":
		seq1_align = s1[i_count]+ seq1_align
		seq2_align = s2[j_count]+ seq2_align
		i_count = i_count -1
		j_count = j_count -1
	if pathway_matrix[i_count,j_count] == "v":
		seq1_align = s1[i_count]+ seq1_align
		seq2_align = "-" + seq2_align
		i_count = i_count -1
	if pathway_matrix[i_count,j_count] == "h":
		seq1_align = "-"+ seq1_align
		seq2_align = s2[j_count]+ seq2_align
		j_count = j_count -1


print (scoring_matrix[len(s1), len(s2)])
print ("S1", seq1_align)
print("S2", seq2_align)


