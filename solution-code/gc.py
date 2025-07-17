import os
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_gc.txt"
    solution_path = "../solution-outputs/rosalind_gc.txt"
    file = open(file_path, "r")
    ### Solving code goes here
    GCmax = 0
    GCname = ""
    for record in SeqIO.parse(file, "fasta"):
        if GCmax < gc_fraction(record.seq):
            GCmax = gc_fraction(record.seq)
            GCname = record.id
    GCmax *= 100
    solution = GCname + '\n' + '%f' % GCmax
    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)
