from Bio import SeqIO
from Bio import AlignIO
import re
from collections import defaultdict


def get_locus_list(filename, protein_id):

    gene_list = list()
    locus_list = list()
    protein_list = list()

    for seq_record in SeqIO.parse(filename, "genbank"):
        for f in seq_record.features:
            for qualifier in f.qualifiers:

                if qualifier == 'protein_id':
                    if f.qualifiers['protein_id'][0] == protein_id:

                        protein_list.append(f.qualifiers['translation'][0])
        locus_dict = protein_list

    return locus_dict
#
# ortholog_genes = {}
# input = open("orthologs.txt")
# pattern = '[B-W]{2}[0-9]{3,}_[0-9]{3,}'
# regex = re.compile(pattern)
#
# gene_orthologs_parsed = list()
# for j in input:
#     gene_orthologs_parsed.append(regex.search(j).group())

bw25113 = get_locus_list('bw25113Sequence.gb', 'AIN33564.1')
nissle = get_locus_list("nissleSequence.gb", 'AID80356.1')

print(bw25113)
print(nissle)

# for locus in bw25113:
#     if locus in gene_orthologs_parsed:
#         ortholog_genes[locus] = bw25113[locus]
#
# print(ortholog_genes)


