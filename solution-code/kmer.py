import os
from Bio import SeqIO
from itertools import product

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def build_dictionary():
    dict = {}
    for item in product('ACGT', repeat=4):
        dict[item] = 0
    return dict

def populate(sequence, dictionary):
    for i in range(len(sequence) - 3):
        kmer = sequence[i:i+4]
        lookup = (str(kmer[0]), str(kmer[1]), str(kmer[2]), str(kmer[3]))
        # print(kmer)
        dictionary[lookup] += 1
    return dictionary


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_kmer.txt"
    solution_path = "../solution-outputs/rosalind_kmer.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    sequence = str(read_fasta(file_path)[0].seq)
    # print(sequence)
    dictionary = build_dictionary()
    # print(dictionary)
    # print(len(dictionary))
    dict2 = populate(sequence, dictionary)
    file = open(solution_path, "x")
    file.write(str((list(dict2.values()))).replace('[','').replace(']','').replace(',', ''))
    file.close()