from Bio import SeqIO

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_sseq.txt"
    s = str(read_fasta(file_path)[0].seq).strip()
    t = str(read_fasta(file_path)[1].seq).strip()
    print(s, t)
    m = 0
    solution = []
    for j in range(len(t)):
        i = s.index(t[j], m, len(s))
        if i > m:
            solution.append(i + 1)
            m = i
    print(solution)
    print(len(solution), len(t))