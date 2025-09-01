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

def catalan(dna, cata):
    if dna in cata:
        return cata[dna]
    n = len(dna)
    c = 0
    for m in range(1, n ,2):
        if isComplement(dna[0], dna[m]):
            c += (catalan(dna[1:m], cata) * catalan(dna[m+1:], cata))
    cata[dna] = c
    return cata[dna]

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_motz_sample.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    cata = {'': 1, 'AU': 1, 'UA': 1, 'GC': 1, 'CG': 1}
    print(catalan(s, cata) % 1000000)

