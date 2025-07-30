from Bio import SeqIO
from Bio.Seq import Seq

def read_fasta(file):
    return list(SeqIO.parse(file, 'fasta'))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_splc.txt"
    sequence = Seq(str(read_fasta(file_path)[0].seq))
    print(sequence)
    introns = read_fasta(file_path)[1:]
    for intron in introns:
        sequence.replace(str(intron.seq), '')
    sequence.replace('T', 'U')
    print(sequence.translate())




