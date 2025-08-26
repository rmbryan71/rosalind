from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def edit(s, t):
    m = len(s)
    n = len(t)
    d = [[0]*n]*m
    for i in range(1, m):
        d[i][0] = i
    for j in range(1, n):
        d[0][j] = j
    return d

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_edit.txt"
    s = read_fasta(file_path)[0].seq
    t = read_fasta(file_path)[1].seq
    print(s, t)
    print(edit(s, t))