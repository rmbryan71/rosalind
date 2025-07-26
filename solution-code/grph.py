import os
from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_grph.txt"
    solution_path = "../solution-outputs/rosalind_grph.txt"
    ### Solving code goes here
    records = read_fasta(file_path)
    solution = []

    for record_a in records:
        # print(record_a.seq)
        for record_b in records:
            #print(record_a.seq, record_b.seq)
            # print(record_a.seq[0:3], record_b.seq[-3:])
            if record_a.id != record_b.id:
                if record_a.seq[0:3] == record_b.seq[-3:]:
                    # print(record_a.seq[0:3], record_b.seq[-3:])
                    solution.append(record_b.id + ' ' + record_a.id)
    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    for item in solution:
        print(item)
        file.write(item + '\n')
    file.close()
