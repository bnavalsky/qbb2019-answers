#!/usr/bin/env python3

import sys

#col 13 is "protein coding"
#col 1 is chromosome
protein_coding_genes = {}
list_of_locations = []

for line in open(sys.argv[1]):
    col = line.rstrip("\n").split()
    if (col[0] == '3R' and col[2] == "gene") and "protein_coding" in line:
        start_location = int(col[3])
        end_location = int(col[4])
        gene = col[13]
        protein_coding_genes[(start_location, end_location)] = gene
        list_of_locations.append((start_location, end_location)) 
        
list_of_locations.sort()

lo =0
hi = len(list_of_locations)-1
mid = 0
number_of_iterations = 0
position = 21378950

while (lo < hi):
   
    mid = int((hi + lo)/2) #finds median
    number_of_iterations += 1
    if (position < list_of_locations[mid][1]):
        list_of_locations = list_of_locations[:mid]
    elif (position > list_of_locations[mid][0]):
        list_of_locations = list_of_locations[(mid+1):]
    else:
       break
    hi = len(list_of_locations)-1
gene_name = protein_coding_genes[list_of_locations[0]]
print (gene_name)

location_list = list(list_of_locations[0])
distance1 = abs(location_list[0]-position)
distance2 = abs(location_list[1]-position)

if distance1 > distance2:
    print(distance2)
else:
    print(distance1)
    
print (number_of_iterations)


    


        
    
        

        
