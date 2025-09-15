from Bio import SeqIO
from functools import cache

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def isComplement(a, b):
    if a == 'A' and b == 'U':
        return True
    if a == 'U' and b == 'A':
        return True
    if a == 'C' and b == 'G':
        return True
    if a == 'G' and b == 'C':
        return True
    else:
        return False

@cache
def rnas(dna):
    if len(dna) == 1:
        return 1
    if len(dna) == 0:
        return 1
    else:
        return (
            rnas(dna[1:])
            + sum(
                rnas(dna[1:m]) * rnas(dna[m + 1 :])
                for m in range(1, len(dna))
                if isComplement(dna[0], dna[m])
            )
            % 1000000
        )

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_rnas_sample.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    print(s)
    print(len(s))
    print(rnas(s) % 1000000)