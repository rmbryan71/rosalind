import os
from Bio import SeqIO

def read_fasta(file):
    records = SeqIO.parse(file, 'fasta')
    return records

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_grph.txt"
    solution_path = "../solution-outputs/rosalind_grph.txt"
    file = open(file_path, "r")
    ### Solving code goes here
    records = read_fasta(file)
    for record in records:
        print(record.seq)
    solution = str(0)
    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)
