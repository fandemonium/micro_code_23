## input: anything resembles /Users/metagenomics/Documents/Databases/uniprotKB_taxa.txt
## for virus, bacteria, archaea, and fungi
import sys
import os
import re

for line in open(sys.argv[1]):
	line = line.rstrip() ## Remove extra spaces
	lexeme = line.split("\t") ## Split using tabs; store in array lexeme
	id = lexeme[0] ## First column is id
	tax = lexeme[-1] ## Second column is taxa
	domain = re.split("[|, |'|]", tax) ## Split on ", '"
	#print domain[1]
	if domain[1] != "Eukaryota": ## Extract only those lines that do not have Eukaryota
		print "%s\t%s" % (id, domain[1])
	if len(domain) != 3 and "Eukaryota" in domain[1] and "Fungi" in domain[5]: ## Extract only those lines with Eukaryota and Fungi in 1st and 5th tab (in second column)	
		print "%s\t%s" % (id, domain[5])
