#!/bin/bash
args=("$@")
        python ~/Documents/Fan/scratch/code/combine_desc_clstr.py /Users/metagenomics/Documents/Fan/scratch/parsed_files/clstr_parsed/final/'${args[0]}'.'${args[1]}'.clstr.parsed.final /Users/metagenomics/Documents/Fan/scratch/parsed_files/blast_parsed/'${args[1]}'_'${args[0]}'_nucl_cdhit.blast.desc.parsed > /Users/metagenomics/Documents/Smita/combined/'${args[0]}'.'${args[1]}'.combined


#echo ${args[1]}
#perl /Users/metagenomics/Documents/Fan/scratch/code/sample.pl final/${args[0]}clstr final/${args[1]}final


