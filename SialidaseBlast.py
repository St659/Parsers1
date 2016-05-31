from Bio.Align.Applications import ClustalOmegaCommandline


input_file = "gh33.fasta"
output_file = "aligned.fasta"
clustal = ClustalOmegaCommandline(infile=input_file, outfile=output_file, verbose=True,auto=True)
print(clustal)