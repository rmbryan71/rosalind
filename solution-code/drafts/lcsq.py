import os
from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def LCSLength(s, t):
    C = [[0 for i in range(len(s))] for j in range(len(t))]
    for i in range(1, len(s)-1):
        for j in range(1, len(t)-1):
            if s[i] == t[j]:
                C[i][j]=C[i-1][j-1] + 1
            else:
                C[i][j]=max(C[i][j-1], C[i-1][j])
    return C[len(s)][len(t)]

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_lcsq.txt"
    solution_path = "../../solution-outputs/rosalind_lcsq.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    s = read_fasta(file_path)[0].seq
    t = read_fasta(file_path)[1].seq
    print(s)
    print(t)
    print(LCSLength(s, t))
