import os
from orffinder import orffinder
from Bio import SeqIO

def read_fasta(file):
    return SeqIO.read(file, 'fasta')

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_orf.txt"
    solution_path = "/Users/robertbryan/PycharmProjects/rosalind/solution-outputs/"
    ### Solving code goes here
    sequence = read_fasta(file_path)
    print (orffinder.getORFs(sequence, minimum_length=3, trim_trailing = True))