#!/bin/bash
args=("$@")

# go to folder : /Users/metagenomics/Documents/Smita/test_folder/test_blast_parsed
# run through the cmd : ls *.parsed | perl -ne '/(.*?)_(.*)_nucl_(.*)/;print $1." ".$2."\n"' | awk '{print $1,$2}' | xargs -n 2 /Users/metagenomics/Documents/Smita/code/copy_combine_clstr_wrap.sh $1 $2

#echo ${args[1]}
#perl /Users/metagenomics/Documents/Smita/sample.pl final/${args[0]}clstr final/${args[1]}final

python ~/Documents/Smita/code/combine_desc_clstr.py /Users/metagenomics/Documents/Smita/test_folder/test_clstr/${args[0]}_${args[1]}.clstr.parsed /Users/metagenomics/Documents/Smita/test_folder/test_blast_parsed/${args[0]}_${args[1]}_nucl_cdhit.blast.desc.parsed > /Users/metagenomics/Documents/Smita/combined/${args[0]}.${args[1]}.combined
