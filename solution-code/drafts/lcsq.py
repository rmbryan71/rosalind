import os, sys
from Bio import SeqIO

sys.setrecursionlimit(1500)

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def LCSLength(s, t):
    C = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                C[i][j]=C[i-1][j-1] + 1
            else:
                C[i][j]=max(C[i][j-1], C[i-1][j])
    return C

def backtrack(C, s, t, i, j):
    if i == 0:
        return ""
    if j == 0:
        return ""
    if s[i] == t[j]:
        return backtrack(C, s, t, i-1, j-1) + s[i]
    if C[i][j-1] > C[i-1][j]:
        return backtrack(C, s, t, i, j-1)
    else:
        return backtrack(C, s, t, i-1, j)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_lcsq.txt"
    solution_path = "../../solution-outputs/rosalind_lcsq.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    s = read_fasta(file_path)[0].seq
    t = read_fasta(file_path)[1].seq
    s = str(s).strip()
    t = str(t).strip()
    print(LCSLength(s,t))
    print(backtrack((LCSLength(s,t)), s, t, len(s)-1, len(t)-1))
