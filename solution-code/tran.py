from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_tran.txt"
    s1 = str(read_fasta(file_path)[0].seq).strip()
    s2 = str(read_fasta(file_path)[1].seq).strip()
    # print(len(s1), len(s2))
    transitions = 0
    transversions = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == 'A':
                if s2[i] in ('T', 'C'):
                    transversions += 1
                else:
                    transitions += 1
            if s1[i] == 'G':
                if s2[i] in ('T', 'C'):
                    transversions += 1
                else:
                    transitions += 1
            if s1[i] == 'C':
                if s2[i] in ('A', 'G'):
                    transversions += 1
                else:
                    transitions += 1
            if s1[i] == 'T':
                if s2[i] in ('A', 'G'):
                    transversions += 1
                else:
                    transitions += 1
    print(transitions/transversions)
