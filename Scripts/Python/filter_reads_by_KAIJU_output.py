#!/usr/bin/env python3

# Possition arguments:
# arg1 = input_R1.fq.gz
# arg2 = input_R2.fq.gz
# arg3 = KAIJU_output.gz
# arg4 = out_good_R1.fq
# arg5 = out_good_R2.fq
# arg6 = out_bad_R1.fq
# arg7 = out_bad_R2.fq

# usage:
# filter_reads_by_namelist.py inp_R1_read.fq.gz inp_R2_read.fq.gz KAIJI_output.gz out_good_R1 out_good_R2 out_bad_R1 out_bad_R2

from Bio import SeqIO
import sys
import gzip

# open zipped: reads R1 (arg1), R2 (arg2) and list_of_headers (arg3)
# and save: good R1 reads (arg4), good R2 reads (arg5) , bad R1 reads (arg6), bad R2 reads(arg7)
with gzip.open(sys.argv[1], 'rt') as R1, gzip.open(sys.argv[2], 'rt') as R2, \
        gzip.open(sys.argv[3], 'rt') as KAIJI_output, \
        open(sys.argv[4], 'w') as out_good_R1, open(sys.argv[5], 'w') as out_good_R2, \
open(sys.argv[6], 'w') as out_bad_R1, open(sys.argv[7], 'w') as out_bad_R2:

# Parse fastq files R1 and R2
    ffile1 = SeqIO.parse(R1, "fastq")
    ffile2 = SeqIO.parse(R2, "fastq")
# Parse KAIJI output: take only names(second column) of reads which have flag 'U' - unclassified
    list_of_names = set(line.split('\t')[1] for line in KAIJI_output if line.startswith('U'))
# Count all reads and reads of contaminations
    readscount = 0
    contamincount = 0
# Iterate pair of reads (R1 and R2)
    for seq_record_1, seq_record_2 in zip(ffile1, ffile2):
        readscount += 1

# Checking the identity of paired read names (if reads have flag \1 and \2 ignore it or modify code)
        if seq_record_1.name != seq_record_2.name:
            print('Attention: Problem with reads pairing')
            break

        try:
            # Try to remove name of current read from list of names
            list_of_names.remove(seq_record_1.name)
            # If name in list write reads pair in two files
            out_good_R1.write(seq_record_1.format('fastq'))
            out_good_R2.write(seq_record_2.format('fastq'))

        except KeyError:
            # If there is no read name in list of names count contaminated reads
            contamincount += 1
            # and write contaminated reads pair to two files
            out_bad_R1.write(seq_record_1.format('fastq'))
            out_bad_R2.write(seq_record_2.format('fastq'))

# Calculating the percentage of discarded reads
    contampercent = (contamincount / readscount) * 100
# Print short summary
    print(f'''{readscount} reads were analyzed and {contamincount} of them were rejected. 
This is {contampercent}% of all reads''')

