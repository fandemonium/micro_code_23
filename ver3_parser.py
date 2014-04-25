#!/usr/bin/python
## same as count_clst_abundance.py

import sys
import os
from collections import Counter
import re

# print "USAGE: ver3_parser.py <input_file> <out_file>"

j =0

f = open(sys.argv[1], 'rU')

for line in f:
	line = line.rstrip()
	if line.startswith(">Cluster"):
		string = re.split("\n", line)
		id = string[0]
		if j == 0:
			print '%s\t' % (id),
		else:
		# print contig name followed by the total number j	
			print '%s\t%s\n%s\t' % (contig,j,id),

	if line.endswith("*"):
		lexeme = re.split("\t| |>|\...", line)
		contig = lexeme[3]
		#print contig + '\t'
		j = 1

	else:
		j = j+1
# print last line 
print '%s\t%s' % (contig,j)
