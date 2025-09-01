from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

def isComplement(a, b):
    if a == 'A' and b == 'U':
        return True
    if a == 'U' and b == 'A':
        return True
    if a == 'C' and b == 'G':
        return True
    if a == 'G' and b == 'C':
        return True
    else:
        return False

def motzkin(dna):
    return False

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_motz_sample.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    print(motzkin(s))

