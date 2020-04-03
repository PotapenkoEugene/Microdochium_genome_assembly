#!/usr/bin/env python3

from Bio import SeqIO
import sys

ffile = SeqIO.parse(sys.argv[1], "fasta")
header_set = [line.strip() for line in open(sys.argv[2])]


# with open('./filtered_contigs_v2.fasta', 'w') as w, open('./contamination_contigs_v2.fasta', 'w') as w2:
#     for contigs in ffile:
#         for k_seq in header_set:
#             splt_seq = k_seq.split('\t')
#             if contigs.name == splt_seq[1]:
#                 if splt_seq[0] == 'U':
#                     w.write('>' + contigs.name + '\n' +
#                             str(contigs.seq) + '\n')
#                     # find another taxid in raw reads but not in contigs
#
#                     w.write('>' + contigs.name + '\n' +
#                             str(contigs.seq) + '\n')
#                 else:
#                     w2.write('>' + contigs.name + '\n' +
#                              str(contigs.seq) + '\n')
#
### usage:
### filter_fasta_by_list_of_headers.py input.fasta list_of_scf_to_filter > filtered.fasta
### P.S. it's quite easy to turn over the script to extract the sequences from the list
# (just the print line would have to move after line header_set.remove(seq_record.name)
