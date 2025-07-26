import os
from Bio import SeqIO
from Bio import motifs

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def consensus(file_path):
    instances = []
    for record in read_fasta(file_path):
        instances.append(record.seq)
    m = motifs.create(instances)
    return str(m.consensus)

def matrix(file_path):
    instances = []
    for record in read_fasta(file_path):
        instances.append(record.seq)
    m = motifs.create(instances)
    return str(m.counts).replace('.00','').replace('   ', ' ')

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_cons.txt"
    solution_path = "../solution-outputs/rosalind_cons.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    # print(consensus(file_path))
    # print(matrix(file_path))
    file = open(solution_path, "x")
    file.write(consensus(file_path))
    file.write('\n')
    file.write(matrix(file_path))
    file.close()

# This solution requires a manual edit of the solution file to remove the column headers from the matrix section