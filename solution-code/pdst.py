import os
from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def p_dist(s1, s2):
    diff = 0
    for x in range(len(s1)):
        if s1[x] != s2[x]:
            diff += 1
    return str(round(diff/len(s1), 4))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_pdst.txt"
    solution_path = "../solution-outputs/rosalind_pdst.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    sequences = []
    for record in read_fasta(file_path):
        sequences.append(str(record.seq))
    file = open(solution_path, "x")
    for s1 in sequences:
        for s2 in sequences:
            file.write(p_dist(s1, s2))
            file.write(' ')
        file.write('\n')
    file.close()