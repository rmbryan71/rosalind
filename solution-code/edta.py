from Bio import SeqIO, Align
import numpy as np
import os

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def edta(s1, s2):
    """Edit Distance Alignment"""
    # initialise
    m, p = {}, {}
    for j in range(len(s2) + 1):
        m[j, 0] = j
        p[j, 0] = [j - 1, 0]

    for i in range(len(s1) + 1):
        m[0, i] = i
        p[0, i] = [0, i - 1]

    # fill matrices
    for j in range(len(s2)):
        for i in range(len(s1)):
            if s1[i] == s2[j]:
                m[j + 1, i + 1] = m[j, i]
                p[j + 1, i + 1] = [j, i]
            else:
                opt = [m[j + 1, i], m[j, i], m[j, i + 1]]
                m[j + 1, i + 1] = min(opt) + 1
                p[j + 1, i + 1] = [[j + 1, i], [j, i], [j, i + 1]][opt.index(min(opt))]

    # traceback
    a1, a2 = "", ""
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if p[j, i] == [j - 1, i - 1]:
            a1 += s1[i - 1]
            a2 += s2[j - 1]
        elif p[j, i] == [j, i - 1]:
            a1 += s1[i - 1]
            a2 += "-"
        elif p[j, i] == [j - 1, i]:
            a1 += "-"
            a2 += s2[j - 1]
        j, i = p[j, i]

    return {"dist": m[len(s2), len(s1)], "a1": a1[::-1], "a2": a2[::-1]}

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_edta.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    t = str(read_fasta(file_path)[1].seq).strip()
    # print(s, t)
    solution = (edta(s, t))
    print(solution["dist"], solution["a1"], solution["a2"], sep='\n')

