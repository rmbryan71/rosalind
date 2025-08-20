import os
from Bio import SeqIO
from Bio.Seq import Seq

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def hamm(a, b):
    solution = 0
    length = len(a)
    for i in range(0, length - 1):
        if a[i] != b[i]:
            solution += 1
    # print(a, b, solution)
    return solution

def clean(seqs):
    removals = []
    result = seqs
    for i in range(len(seqs)):
        for j in range(len(seqs)):
            if i != j:
                if seqs[i] == seqs[j]:
                    if i not in removals:
                        removals.append(i)
                if seqs[i] == Seq.reverse_complement(seqs[j]):
                    if i not in removals:
                        # print(sequences[i], " is the reverse complement of ", sequences[j])
                        removals.append(i)
    removals.sort(reverse = True)
    for k in removals:
        del result[k]
    return result

def corrections(errors, sequences):
    response = []
    for s in errors:
        for t in sequences:
            if hamm(str(s), str(t)) == 1:
                if (s, "->", t) not in response:
                    response.append(s, "->", t)
            if hamm(s, Seq.reverse_complement(t)) == 1:
                print(s, "->", t)
    return 0

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_corr.txt"
    solution_path = "../solution-outputs/rosalind_corr.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    sequences = []
    for record in read_fasta(file_path):
        sequences.append(record.seq)
    # print(sequences)
    errors = clean(sequences)
    print(errors)
    all_sequences = []
    for record in read_fasta(file_path):
        all_sequences.append(record.seq)
    print(all_sequences)
    print(corrections(errors, all_sequences))



    # file = open(solution_path, "x")
    # file.close()