from Bio import SeqIO
import numpy as np


def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def edit(s, t):
    m = len(s)
    n = len(t)
    d = np.full((m+1, n+1), 0)
    for i in range(0, m+1):
        d[i, 0] = i
    for j in range(0, n+1):
        d[0, j] = j


    for j in range (1, n):
        for i in range(1, m):
            if s[i-1] == t[j-1]:
                substCost = 0
            else:
                substCost = 1
            d[i,j] = min(d[i-1][j] + 1, d[i][j-1] +1, d[i-1][j-1] + substCost)
    # print(d)
    return d[m-1,n-1]

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_edit.txt"
    s = read_fasta(file_path)[0].seq
    t = read_fasta(file_path)[1].seq
    # print(s, t)
    print(len(s), len(t))
    print(edit(s, t))