#!/usr/bin/env python3

from Bio import SeqIO
import sys

ffile = SeqIO.parse(sys.argv[1], "fasta")
header_set = set(line.strip() for line in open(sys.argv[2]))

for seq_record in ffile:
    try:
        header_set.remove(seq_record.name)
        print(seq_record.format("fasta"))
    except KeyError:
        continue
# if len(header_set) != 0:
#     print(len(header_set),'of the headers from list were not identified in the input fasta file.', file=sys.stderr)

### usage:
### filter_fasta_by_list_of_headers.py input.fasta list_of_scf_to_filter > filtered.fasta
### P.S. it's quite easy to turn over the script to extract the sequences from the list (just the print line would have to move after line header_set.remove(seq_record.name)
