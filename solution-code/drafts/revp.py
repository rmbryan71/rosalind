from Bio import SeqIO

def reverse_complement(string):
    return string.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]

def read_fasta(file):
    handle = open(file)
    record = list(SeqIO.parse(handle, "fasta"))
    handle.close()
    return str(record[0].seq)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_revp.txt"
    # dna = open(file_path, 'r').read()
    dna = read_fasta(file_path)
    print(dna)
    for i in range(len(dna)):
        for j in range(4,13):
            if i + j <= len(dna) and dna[i: i+j] == reverse_complement(dna[i: i+j]):
                print(i+1, j)

