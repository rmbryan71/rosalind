from Bio import SeqIO
from Bio.Seq import Seq

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def reverse_complement(string):
    return string.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]

def rev_pal(set, length):
    results = []
    for i in range(len(set) + 1 - length):
        candidate = (set[i: i+length])
        if candidate == reverse_complement(candidate):
            results.append([i + 1, length])
    return results

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_revp.txt"
    dna = open(file_path, 'r').read()
    results = []
    for j in range(4,12):
        if len(rev_pal(dna, j)) > 0:
            results.append(rev_pal(dna, j))
    for item in results:
        for i in item:
            print(str(i).replace('[', '').replace(']', '').replace(',', ''))

