from Bio import SeqIO
from suffix_trees import STree

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_lcsm.txt"
    strings = []
    for x in read_fasta(file_path):
        strings.append(str(x.seq))
    st = STree.STree(strings)
    print(st.lcs())

