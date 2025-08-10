from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def x(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    else:
        return ((2*n)-1) * x(n - 1)

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_pmch.txt"
    sequence = str(read_fasta(file_path)[0].seq)
    # print(sequence)
    A = sequence.count("A")
    G = sequence.count("G")
    # print(A, G)
    print(fact(A) * fact(G))




