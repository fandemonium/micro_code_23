import sys
import os
import Bio
import re

l_id = []
l_seq = []

for line in open(sys.argv[1], 'r'):
    line = line.strip()
    if line.startswith(">"):
        id_des = line[1:]
        id_long = re.split("\|", id_des)[2]
        l_id.append(re.split("\|", id_des)[1])
        # '|' itself is a nulti-divider seperater. need \ to escape it to be used as a divider itself.
#print len(l_id)
    else:
        l_seq.append(line)

dict_seq = dict(zip(l_id, l_seq))

id_to_grab = []
with open(sys.argv[2]) as f:
    next(f)
    for line in f:
        lexemes = re.split("\t|_", line)
        gene_id = lexemes[1]
        id_to_grab.append(gene_id)

out = open(sys.argv[3], 'w')
for item in id_to_grab:
    out.write('>%s\n' % (item))
    out.write('%s\n' % dict_seq[item])
